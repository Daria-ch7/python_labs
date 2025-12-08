from src.lab10.structures import Stack, Queue

def stack_example():
    """Пример работы со стеком"""
    print("Пример работы со стеком")

    stack=Stack()

    print("Добавление элемента в стек:")
    for i in range(1,5):
        stack.push(i)
        print(stack)

    print(f"Количество эл-ов в стеке: {stack.__len__()}")

    print(f"\nВерхний элемент (peek): {stack.peek()}")

    print("\nИзвлекаем элементы со стека:")
    while not stack.is_empty():
        item = stack.pop()
        print(f"извлечено: '{item}', осталось: {stack}")
    print(f"\nСтек пуст: {stack.is_empty()}")

def queue_example():
    """Пример работы с очередью"""
    print("Пример работы с очередью")

    queue = Queue()

    print("Добавляем элементы в очередь:")
    for i in range(1,5):
        queue.enqueue(i)
        print(queue)
    print(f"\nПервый элемент (peek): {queue.peek()}")

    print("\nОбрабатываем элементы из очереди:")
    while not queue.is_empty():
        task = queue.dequeue()
        print(f" взяли: '{task}', осталось: {queue}")
    
    print(f"\nОчередь пуста: {queue.is_empty()}")

if __name__ == "__main__":
    stack_example()
    queue_example()