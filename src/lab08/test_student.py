from models import Student  # импортируем класс
from datetime import datetime

def test_student_creation():
    """Тест создания студента"""
    student = Student(
        fio="Иванов Иван Иванович",
        birthdate="2000-05-15",
        group="ИТ-101", 
        gpa=4.5
    )

    print("создаём студента:")
    print(student)
    print()

def test_student_methods():
    """Тест методов студента"""

    student = Student("Петрова Анна", "2002-12-31", "ФИ-102", 3.8)
    
    print("тестируем методы студента:")
    print(f"age(): {student.count_age()} лет")
    print(f"to_dict(): {student.to_dict()}")
    print()

def test_student_validation():
    print("проверка ошибок:")
    """Тест валидации"""
    try:
        student = Student("Сидоров", "2000-13-45", "МТ-101", 4.0)  # неправильная дата
        student = Student("Сидоров", "2000-09-23", "МТ-101", 6.0)  # неправильный GPA
    except ValueError as e:
        
        print(f"Ошибка: {e}")
    print()

def test_from_dict():
    """Тест создания из словаря"""
    data = {
        'fio': 'Козлова Мария',
        'birthdate': '2001-08-20',
        'group': 'ИТ-103',
        'gpa': 4.2
    }
    student = Student.from_dict(data)
    print(f"Студент создан из словаря: {student.fio}, {student.birthdate}, {student.group}, {student.gpa}")
    print()

if __name__ == "__main__":
    test_student_creation()
    test_student_methods() 
    test_student_validation()
    test_from_dict()
