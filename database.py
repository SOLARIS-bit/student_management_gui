import json
import os

class Database:
    def __init__(self, filename="student_data.json"):
        self.filename = filename

    def save_data(self, students, subjects, grades):
        data = {
            "students": students,
            "subjects": subjects,
            "grades": grades
        }
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=4)

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                data = json.load(f)
                return data.get("students", []), data.get("subjects", []), data.get("grades", {})
        return [], [], {}

