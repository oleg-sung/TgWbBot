import asyncio

from app.keyboard.reply import reply


scheduled_task = {}


async def send_notification(chat_id, text=None, status: bool = True):
    while status:
        from run import bot
        await asyncio.sleep(10)
        await bot.send_message(chat_id, text, reply_markup=reply)
    scheduled_task[chat_id].cancel()
    scheduled_task[chat_id] = None
