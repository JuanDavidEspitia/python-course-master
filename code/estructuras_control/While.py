# Bucles o iteradores
# Mientras se cumpla una condicion ejecuta el codigo interno
# Sintaxis
# while condicion:
#     cuerpo del bucle


# Ejemplo Base
iterador = 1
while iterador <= 3:
    print("El valor del iterador es: ", iterador)
    iterador += 1
print("Programa terminado")

# Ejemplo # 2
numero = int(input("Escriba un número positivo: "))
while numero < 0:
    print("¡Ha escrito un número negativo! Inténtelo de nuevo")
    numero = int(input("Escriba un número positivo: "))
print("Gracias por su colaboración")

# ejemplo 3
i = 0
while i <= 3:
    i += 1
    print("Estoy iterando, van = ", i)
    break
else:
    print("Imprimo esto por que se termino y es el else")


# ejemplo 5
while True:  # Creamos el ciclo infinito
    opcion = (input("""Elige una fruta para tu desayuno: 
    1- Manzanas
    2- Bananas
    3- Nada
    """))  # Creamos un input para
    # que el usuario ingrese su opción y la almacenamos en "opcion"

    ############################################-2-##################################################
    if opcion == '1':  # Condicionales según la opción que eligió!
        print("Has seleccionado manzanas")

    elif opcion == '2':
        print("Has seleccionado bananas")

    elif opcion == '3':
        print("Has seleccionado nada")

    else:
        print("Debes seleccionar una opcion (1, 2 o 3)")










