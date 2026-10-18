"""
las listas nos permiten almacenar informacion en un lugar,
la cantidad que desee: ya sea pocos elementos 
o millones de elementos 

una lista es una coleccion de items(elementos) que tiene
un orden particular, se puede creear listas que incluyen
strings, enteros, floats, los nombres de las personas de tu familia
etccetera, podemos almacenar (los tipos de datos
permitidos en python) lo que queremos en su lista.

son elemntos mutables: puede modificarse al tamaño de una lista

se recomienda nombrar una variable de tipo lista en plural.

en python los corchetes [] indican una lista,
sus elementos se separan por comas.

Ejemplo
"""
bicycles = ['treck', "cannondale", 'redline' 'specialized']
print(bicycles)

# como podemos acceeder a los elementos de una lista?

"""
las listas son coleccionesw ordenadas. se puede acceder
a un elemento de una lista diciendole a python la 
posicion o indice del elemento deseado.

para obtener el valor deseado, se debe escribir 
el nombre de la lista, seguido del indice del elemento
entre corchetes
"""
print(bicycles[0], bicycles[1], bicycles[2])

print(bicycles[0].upper())

# los indices comiensan en 0, no en 1
# ejemplo 
print(bicycles[1]) #cannondale
print(bicycles[3]) #specialized

#accediendo al ultimo elemneto de la lista 
print(bicycles[-1])
print(bicycles[-2])

# utilizando valores individuales de una lista 
message = f"my first bicycle was a {bicycles[0].upper()}"
print(message)
