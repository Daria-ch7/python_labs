from typing import Any

class Node:
    """Узел односвязного списка.
    Содержит значение и ссылку на следующий узел."""

    def __init__(self, value: Any):
        """Инициализация узла.
        value: значение, которое хранит узел"""
        self.value = value
        self.next: 'Node' | None = None #следующий объект либо объект класса, либо ничего

    def __str__(self) -> str:
        """Строковое представление узла"""
        return f"Node({self.value})"
    
class SinglyLinkedList:
    """Односвязный список.
    Состоит из узлов Node, связанных через next."""

    def __init__(self):
        """Инициалищация пустого списка"""
        self.head: Node | None = None #первый узел
        self.tail: Node | None = None #последний узел
        self._size = 0 #количество элементов
    
    def is_empty(self):
        """Проверяет, пуст ли список"""
        return self.head is None
    
    def append(self, value: Any):
        """Добавляет элемент в КОНЕЦ списка.
        Время: O(1) благодаря tail.
        value: значение для добавления
        ничего не возвращает"""
        new_node = Node(value)

        if self.is_empty():
            # Если список пуст, новый узел становится и head и tail
            self.head = new_node
            self.tail = new_node
        else:
            # Добавляем после tail и обновляем tail
            self.tail.next = new_node
            self.tail = new_node
        self._size +=1

    def prepend(self, value: Any):
        """ Добавляет элемент в начало списка.
        Время: O(1).
        value: значение для добавления
        ничего не возвращает"""
        new_node = Node(value)
        if self.is_empty():
            # Если список пуст, новый узел становится и head и tail
            self.head = new_node
            self.tail = new_node
        else:
            # Новый узел становится головой
            new_node.next = self.head
            self.head = new_node
        
        self._size += 1
    
    def insert(self, idx: int, value: Any):
        """Вставляет элемент по указанному индексу.
        подаём:
        idx: индекс для вставки (0 = начало, len(list) = конец)
        value: значение для вставки
        ошибка: если индекс вне диапазона [0, len(list)]"""
        
        # Проверка индекса
        if idx < 0 or idx > self._size:
            raise IndentationError(f"Индекс {idx} вне диапазона [0, {self._size}]")
        # Специальные случаи
        if idx == 0:
            self.prepend(value)
            return
        elif idx == self._size:
            self.append(value)
            return
        # Обычный случай (вставка в середину)
        new_node = Node(value)

        # Находим узел ПЕРЕД местом вставки
        pered = self.head
        for i in range(idx-1):
            pered = pered.next

        # Вставляем новый узел между pered и pered.next
        new_node.next = pered.next
        pered.next = new_node
        
        self._size += 1

    def remove(self, value: Any):
        """Удаляет ПЕРВОЕ вхождение значения из списка.
        value: значение для удаления
        возвращает: True если элемент был найден и удалён, False если не найден"""
        if self.is_empty():
            return False
        
        # Специальный случай: удаляем голову
        if self.head.value == value:
            self.head = self.head.next
            # Если список стал пустым, обнуляем tail
            if self.head is None:
                self.tail = None
            self._size -= 1
            return True
        
        # Ищем узел ПЕРЕД тем, который нужно удалить
        pered = self.head
        while pered.next is not None and pered.next.value != value:
            pered = pered.next
        
        # Если не нашли значение
        if pered.next is None:
            return False
        
        # Удаляем узел
        pered.next = pered.next.next
        
        # Если удалили последний элемент, обновляем tail
        if pered.next is None:
            self.tail = pered
        
        self._size -= 1
        return True
        
    def __iter__(self):
        """Возвращает итератор по значениям в списке."""
        pered = self.head
        while pered is not None:
            #Функция с yield генерирует по одному
            yield pered.value
            pered = pered.next
        
    def __len__(self):
        """Возвращает количество элементов в списке"""
        return self._size
    
    def __repr__(self) -> str:
        """Возвращает строковое представление."""
        values = list(self)
        return f"SinglyLinkedList({values})"
    
    def __str__(self) -> str:
        """Строковое представление для пользователя"""
        values = []
        current = self.head
        while current is not None:
            values.append(str(current.value))
            current = current.next
        return ",".join(values)




