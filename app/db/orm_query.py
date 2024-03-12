from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import History


async def orm_add_product(session: AsyncSession, data: dict):
    obj = History(
        user_id=data["user_id"],
        art=data["art"],
    )
    session.add(obj)
    await session.commit()


async def orm_get_product(session: AsyncSession, user_id: int):
    query = (
        select(History)
        .filter(History.user_id == user_id)
        .order_by(History.created.desc())
        .limit(5)
    )
    result = await session.execute(query)
    return result.scalars().all()
