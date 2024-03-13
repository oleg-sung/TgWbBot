import datetime

import asyncio

from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession

from app.notification.base import scheduled_task as scheduled_task, send_notification
from app.keyboard.inline import inline
from app.keyboard.reply import reply
from app.db.orm_query import orm_add_product, orm_get_product
from app.service.wb_servises import get_item_by_articyl, validate_articyl

router = Router()


class Art(StatesGroup):
    id = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"Здравствуйте {message.from_user.first_name}! 🖐🏻\n\n"
        "Это бот для быстрого поиска товаров по артиклю Wildberries!\n\n"
        "Выберите одну из кнопок:\n"
        "1⃣ Для поиска товара по артиклю - Получить информацию по товару 🌐\n\n"
        "2⃣ Для остановки увидомлений по товару - Остановить уведомления ❌\n\n"
        "3⃣ Для просмотра истории поиска - Получить информацию из БД 💽",
        reply_markup=reply,
    )


@router.message(F.text == "Получить информацию по товару")
async def get_item_info(message: Message, state: FSMContext):
    await state.set_state(Art.id)
    await message.answer(
        f"Артикул товара состоит из 9 цифр ❗\nВведите артикул тавара 👇",
        reply_markup=reply,
    )


@router.message(F.text == "Остановить уведомления")
async def stop_notification(message: Message):
    await send_notification(message.from_user.id, status=False)
    await message.answer(f"❌ Уведомление остановленны ❌", reply_markup=reply)


@router.message(Art.id)
async def cheak_art(message: Message, state: FSMContext, session: AsyncSession):
    await state.update_data(id=message.text)
    art = await state.get_data()
    await state.clear()
    validate_data = await validate_articyl(art["id"])
    if validate_data is not art["id"]:
        await message.answer(validate_data, reply_markup=reply)
    else:
        data = await get_item_by_articyl(validate_data)
        if isinstance(data, str):
            await message.answer(text=data, reply_markup=reply)
        else:
            await message.answer(
                f"📦 {data['name']} 📦\n\n"
                f"🧮 Артикул товара: {data['id']}\n"
                f"💵 Цена: {data['price']//100} рублей\n"
                f"🗃 Колличество товара на складах: {data['qty']}шт.",
                reply_markup=inline,
            )

            history_date = {"user_id": message.from_user.id, "art": int(validate_data)}
            await orm_add_product(session, history_date)


@router.message(F.text == "Получить информацию из БД")
async def get_info_from_db(message: Message, session: AsyncSession):
    data = await orm_get_product(session, message.from_user.id)
    text = "📦 История поиска товаров 📦\n"
    count = 0
    for item in data:
        count += 1
        t = (
            f"\n\n{count}. 🧮 Артикул товара: {item.art}\n"
            f"Дата и время просмотра: {item.created.replace(microsecond=0) + datetime.timedelta(hours=3)}"
        )
        text += t
    await message.answer(f"{text}", reply_markup=reply)


@router.callback_query(lambda c: c.data == "subscribe")
async def subscribe(call: CallbackQuery):
    await call.answer("✅ Вы подписались на уведомления ✅", reply_markup=reply)
    scheduled_task[call.from_user.id] = asyncio.create_task(
        send_notification(call.from_user.id, text=call.message.text)
    )
