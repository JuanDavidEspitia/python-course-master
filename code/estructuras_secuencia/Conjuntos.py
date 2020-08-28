# Conjuntos
# Colecciones desordenadas
# Comprobacion de pertenencia a un conjunto
# No permite registros duplicados
# Creando un conjunto en python
A = {1,2,3}
print(A)

# Creamos un conjunto
conjunto = {1,2,3,4,5,6}
# Agregamos un nuevo valor al conjunto
conjunto.add(7)
print(conjunto)
# al agregar un valor numerico el organiza en orden con un criterio interno
conjunto.add(0)
print(conjunto)

# Pero depende del tipo de dato que se añada
conjunto.add('D')
conjunto.add('B')
conjunto.add('Y')
# Para este caso no ordeno alfabeticamente
print(conjunto)

# Creando un conjunto a partir de una lista
lista = ["bananas", "manzanas", "naranjas", "limones"]
B = set(lista)
print(B)

# Los conjuntos eliminan los elementos duplicados
lista = ["bananas", "manzanas", "naranjas", "limones",
        "bananas", "bananas", "limones", "naranjas"]
C = set(lista)
print(C)

# Creando el conjunto vacío
O = set()
print(O)


# Cardinalidad de un conjunto con len().
A = {1,2,3}
Con = {1,4,5,7,8,96,7,8,55,64,7874,5417,7}
print("La cardinalidad del conjunto A = {0} es {1}".format(Con,len(Con)))

# Igualdad entre conjuntos. El orden de los elementos no importa.
A = {1,2,3,4}
B = {4,2,3,1}
print(A == B)

# Subconjunto. No hay distincion entre subconjunto y propio
# para el conjunto por defecto de python.
A = {1,2,3}
B = {1,2,3,4,5}
print(A.issubset(B))

# Union de conjuntos
A = {1,2,3,4,5}
B = {4,5,6,7,8,9,10}
print("La union entre dos conjuntos seria: ",A.union(B))
# Intersección de conjuntos
print("La Intersección entre dos conjuntos seria:", A.intersection(B))
# Diferencia entre conjuntos
print("La Diferencia entre dos conjuntos seria:", A - B)


