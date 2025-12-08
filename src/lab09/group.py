from src.lab08.models import Student
from src.lab04.io_txt_csv import ensure_parent_dir, write_csv
from pathlib import Path
import csv

class Group:
    def __init__(self, csv_path: str):
        """инициализация хранилища студентов"""
        self.csv_path = Path(csv_path)
        self._ensure_file_exists()
    
    def _ensure_file_exists(self):
        """создаёт папку и файл, если их нет"""
        if not self.csv_path.exists():
            ensure_parent_dir(self.csv_path)
            write_csv([], self.csv_path, header=("fio", "birthdate", "group", "gpa"))
    
    def _read_all(self):
        """читает всех студентов из файла"""
        students = []
        
        try:
            with open(self.csv_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    gpa = row.get('gpa', '0')
                    gpa = float(gpa)
                    
                    try:
                        student = Student(
                            fio=row.get('fio', '').strip(),
                            birthdate=row.get('birthdate', '').strip(),
                            group=row.get('group', '').strip(),
                            gpa=gpa
                        )
                        students.append(student)
                    except ValueError as e:
                        print(f"Ошибка создания студента: {e}")
                        continue
                        
        except FileNotFoundError:
            pass
        
        return students
    
    def _save_students(self, students):
        """Сохраняет список студентов в файл"""
        with open(self.csv_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['fio', 'birthdate', 'group', 'gpa'])
            writer.writeheader()
            
            for student in students:
                writer.writerow({
                    'fio': student.fio,
                    'birthdate': student.birthdate,
                    'group': student.group,
                    'gpa': str(student.gpa)
                })
    
    def list(self):
        """возвращает всех студентов в виде списка"""
        return self._read_all()
    
    def add(self, student: Student):
        """добавляет нового студента"""
        all_students = self._read_all()
        
        for s in all_students:
            if s.fio.lower() == student.fio.lower():
                print(f"Студент '{student.fio}' уже существует")
                return False
        
        all_students.append(student)
        self._save_students(all_students)
        return True
    
    def find(self, need_fio: str):
        """находит студента по подстроке fio"""
        all_students = self._read_all()
        found = []
        need_fio = need_fio.lower()
        
        for student in all_students:
            if need_fio in student.fio.lower():
                found.append(student)
        
        return found
    
    def remove(self, extra_fio: str):
        """удаляет запись с данным fio"""
        all_students = self._read_all()
        new_list = []
        extra_fio = extra_fio.lower()
        
        for student in all_students:
            if student.fio.lower() != extra_fio:
                new_list.append(student)
        
        if len(new_list) < len(all_students):
            self._save_students(new_list)
            return True
        else:
            print(f"Студент '{extra_fio}' не найден")
            return False
    
    def update(self, fio: str, **changes):
        """обновляет поля существующего студента
        **changes - можно передавать любое количество полей для обновления
        ** превращает переданные параметры в словарь"""
        all_students = self._read_all()
        updated = False
        
        for student in all_students:
            if student.fio.lower() == fio.lower():
                if 'group' in changes:
                    student.group = str(changes['group'])
                if 'gpa' in changes:
                    student.gpa = float(changes['gpa'])
                if 'birthdate' in changes:
                    student.birthdate = str(changes['birthdate'])
                updated = True
                break
        
        if updated:
            self._save_students(all_students)
        
        return updated
    