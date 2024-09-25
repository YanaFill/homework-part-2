from database_manager import ManagerDB
from models import UpdateStudent
from utils import parse_sort_order, generate_fake_students


if __name__ == "__main__":
    db_manager = ManagerDB(uri="mongodb://localhost:27017/", db_name="university")
    fake_students = generate_fake_students(2)
    db_manager.insert_student(fake_students)
    students = db_manager.get_students(sort_key="year_of_admission", sort_order=parse_sort_order("asc"),
                                       projection={"last_name": 1, "year_of_admission": 1})
    print(f"Усі студенти: {students}")

    update_data = UpdateStudent(email="wowa@gmail.com")
    db_manager.update_student(student_id="669d173ae33a9145ac2f05d8", update_data=update_data.dict(exclude_unset=True))
    db_manager.delete_student(student_id="669d173ae33a9145ac2f05d9")
    filtered_students = db_manager.filter_students(filter_criteria={"year_of_admission": 2021})
    print(f"Filtered Students: {filtered_students}")
