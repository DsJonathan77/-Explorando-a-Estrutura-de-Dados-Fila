class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            print("Fila vazia. Nada para remover.")
            return None
        removed = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return removed

    def peek(self):
        if self.is_empty():
            print("Fila vazia.")
            return None
        return self.front.data

    def display_queue(self):
        if self.is_empty():
            print("Fila vazia.")
            return
        current = self.front
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
