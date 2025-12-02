from serialize import students_from_json, students_to_json

def demonstrate_serialization():
    students = students_from_json('data/lab08/students_input.json')
    print("\n Загруженные студенты:")
    for student in students:
        print(f"fio: {student.fio}, birthdate: {student.birthdate}, group: {student.group}, GPA: {student.gpa}")
    print("\n Сохранение в выходной файл")
    students_to_json(students, 'data/lab08/students_output.json')
    print("Файл сохранен: data/lab08/students_output.json")

if __name__ == "__main__":
    demonstrate_serialization()