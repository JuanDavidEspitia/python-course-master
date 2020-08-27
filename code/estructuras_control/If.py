# Sentencia de desicion If

# Ejemplo Base
if True:
    print("****En caso de que sea verdadero****")

# Ejemplo de solo If
numero = int(input("Escriba un número positivo: "))
if numero < 0:
    print("¡Le he dicho que escriba un número positivo!")
print(f"Ha escrito el número {numero}")

# Ejemplo de If - Else
edad = int(input("¿Cuántos años tiene? "))
if edad < 18:
    print("Es usted menor de edad")
else:
    print("Es usted mayor de edad")
print("¡Hasta la próxima!")

# Ejemplo de Elif
edad = int(input("¿Cuántos años tiene? "))
if edad >= 18:
    print("Es usted mayor de edad")
elif edad < 0:
    print("No se puede tener una edad negativa")
else:
    print("Es usted menor de edad")

# Ejemplo IF con mas condiciones - Elif
numero = int(input("Escriba un número: "))
if numero % 2 == 0 and numero % 4 != 0:
    print(f"{numero} es múltiplo de dos")
elif numero % 4 == 0:
    print(f"{numero} es múltiplo de cuatro y de dos")
else:
    print(f"{numero} no es múltiplo de dos")

# Ejemplo 5
numero = int(input("Escriba un número: "))
if numero >= 0:
    print("Ha escrito un número positivo")
elif numero < 0:
    print("Ha escrito un número negativo")

# Ejemplo 6
Comprador_Dinero = 100
if (Comprador_Dinero >= 25):
    print ("Has comprado un libro")
    Comprador_Dinero = Comprador_Dinero - 25
    print (("Tu saldo es"), (Comprador_Dinero))
else:
    print ("Usted no tiene dinero suficiente. Seguridad!!")

# ejemplo 7
x = int(input("Dame un número: "))
if x < 0:
    x = 0
    print('Negativo... convertido en cero')
elif x == 0:
    print('Cero')
elif x == 1:
    print('Uno')
else:
    print('Otro')










