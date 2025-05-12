from queue import Queue

# Criando a fila
q = Queue()

# Enfileirando os primeiros elementos
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print("Fila após enfileirar 1, 2 e 3:")
q.display_queue()

# Adicionando mais elementos à fila
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
print("Fila após enfileirar 4, 5 e 6:")
q.display_queue()

# Removendo dois elementos da fila
q.dequeue()
q.dequeue()
print("Fila após desenfileirar dois elementos:")
q.display_queue()

# Visualizando o primeiro elemento (peek)
primeiro = q.peek()
print("Primeiro elemento da fila (peek):", primeiro)

# Verificando se a fila está vazia
if q.is_empty():
    print("Fila está vazia")
else:
    print("Fila não está vazia")
