from collections import deque
from typing import Any

class Stack:
    """Структура данных "Стек" (LIFO - Last In, First Out)
    Реализация на базе списка (list)"""
    def __init__(self):
        """создание и настройка (инициализация) пустого стека"""
        self._data: list[Any] = []
        
    def push(self, item: Any):
        """Добавить элемент на вершину стека (ничего не возвращает)
        подаем: item: элемент для добавления"""
        self._data.append(item)

    def is_empty(self):
        """Проверить, пуст ли стек
        возвратить: True если стек пуст, иначе False"""
        return len(self._data)==0

    def pop(self):
        """Cнять верхний элемент стека и вернуть его
        oшибка, если стек пуст"""
        if self.is_empty():
            raise IndexError("Невозможно извлечь элемент: стек пуст")
        return self._data.pop()
    
    def peek(self):
        """Посмотреть верхний элемент без удаления
        возвратить: верхний элемент стека или None, если стек пуст"""
        if self.is_empty():
            return None
        return self._data[-1]
    
    def __len__(self):
        """Возвращает количество элементов в стеке"""
        return len(self._data)
    
    def __str__(self):
        """Строковое представление стека, возвращает строку"""
        return f"Stack({self._data})"
    
    def __repr__(self) -> str:
        """Техническое представление для отладки"""
        return f"Stack({self._data})"
    

class Queue:
    """Структура данных "Очередь" (FIFO - First In, First Out)
    Реализация на базе collections.deque"""
    def __init__(self):
        """Инициализация пустой очереди"""
        self._data: deque[Any] = deque()
    def enqueue(self, item: Any):
        """Добавить элемент в конец очереди
        подаем: item (элемент для добавления)"""
        self._data.append(item)
    def is_empty(self):
        """Проверить, пуста ли очередь
        возвращает: True если очередь пуста, иначе False"""
        return len(self._data) == 0
    def dequeue(self):
        """Взять элемент из начала очереди и вернуть его
        возвращаем: первый жлемент очереди
        ошибка: если пустая очередь"""
        if self.is_empty():
            raise IndexError("Невозможно извлечь элемент: очередь пуста")
        return self._data.popleft()
    def peek(self):
        """Посмотреть первый элемент без удаления
        возвращает: первый элемент в очереди или None, если очередь пуста"""
        if self.is_empty():
            return None
        return self._data[0]
    def __len__(self):
        """Количество элементов в очереди"""
        return len(self._data)
    def __str__(self) -> str:
        """Строковое представление очереди, возвращает строку"""
        return f"Queue({list(self._data)})"
    
    def __repr__(self) -> str:
        """Представление для отладки"""
        return f"Queue({list(self._data)})"