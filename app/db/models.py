from datetime import datetime

import pytz
from sqlalchemy import DateTime, func, BigInteger
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class History(Base):
    __tablename__ = "history"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    created: Mapped[DateTime] = mapped_column(
        DateTime, default=func.now(), nullable=False
    )
    art: Mapped[int] = mapped_column(BigInteger, nullable=False)
