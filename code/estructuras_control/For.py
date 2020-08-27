# Ciclos For
# Sintaxis
# for variable in elemento_iterable:
#     cuerpo de la repetición

# ejemplo 1
for vuelta in range(1,10):
    print("Vuelta "+str(vuelta))

print("Ejemplo de iteracion de una lista")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] #Creamos la lista con números
# Numeros pares
for num in numeros: #En la variable "num" almacenamos los ítem de la lista
    if num % 2 == 0: #Condición: Si el resto de la división por dos es cero entonces:
        print (num) # Imprimimos la variable num

# Para numeros primos
print(" ********  numeros primos  *******")
for num in numeros: #En la variable "num" almacenamos los ítem de la lista
    if num % 2 != 0: #Condición: Si el resto de la división por dos es cero entonces:
        print (num) # Imprimimos la variable num

# Creamos uns ciclo For para calcular el tamaño de caracteres por cada elemento
Palabras = ['Peine', 'Pelo', 'Ventana', 'Refrigerador', 'Adolescente', 'Dentista', 'Asesino'] #Lista de palabras
for caracteres in Palabras: #Creamos el bucle para iterar Palabras y almacenar en caracteres
    print ((caracteres), ('| Longitud:'), (len(caracteres)))
#Aquí imprimimos la variable caracteres
# y luego la cadena " | Longitud:" y seguido utilizando la
#Función predefinida "Len()" la longitud de cada palabra


# Iterar diccionarios
print(" **********  Recorremos un Diccionario  ********* ")
Agenda = {
'Marcelo' : '3443456993',
'Gaston' : '3443456992',
'Lucas' : '3443456991',
'Angela' : '3443456990',
'Lucio' : '3443456989'
} #Aqui hemos creado nuestra agenda como un diccionario
#Ahora creamos el bucle definiendo las variables k y v
#para Key y Value (clave y valor)
for (k, v) in Agenda.items():
    print(k, v)
#Utilizamos el método .items() en python 3 para evitar errores.
#Imprimimos el resultado de las variables

# Iterar cadena string
print("************ Iterar cadena string *************")
entrada = "hola estoy programando en python"  # Cadena de texto a analizar
contador = 0
cuentalaletra = 'a'  # Almacenamos en la variable la letra que queremos contar
for letra in entrada:  # Almacenamos en letra cada ítem de la cadena
    if letra == cuentalaletra:  # Si el ítem es igual a la letra a contar
        contador = contador + 1  # Sumamos uno al contador

print((cuentalaletra), (':'), (contador))  # Imprimimos la letra a contar
# y el número del contador