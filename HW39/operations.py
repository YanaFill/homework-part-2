from database import Session as SessionMaker
from models import Base, Student
from database import engine
from sqlalchemy import select, update, delete, func
from datetime import date
from faker import Faker


def re_create_table():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


fake = Faker(locale='uk_UA')


def add_student():
    with SessionMaker() as session:
        student = Student(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            birth_date=fake.date_of_birth(minimum_age=17, maximum_age=25),
            is_budget=fake.boolean()
        )
    session.add(student)
    session.commit()


def get_all():
    with SessionMaker() as session:
        stmt = select(Student).order_by(Student.last_name)
        result = session.scalars(stmt)
        for row in result:
            print(row)


def update_student(id: int, email: str):
    with SessionMaker() as session:
        stmt = update(Student).where(Student.id == id).values(email=email)
        session.execute(stmt)
        session.commit()


def delete_student(id: int):
    with SessionMaker() as session:
        stmt = delete(Student).where(Student.id == id)
        session.execute(stmt)
        session.commit()


def get_budget(): # Отримання всіх студентів на бюджеті, які народилися після заданої дати
    with SessionMaker() as session:
        stmt = select(Student).where(Student.is_budget, Student.birth_date > date(2004, 7, 2))
        result = session.scalars(stmt)
        for row in result:
            print(row)


def get_count_students(): # Отримання загальної кількості студентів у базі даних
    with SessionMaker() as session:
        stmt = select(func.count(Student.first_name))
        result = session.execute(stmt).all()
        print(result)
