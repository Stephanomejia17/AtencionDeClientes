class EmptyQueue (Exception):
    def __init__(self, message):
        self.message = message


class UserNotFound(Exception):
    def __init__(self, message):
        self.message = message


class Person:
    def __init__(self, name, age, descrip, plevel) -> None:
        self.name: str = name
        self.age: int = age
        self.descrip: str = descrip
        self.plevel: int = plevel

    def __str__(self) -> str:
        return f"Nombre: {self.name}, edad: {self.age}, descripcion: {self.descrip}, nivel de prioridad: {self.plevel}"

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getDescrip(self):
        return self.descrip

    def getPlevel(self):
        return self.plevel

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def setDescrip(self, descrip):
        self.descrip = descrip

    def setPlevel(self, plevel):
        self.plevel = plevel


class Node:
    def __init__(self, value = None, next = None) -> None:
        self.value = value
        self.next = next

    def getNext(self):
        return self.next

    def getValue(self):
        return self.value

    def setNext(self, next):
        self.next = next

    def setValue(self, value):
        self.value = value


class DNode:
    def __init__(self, value=None, next=None, prev=None) -> None:
        self.value = value
        self.next: Node = next
        self.prev: Node = prev

    def __str__(self) -> str:
        return f"{self.value}"

    def getNext(self):
        return self.next

    def getValue(self):
        return self.value

    def setNext(self, next):
        self.next = next

    def setValue(self, value):
        self.value = value


class DLinkedList:
    def __init__(self) -> None:
        self.head: DNode = None
        self.tail: DNode = None
        self.size = 0

    def append(self, node, e):  # Agregar nodos al final de la lista
        if self.head is None:
            self.head = DNode(e)
            self.tail = self.head
            self.size += 1
            return
        if node.next is None:
            new_node = DNode(e)
            node.next = new_node
            self.tail = new_node
            self.tail.prev = node
            self.size += 1
            return
        self.append(node.next, e)

    def preppend(self, e):  # Añadir nodos al comienzo
        new_node = DNode(e)
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def delete_at_index(self, index):  # Eliminar nodos en un indice dado
        return_Node = DNode()
        if index > self.size - 1:
            return
        if index == 0:
            return_Node = self.head
            self.head = self.head.next
            self.head.prev = None
            return return_Node

        elif index > 0:
            pos = 0
            node = self.head
            if index == self.size - 1:
                return_Node = self.tail
                self.tail = self.tail.prev
                self.tail.next.prev = None
                self.tail.next = None
                return return_Node
            else:
                while pos != index - 1:
                    node = node.next
                    pos += 1
                return_Node = node
                aux_node = node.next.next
                aux_node.prev = node
                node.next.next = None
                node.next.prev = None
                node.next = aux_node
                return return_Node

    def getSize(self):
        return self.size


def traverse(node):  # Imprimir la lista
    cont = 1
    while node is not None:
        print(f"{cont}. ", node.getValue())
        node = node.getNext()
        cont += 1


