from database import Session as SessionMaker, engine
from models import Base, Student, Grade
from database import engine
from sqlalchemy import select, update, delete, func
from datetime import date
from faker import Faker


def re_create_table():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


fake = Faker(locale='uk_UA')


# Table Student

def add_static_student():
    with SessionMaker() as session:
        student=Student(
            first_name="Яна",
            last_name="Філь",
            email="yana2004rt@gmail.com",
            birth_date=date(2004,7,2),
            is_budget=True,
            grades=[
                Grade(
                    score=99,
                    subject="math"
                )
            ]

        )
        session.add(student)
        session.commit()


def add_student(user_score: int, user_subject: str):
    with SessionMaker() as session:
        student = Student(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            birth_date=fake.date_of_birth(minimum_age=17, maximum_age=25),
            is_budget=fake.boolean(),
            grades=[
                Grade(
                    score=user_score,
                    subject=user_subject
                )
            ]
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

#Table Grade

#Read
def get_grade_info():
    with SessionMaker() as session:
        stmt = select(Grade.id, Grade.subject, Grade.score, Grade.student_id, Grade.student).join(Grade)
        result = session.execute(stmt)
        for row in result:
            print(row)


# Операція Update
def update_grade_by_id(user_id: int, new_subject: str, new_score: int):
    with SessionMaker() as session:
        stmt = (
            update(Grade).
            where(Grade.id == user_id).
            values(subject=new_subject, score=new_score)
        )
        session.execute(stmt)
        session.commit()
        pass


# Операція Delete
def delete_grade_by_id(user_id: int):
    with SessionMaker() as session:
        stmt = delete(Grade).where(Grade.id == user_id)
        session.execute(stmt)
        session.commit()


# Отримання списку студентів та їх оцінок з певного заданого предмета, відсортувавши по дані по прізвищу.
def get_all_info(subject: str):
    with SessionMaker() as session:
        stmt = select(Student.id, Student.first_name, Student.last_name, Grade.subject, Grade.score
                      ).join(Student.grades).where(Grade.subject == subject).order_by(Student.last_name)
        result = session.execute(stmt)
        for row in result:
            print(row)


# Отримання всіх оцінок певного студента за його прізвищем.
def get_student_scores_by_last_name(user_last_name: str):
    with SessionMaker() as session:
        stmt = select(Student.last_name, Grade.subject, Grade.score
                      ).join(Student.grades).where(Student.last_name == user_last_name)
        result = session.execute(stmt)
        for row in result:
            print(row)


# Отримання середньої оцінки по кожному предмету.
def get_avg_subjects_scores():
    with SessionMaker() as session:
        stmt = select(Grade.subject, func.avg(Grade.score).label('average_score')
                      ).group_by(Grade.subject)
        result = session.execute(stmt)
        for row in result:
            print(f"Subject: {row.subject}, Average Score: {row.average_score:.2f}")