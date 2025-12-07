from src.lab09.group import Group
from src.lab08.models import Student

def quick_test():
    
    test_file = "data/lab09/students.csv"
        
    # 1. Создаём Group
    group = Group(test_file)

    
    print("1. Просмотр всех студентов:")
    students = group.list()
    for student in students:
        print(student)
    print()
    
  
    print("2. Добавление нового студентa:")
    students_to_add = [
        ("Иванов Иван", "2003-10-10", "БИВТ-21-1", 4.3),
        ("Петров Петр", "2002-05-15", "БИВТ-21-2", 4.7),
        ("Сидорова Анна", "2003-02-10", "БИВТ-21-1", 4.9),
    ]
    
    for fio, date, grp, gpa in students_to_add:
        student = Student(fio, date, grp, gpa)
        if group.add(student):
            print(f"Добавлен: {fio}")
        else:
            print(f"Ошибка: {fio}")
    print()

    print("3. Список студентов после добавления:")
    students = group.list()
    for student in students:
        print(student)
    print()
    
    print("4. Поиск студентов по подстроке 'Иаан':")
    found_students = group.find("Иван")
    for s in found_students:
        print(s)
    print()
    
    print("5. Обновление информации о студенте:")
    if group.update("Петров Петр", gpa=5.0, group="БИВТ-21-9"):
        print("данные у Петра обновлены")
    print()
   
    print("6. Удаление студента:")
    if group.remove("Сидорова Анна"):
        print("Студент Анна удалён")
    print()
    
    print("7. Финальный список студентов:")
    students = group.list()
    for s in students:
        print(s)
    print()
    

if __name__ == "__main__":
    quick_test()