class PriorityQueue:
    def __init__(self) -> None:
        self.queue: DLinkedList = DLinkedList()
        self.backupQueue: DLinkedList = DLinkedList()

    def __str__(self) -> str:
        return f"{traverse(self.queue.head)}"

    def enqueue(self, persona: Person):
        self.queue.append(self.queue.head, persona)
        if self.queue.getSize() != 1:
            self.ordenar()

    def dequeue(self):
        try:
            if self.queue.getSize() == 1:
                auxtail = self.queue.tail
                self.queue.tail = None
                self.queue.head = None
                self.queue.size -= 1
                return auxtail
            else:
                auxtail = self.queue.tail
                auxprevtail = self.queue.tail.prev
                self.queue.tail.prev.next = None
                self.queue.tail.prev = None
                self.queue.tail = auxprevtail
                self.queue.size -= 1
                return auxtail
        except Exception:
            raise EmptyQueue("No hay elementos en la cola")

    def first(self):
        return self.queue.tail

    def updatePriority(self, paciente: int, new_priority: int):
        index_queue = self.queue.head
        self.backupQueue.head = self.queue.head
        self.backupQueue.tail = self.queue.tail
        if paciente > self.queue.getSize():
            print("El valor ingresado sobrepasa el numero de pacientes...")
        else:
            for i in range(paciente):
                index_queue = index_queue.next

            if index_queue == self.queue.head:
                index_queue.next.prev = None
                self.backupQueue.head = index_queue.next
                index_queue.next = None
            elif index_queue == self.queue.tail:
                index_queue.prev.next = None
                self.backupQueue.tail = index_queue.prev
                index_queue.prev = None
            else:
                index_queue.next.prev = index_queue.prev
                index_queue.prev.next = index_queue.next
                index_queue.prev = None
                index_queue.next = None

            self.queue.head = self.backupQueue.head
            self.queue.tail = self.backupQueue.tail
            index_queue.value.setPlevel(new_priority)
            self.enqueue(index_queue.value)


    def ordenar(self):
        self.backupQueue.head = self.queue.head
        self.backupQueue.tail = self.queue.tail
        index_queue = self.queue.head
        contador = 1
        while (self.queue.getSize()-1) >= contador:
            if self.backupQueue.tail.value.plevel < index_queue.value.plevel:
                index_queue = index_queue.next
            elif self.backupQueue.tail.value.plevel > index_queue.value.plevel:
                if index_queue.prev is not None:
                    auxindexprev = index_queue.prev
                    auxprevtail = self.backupQueue.tail.prev
                    index_queue.prev.next = self.backupQueue.tail
                    self.backupQueue.tail.prev = index_queue.prev
                    self.backupQueue.tail.next = index_queue
                    index_queue.prev = self.backupQueue.tail
                    self.backupQueue.tail = auxprevtail
                    self.backupQueue.tail.next = None
                    break

                else:
                    self.backupQueue.tail = self.backupQueue.tail.prev
                    self.backupQueue.tail.next.prev = None
                    self.backupQueue.tail.next.next = index_queue
                    self.backupQueue.tail.next.next.prev = self.backupQueue.tail.next
                    self.backupQueue.head = self.backupQueue.tail.next
                    self.backupQueue.tail.next = None
                    break
            else:
                if index_queue.prev is not None:
                    aux_tail = self.backupQueue.tail
                    self.backupQueue.tail = aux_tail.prev
                    self.backupQueue.tail.next = None
                    aux_tail.prev = None
                    index_queue.prev.next = aux_tail
                    aux_tail.prev = index_queue.prev
                    index_queue.prev = aux_tail
                    aux_tail.next = index_queue


                    break
                else:
                    self.backupQueue.tail = self.backupQueue.tail.prev
                    self.backupQueue.tail.next.prev = None
                    self.backupQueue.tail.next.next = index_queue
                    self.backupQueue.tail.next.next.prev = self.backupQueue.tail.next
                    self.backupQueue.head = self.backupQueue.tail.next
                    self.backupQueue.tail.next = None
                    break

            contador += 1
        self.queue.head = self.backupQueue.head
        self.queue.tail = self.backupQueue.tail


# Pruebas
"""pq = PriorityQueue()
p1 = Person("Deyson", 18, "Dolor de muela", 4)
p2 = Person("Nathy", 19, "Dolor de cabeza", 5)
p3 = Person("Tepho", 20, "Dolor de cabeza", 2)
p4 = Person("Juli", 20, "Dolor de muela", 1)
p5 = Person("Sofi", 19, "Dolor de cabeza", 1)
p6 = Person("Edison", 18, "Dolor de cabeza", 6)
p7 = Person("JJ", 18, "Dolor de cabeza", 6)


pq.enqueue(p1)
pq.enqueue(p2)
pq.enqueue(p3)
pq.enqueue(p4)
pq.enqueue(p5)
pq.enqueue(p6)
pq.enqueue(p7)
print(pq)

pq.updatePriority(0, 1)
traverse(pq.queue.head)"""
