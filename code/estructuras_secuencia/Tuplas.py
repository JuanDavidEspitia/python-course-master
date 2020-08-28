# Tuplas
# Las tuplas son inmutables
tupla = ('Juan', 'Bogota', 'Estuddiante', 26)
print(tupla)

t=(25, "Mayo", 1810)
print(t[0])

# Logitud de las tuplas
print(len(t))

valores = ("Python", True, "Zope", 'Python', 5,'Juan', 'C', 'Scala','Python')
print(valores[-1])

# Para conocer la posicion de un elemento en particular
print('esta en la posicion: ' , valores.index('Zope'))

# Cuenta cuantos valores se repiten con la palabra a buscar
print("la cantida de veces que aperece el elemento a buscar son: ",valores.count('Python'))