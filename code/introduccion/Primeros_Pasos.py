# Primer contacto con Python
# Lenguje no fuertemente tipado
print("Hola, PyCharm Python")
a = 5
b= 5
b = b *5
r = a + b
print(r)

# Cadenas de caracteres
'Juan David Espitia'
"Juan David Espitia"
print('Comillas simples')
print("Comillas dobles")
print('Juan David "Espitia"')
print('Imprime con salto de linea \n nueva linea')
print('Imprime con tabulador --> \t tabular')
# Unidad logica o ruta del SO
print('C:\ruta\logica') # NO funciona
# Colocando la r adelante establecemos que es una ruta
print(r'C:\ruta\logica')

# Cadenas de caracteres con variables, operaciones y arrays

print(""" De esta manera
  se ahorra el salto de linea
  cuando se presiona enter para una nueva linea """)

# ASignacion de variables
variable = 'Cadena de caracteres'
print(variable)

# Concatenamos mas caracteres a una variables string
variable1 = variable + "  Nuevos caracteres "
print(variable1)
print("Fusionar dos variables de caracteres " + variable1 + variable)

# Indices de caracteres
alumno = "Juan David Espitia"
print("Obtenemos la primera letra: " + alumno[0])
print("Obtenemos la letra D: " + alumno[5])
print("Obtenemos la letra E: " + alumno[11])
print("Obtenemos la ultima letra: " + alumno[-1])

# Obtenemos un rango de caracteres
print("Obtenemos las letras: " + alumno[0:7])
print("Obtenemos las letras: " + alumno[5:10])
print("Obtenemos las letras: " + alumno[:7])
print("Obtenemos las letras: " + alumno[5:])

# Para obtner la cantida de caracteres de la cadena
print(len(alumno))

# Listas

lista = [1,2,3,4,5,6,7,8,9,10]
print(lista)

# Puede tener todo tipo de datos
lista2 = [1,4,'Juan', 'C', 785, 962, 'Camila', 'Laura', 87, 4, 5, 8, 9]
print(lista2)
print(lista2[0])
print(lista2[0:7])
print(lista2[5:])
print(lista2[:4])
print(lista2[-1])

# Podemos concatenar listas
listaConcat = lista + lista2
print(listaConcat)

# Podemos añadir elementos a la lista
numero = [1,2,3,4,5]
numero.append(10)
print(numero)
numero.append(10+2)
print(numero)

# Podemos modificar las listas
abecedario = ['a','b','c','d','e']
print(abecedario)
abecedario[2] = 'F'
print(abecedario)
abecedario[:2] = ['A','B'] # No toma el valor final (2)
print(abecedario)

# Listas anidadas
primero = [1,2,3]
segundo = [4,5,6]
tercero = [7,8,9]
anidad = [primero,segundo,tercero]
print(anidad)
print(anidad[0])

# Ingresamo datos por consola
input()
dato = input() # Se guarda en string
print(dato)

dato2 = float(input("Intruduce un valor decimal: "))
print(dato2)

dato3 = float(input("Intruduce un valor entero: "))
print(dato3)

