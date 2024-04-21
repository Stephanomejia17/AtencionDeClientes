import sys
import time
from typing import Optional

from classes.classes import Person, traverse
from classes.classes import PriorityQueue


class Console:
    GUION = "-"

    def __init__(self):
        self.priorityQueue = PriorityQueue()
        self.opcion: Optional[int] = None

    def menu(self) -> None:
        while True:
            print(self.GUION * 40, "\n")
            print("BIENVENIDO AL SISTEMA DE ATENCIÓN DE CLIENTES\n")
            print(self.GUION * 40, "\n")
            print("Digite el número según su necesidad: ")
            print("1. Ingresar un nuevo paciente a la cola")
            print("2. Atender a un paciente de la cola")
            print("3. Consultar el proximo paciente que será atendido(a)")
            print("4. Actualizar la prioridad de un paciente")
            print("5. Mostrar todos los pacientes en la cola")
            print("6. Salir")
            print(self.GUION * 40, "\n")
            self.opcion = int(input("Ingrese su opción: "))
            if self.opcion == 6:
                sys.exit()
            elif self.opcion == 1:
                print(self.GUION * 40, "\n")
                print("INGRESO DE DATOS DE PACIENTE: ")
                print(self.GUION * 40, "\n")
                name = input("Nombre del paciente: ")
                age = input("Edad del paciente: ")
                descrip = input("Descripción de malestar: ")
                plevel = int(input("Nivel de prioridad: "))
                persona = Person(name, age, descrip, plevel)
                self.priorityQueue.enqueue(persona)
                print("Subiendo datos al sistema...")
                time.sleep(2)
                print("Datos subidos con exito!")
            elif self.opcion == 2:
                print("Atendiendo paciente...")
                time.sleep(1)
                print("El paciente ", (self.priorityQueue.dequeue()).value.name, " fue atendido con exito")

            elif self.opcion == 3:
                print("El próximo paciente que será atendido es: ", self.priorityQueue.first())
            elif self.opcion == 4:
                if self.priorityQueue.queue.getSize() != 0:
                    traverse(self.priorityQueue.queue.head)
                    paciente = int(input("Ingrese el numero de paciente: "))
                    new_priority = int(input("Ingrese la nueva prioridad del paciente: "))
                    self.priorityQueue.updatePriority(paciente, new_priority)
                    print("Actualizando... Listo!")
                else:
                    print("No hay pacientes")
            elif self.opcion == 5:
                traverse(self.priorityQueue.queue.head)
            else:
                print("Ingrese una nueva opción...")
            time.sleep(3)
            self.opcion = None



    def run(self):
        self.menu()


