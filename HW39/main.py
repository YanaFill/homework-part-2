from operations import (re_create_table, add_student,
                        get_count_students, get_all, get_budget,
                        update_student, delete_student)

if __name__ == '__main__':
    re_create_table()
    for _ in range(15):
        add_student()
    update_student(4, "loh@gmail.com")
    delete_student(1)
    get_budget()
    get_all()
    get_count_students()


