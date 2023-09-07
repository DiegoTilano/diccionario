# Inicializamos una lista vacía para almacenar elementos
mi_lista = []

# Función para agregar un elemento a la lista
def agregar_lista():
    elemento = input("Ingresa un elemento: ")
    mi_lista.append(elemento)
    print(f"{elemento} ha sido agregado a la lista.")

# Función para consultar elementos de la lista
def consultar_elementos():
    if not mi_lista:
        print("La lista está vacía.")
    else:
        print("Elementos en la lista:")
        for i, elemento in enumerate(mi_lista, 1):
            print(f"{i}. {elemento}")

# Función para actualizar un elemento de la lista
def actualizar_lista():
    consultar_elementos()
    if not mi_lista:
        return
    indice = int(input("Ingresa el número del elemento que deseas actualizar: ")) - 1
    if 0 <= indice < len(mi_lista):
        nuevo_valor = input("Ingresa el nuevo valor: ")
        mi_lista[indice] = nuevo_valor
        print("Elemento actualizado con éxito.")
    else:
        print("Índice inválido.")

# Función para eliminar un elemento de la lista
def eliminar_lista():
    consultar_elementos()
    if not mi_lista:
        return
    indice = int(input("Ingresa el número del elemento que deseas eliminar: ")) - 1
    if 0 <= indice < len(mi_lista):
        elemento_eliminado = mi_lista.pop(indice)
        print(f"{elemento_eliminado} ha sido eliminado de la lista.")
    else:
        print("Índice inválido.")

# Loop principal del programa
while True:
    print("\nOpciones:")
    print("1. Agregar elemento A La lista")
    print("2. Consultar La Lista")
    print("3. Actualizar La Lista")
    print("4. Eliminar De La Lista")
    print("5. Salir")
    
    opcion = input("Selecciona una opción (1/2/3/4/5): ")
    
    if opcion == "1":
        agregar_lista()
    elif opcion == "2":
        consultar_elementos()
    elif opcion == "3":
        actualizar_lista()
    elif opcion == "4":
        eliminar_lista()
    elif opcion == "5":
        print("¡Adiós!")
        break
    else:
        print("Opción no válida. Por favor, elige una opción válida (1/2/3/4/5).")
