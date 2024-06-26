from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Date, Boolean, DateTime, func
from datetime import datetime, date


class Base(DeclarativeBase):
    pass


class Student(Base):
    __tablename__ = "students"
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(30))
    birth_date: Mapped[date] = mapped_column(Date)
    is_budget: Mapped[bool] = mapped_column(Boolean)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())

    def __repr__(self):
        return (f"id = {self.id}, first_name = {self.first_name}, last_name = {self.last_name},"
                f"email = {self.email}, b-day = {self.birth_date}, budget = {self.is_budget}, created_at = {self.created_at}")
