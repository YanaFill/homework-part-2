from operations import re_create_tables, add_data, get_student_courses, get_course_students
from random import randint

if __name__ == "__main__":
    re_create_tables()
    add_data()
    get_student_courses(randint(1, 10))
    get_course_students("Math")
