# listas de numeros
"""
las listas tambienm pueden almacenar numeros. python
ofrece varias herramientas que ayudan a trabajar 
eficientemente con listas de numeros.
"""
# metodo build-in range()
"""
el metodo range() nos ayuda a creaar eficientemente 
series de numeros.

ejmplo 
"""

for value in range(1,5):
    print(value)

# crea una lista de numeros utilizando rangue 
numbers = list(range(1,6))
print(numbers)

# lista de numeros pares 
even_numbers = list(range(0,11,2))
# que pasa con un paso negativo?
print(even_numbers)