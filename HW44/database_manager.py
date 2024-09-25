from pymongo import MongoClient, ASCENDING
from bson.objectid import ObjectId
from models import Student
from typing import List, Optional, Dict, Any


class ManagerDB:
    def __init__(self, uri: str, db_name: str):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db['students']

    def insert_student(self, students: List[Student]):
        try:
            result = self.collection.insert_many([student.dict() for student in students])
            print(f'Студент добавлений з ID: {result.inserted_ids}')
        except Exception as e:
            print(f'Помилка добавлення: {e}')

    def get_students(self, sort_key: Optional[str] = None, sort_order: Optional[int] = ASCENDING,
                     projection: Optional[Dict[str, int]] = None) -> List[Dict[str, Any]]:
        try:
            cursor = self.collection.find({}, projection)
            if sort_key:
                cursor = cursor.sort(sort_key, sort_order)
            return list(cursor)
        except Exception as e:
            print(f'Помилка отримання: {e}')
            return []

    def update_student(self, student_id: str, update_data: Dict[str, Any]):
        try:
            result = self.collection.update_one({"_id": ObjectId(student_id)}, {"$set": update_data})
            print(f'Початкові дані студента: {result.matched_count}, модифіковані: {result.modified_count}')
        except Exception as e:
            print(f'Помилка оновлення студента: {e}')

    def delete_student(self, student_id: str):
        try:
            result = self.collection.delete_one({"_id": ObjectId(student_id)})
            print(f'Видалений студент: {result.deleted_count}')
        except Exception as e:
            print(f'Студента з таким ID не існує: {e}')

    def filter_students(self, filter_criteria: Dict[str, Any],
                        projection: Optional[Dict[str, int]] = None) -> List[Dict[str, Any]]:
        try:
            return list(self.collection.find(filter_criteria, projection))
        except Exception as e:
            print(f'Такого сортування не існує: {e}')
            return []
