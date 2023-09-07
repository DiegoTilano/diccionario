#Nombre Estudiante Sibaja Tilano Diego Andrés

# Crear un diccionario vacío
mi_diccionario = {}

while True:
    print("\nOpciones:")
    print("1. Agregar elemento")
    print("2. Eliminar elemento")
    print("3. Actualizar elemento")
    print("4. Consultar elemento")
    print("5. Salir")
    
    opcion = input("Selecciona una opción (1/2/3/4/5): ")

    if opcion == '1':
        clave = input("Ingresa la clave: ")
        valor = input("Ingresa el valor: ")
        mi_diccionario[clave] = valor
        print(f"Elemento '{clave}' agregado al diccionario.")

    elif opcion == '2':
        clave = input("Ingresa la clave del elemento a eliminar: ")
        if clave in mi_diccionario:
            del mi_diccionario[clave]
            print(f"Elemento '{clave}' eliminado del diccionario.")
        else:
            print(f"La clave '{clave}' no existe en el diccionario.")

    elif opcion == '3':
        clave = input("Ingresa la clave del elemento a actualizar: ")
        if clave in mi_diccionario:
            valor = input("Ingresa el nuevo valor: ")
            mi_diccionario[clave] = valor
            print(f"Elemento '{clave}' actualizado en el diccionario.")
        else:
            print(f"La clave '{clave}' no existe en el diccionario.")

    elif opcion == '4':
        clave = input("Ingresa la clave del elemento a consultar: ")
        if clave in mi_diccionario:
            valor = mi_diccionario[clave]
            print(f"El valor de '{clave}' es '{valor}'.")
        else:
            print(f"La clave '{clave}' no existe en el diccionario.")

    elif opcion == '5':
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida. Por favor, selecciona una opción válida (1/2/3/4/5).")
