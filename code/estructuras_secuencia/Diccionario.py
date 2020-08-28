# Diccionarios
# Un Diccionario es una estructura de datos y un tipo de dato en Python con características
# especiales que nos permite almacenar cualquier tipo de valor como enteros, cadenas,
# listas e incluso otras funciones. Estos diccionarios nos permiten además identificar
# cada elemento por una clave (Key).

dicc = {'Juan': '24',
               'David': '21',
               'Camila': '20',
               'Laura': '27'}
# Con esta funcion verificamos que tipode coleccion tenemos
print(type(dicc))

diccionario = {'nombre' : 'Carlos', 'edad' : 22, 'cursos': ['Python','Django','JavaScript'] }

# Es clave valor
# Para tener el valor de clave es con el siguiente
print(dicc['Camila'])

# modificar el valor de la clave
dicc['Laura'] = '30'
print(dicc)

# Eliminamos un elemento del diccionario
del(dicc['David'])
print(dicc)

# Defino la varible 'futbolistas' como un diccionario. No es necesario declarar que tipo de dato es
futbolistas = dict()

futbolistas = {
    1 : "Casillas", 15 : "Ramos",
    3 : "Pique", 5 : "Puyol",
    11 : "Capdevila", 14 : "Xabi Alonso",
    16 : "Busquets", 8 : "Xavi Hernandez",
    18 : "Pedrito", 6 : "Iniesta",
    7 : "Villa"
}
# Recorrer un diccionario, imprimiendo su clave-valor
for k,v in futbolistas.items():
    print("%s -> %s" %(k,v))

# Declaración de un diccionario
diccionario = dict()

# Devuelve el numero de elementos que tiene el diccionario
len(dict)

# Compara el número de elementos distintos que tienen los dos
cmp (dict1,dict2)

# Devuelve una lista con las claves del diccionario
dict.keys()

# Devuelve una lista con los valores del diccionario
dict.values()

# Devuelve el valor del elemento con clave key. Sino devuelve default
dict.get(key, default=None)

# Inserta un elemento en el diccionario clave:valor. Si la clave existe no lo inserta
dict.setdefault(key, default=None)

# Insertamos un elemento en el diccionario con su clave:valor
dict['key'] = 'value'

# Eliminamos el elemento del diccionario con clave key
dict.pop('key',None)

# Devuleve la copia de un diccionario dict2 = dict.copy()
dict.copy()

# Elimina todos los elementos de un diccionario
dict.clear()

# Crea un nuevo diccionario poniendo como claves las que hay en la lista y los valores por defecto si se les pasa
dict.fromkeys(list, defaultValue)

# Devuelve true si existe la clave. Sino devuelve false
dict.has_key(key)

# devuelve un lista de tuplas formadas por los pares clave:valor
dict.items()

# Añade los elementos de un diccionario a otro
dict.update(dict2)



