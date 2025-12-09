# from src.lab10.structures import Stack, Queue
from src.lab10.linked_list import SinglyLinkedList
# def stack_example():
#     """Пример работы со стеком"""
#     print("Пример работы со стеком")

#     stack=Stack()

#     print("Добавление элемента в стек:")
#     for i in range(1,5):
#         stack.push(i)
#         print(stack)

#     print(f"Количество эл-ов в стеке: {stack.__len__()}")

#     print(f"\nВерхний элемент (peek): {stack.peek()}")

#     print("\nИзвлекаем элементы со стека:")
#     while not stack.is_empty():
#         item = stack.pop()
#         print(f"извлечено: '{item}', осталось: {stack}")
#     print(f"\nСтек пуст: {stack.is_empty()}")

# def queue_example():
#     """Пример работы с очередью"""
#     print("Пример работы с очередью")

#     queue = Queue()

#     print("Добавляем элементы в очередь:")
#     for i in range(1,5):
#         queue.enqueue(i)
#         print(queue)
#     print(f"\nПервый элемент (peek): {queue.peek()}")

#     print("\nОбрабатываем элементы из очереди:")
#     while not queue.is_empty():
#         task = queue.dequeue()
#         print(f" взяли: '{task}', осталось: {queue}")
    
#     print(f"\nОчередь пуста: {queue.is_empty()}")

# if __name__ == "__main__":
#     stack_example()
#     queue_example()

def simple_example():
    print("ПРИМЕР ИСПОЛЬЗОВАНИЯ SINGLYLINKEDLIST")

    lst = SinglyLinkedList()

    print("1. Добавляем элементы:")
    lst.append("пенал")
    lst.append("карандаш")
    lst.append("ручка")
    print(f"   Список: {lst}")


    print("\n2. Добавляем 'рюкзак' в начало:")
    lst.prepend("рюкзак")
    print(f"   Список: {lst}")

    print("\n3. Вставляем 'тетрадь' после первого элемента:")
    lst.insert(2, "тетрадь")
    print(f"   Список: {lst}")

    print("\n4. Итерируемся по списку:")
    for item in lst:
        print(f"   - {item}")
    
    print("\n5. Удаляем 'тетрадь':")
    if lst.remove("тетрадь"):
        print(f"   Удалили. Теперь список: {lst}")
    
    print(f"\n6. Список элементов:")
    for i in lst:
        print(f" - {i}")

    print(f"\n7. Размер списка: {len(lst)} элементов")

    print(f"\n8. Строковое представление: {str(lst)}")

if __name__ == "__main__":
    simple_example()