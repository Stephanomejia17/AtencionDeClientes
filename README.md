# Atención de Clientes
## Listas enlazadas - 2024-1
El objetivo de esta práctica es diseñar e implementar una cola de prioridad utilizando exclusivamente listas enlazadas para gestionar la atención de pacientes en el departamento de urgencias de un hospital. Esta estructura de datos debe permitir insertar y atender a los pacientes de acuerdo con su nivel de prioridad, asegurando que aquellos en condiciones más críticas sean atendidos primero.

*Descripción del Problema*:
El departamento de urgencias de un hospital recibe pacientes que requieren atención inmediata. Cada paciente es evaluado al ingresar, asignándosele un nivel de prioridad basado en la gravedad de su condición. Es crucial que el sistema de gestión de pacientes pueda organizarlos de manera eficiente para asegurar que los casos más críticos reciban atención prioritaria.

*Requisitos de la Implementación*:
Estructura de Datos del Paciente: Cada paciente debe ser representado como un objeto de tipo Paciente y guardarse en un nodo en la lista enlazada, conteniendo la siguiente información:

* Nombre del paciente.
* Edad.
* Descripción breve de su condición.
* Nivel de prioridad (un entero donde 1 representa la máxima prioridad y valores mayores indican menor prioridad).
*Cola de Prioridad*: Implementar la cola de prioridad utilizando listas enlazadas. Esta estructura debe soportar, al menos, las siguientes operaciones:

* *Inserción*: Agregar un nuevo paciente a la cola basándose en su nivel de prioridad. Los pacientes con igual prioridad se atienden por orden de llegada.
* *Atención*: Extraer y devolver los datos del paciente con mayor prioridad (es decir, el paciente que debe ser atendido a continuación).
* *Sin Uso de Estructuras de Datos Auxiliares*: Está estrictamente prohibido el uso de arrays, listas dinámicas predefinidas (como las listas de Python o ArrayList de Java), pilas, colas, o cualquier otra estructura de datos auxiliar predefinida. Toda la gestión de la cola de prioridad debe realizarse exclusivamente mediante operaciones con listas enlazadas implementadas por el alumno.

*Métodos Adicionales*: Para mejorar la funcionalidad de la cola de prioridad, se pueden implementar métodos adicionales como:

* *MostrarCola*: Mostrar la lista completa de pacientes en la cola, incluyendo su nombre, condición y nivel de prioridad.
* *ActualizarPrioridad*: Cambiar el nivel de prioridad de un paciente existente en la cola.
