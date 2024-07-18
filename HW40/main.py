from operations import (re_create_table, add_student, get_all_info, update_grade_by_id,
                        delete_grade_by_id, get_grade_info, get_avg_subjects_scores, get_student_scores_by_last_name,
                        add_static_student)
from random import randint, choice

if __name__ == '__main__':
    re_create_table()
    add_static_student()
    for _ in range(15):
        add_student(randint(10, 100), choice(["math", "physics"]))
    get_all_info("math")
    update_grade_by_id(2, "math", 10)
    delete_grade_by_id(3)
    get_grade_info()
    get_avg_subjects_scores()
    get_student_scores_by_last_name("Філь")