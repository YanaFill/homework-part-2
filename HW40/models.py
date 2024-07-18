from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Date, Boolean, DateTime, func, Integer, ForeignKey
from datetime import datetime, date
from typing import List

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

    grades: Mapped[List['Grade']] = relationship(back_populates="student")

    def __repr__(self):
        return (f"id = {self.id}, first_name = {self.first_name}, last_name = {self.last_name},"
                f"email = {self.email}, b-day = {self.birth_date}, budget = {self.is_budget}, created_at = {self.created_at}")

class Grade(Base):
    __tablename__ = "grades"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    subject: Mapped[str] = mapped_column(String(30))
    score: Mapped[int] = mapped_column(Integer)
    student_id: Mapped[int] = mapped_column(ForeignKey(Student.id))

    student: Mapped['Student'] = relationship(back_populates="grades")

    def __repr__(self):
        return f"Grade(id={self.id}, subject={self.subject}, score={self.score}, student={self.student}\n"


