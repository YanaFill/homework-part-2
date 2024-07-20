from models import Base, Student, Course
from database import engine, SessionLocal
from faker import Faker
import random

fake = Faker(locale="uk_UA")


def re_create_tables():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


def add_data():
    session = SessionLocal()
    try:
        courses = [
            Course(name="Math", description=fake.sentence(), hours=random.randint(1, 10)),
            Course(name="Science", description=fake.sentence(), hours=random.randint(1, 10)),
            Course(name="History", description=fake.sentence(), hours=random.randint(1, 10)),
            Course(name="Art", description=fake.sentence(), hours=random.randint(1, 10)),
            Course(name="Music", description=fake.sentence(), hours=random.randint(1, 10)),
        ]

        students = [Student(first_name=fake.first_name(), last_name=fake.last_name()) for _ in range(10)]

        session.add_all(students + courses)
        session.commit()

        for student in students:
            enrolled_courses = random.sample(courses, random.randint(1, len(courses)))
            student.courses.extend(enrolled_courses)
        session.commit()
    finally:
        session.close()


def get_student_courses(student_id: int):
    session = SessionLocal()
    try:
        student = session.query(Student).filter(Student.id == student_id).one_or_none()
        if student:
            print(f"Курси студента {student.first_name} {student.last_name}:")
            for course in student.courses:
                print(course.name)
        else:
            print(f"Студента з id {student_id} не знайдено")
    finally:
        session.close()


def get_course_students(course_name: str):
    session = SessionLocal()
    try:
        course = session.query(Course).filter(Course.name == course_name).one_or_none()
        if course:
            print(f"Студенти, записані на курс {course.name}:")
            for student in course.students:
                print(student.first_name, student.last_name)
        else:
            print(f"Курс з назвою {course_name} не знайдено")
    finally:
        session.close()
