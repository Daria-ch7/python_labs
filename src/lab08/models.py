from dataclasses import dataclass, asdict 
from datetime import date
from typing import ClassVar
import re

@dataclass 
class Student:
    correct_data: ClassVar[str] = r'^(19|20)[0-9]{2}-(1[0-2]|0[1-9])-(0[1-9]|[12][0-9]{1}|3[01])$'
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        self._validate_birthdate()
        self._validate_gpa()

    def _validate_birthdate(self):
        if not re.match (self.correct_data, self.birthdate):
            raise ValueError("неверный формат даты")
        
    def _validate_gpa(self):
        if not (0 <= self.gpa <= 5):
            raise ValueError("GPA должен быть от 0 до 5")
    
    def count_age(self):
        "вычисляем возраст студента на текущую дату"
        year, month, day = map(int, self.birthdate.split('-'))
        birth_date=date(year, month, day) 
        today=date.today() 
        age = today.year - birth_date.year

        birthday_this_year = date(today.year, birth_date.month, birth_date.day)

        if today < birthday_this_year:
            age -= 1
        return age
    
    def to_dict(self):
        "преобразуем объект Student в словарь"
        return asdict(self)
    
    @classmethod 
    def from_dict(cls, data: dict):
        "создаём объект Student из словаря"

        fio=data['fio']
        birthdate=data['birthdate']
        group=data['group']
        gpa=data['gpa']

        return cls(fio,birthdate,group,gpa)
    
    def __str__(self):
        "строковое представление студента"
        fio=self.fio 
        birthdate=self.birthdate
        age=self.count_age()
        group=self.group
        gpa=self.gpa
        return (f"{fio} {birthdate} {age} {group} {gpa}")
    

