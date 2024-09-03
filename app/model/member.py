from datetime import datetime

from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped

from app.model.base import Base


class Member(Base):
    __tablename__ = 'member'

    mno: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    userid: Mapped[str] = mapped_column(String(18), unique=True, nullable=False, index=True) # 식별관계
    # userid: Mapped[str] = mapped_column( index=True) # 비식별관계
    passwd: Mapped[str] = mapped_column(String(18))
    name: Mapped[str] = mapped_column(String(10))
    email: Mapped[str] = mapped_column(String(100))
    regdate: Mapped[datetime] = mapped_column(default=datetime.now)