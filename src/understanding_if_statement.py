# if Statement
cars = ["audi", 'bmw', "subaru", 'toyota']
for car in cars:
    if car == 'audi':
        print(car.upper())
    else:
        print(car)


# El condicional o condition
# El condicional es el corazon del if

# Condicional Verdadero
# Condicional True
truck = "ford"
print(truck == 'ford')

# Condicional Falso
# Conditional False
print(truck == 'audi')

#
print(truck == 'Ford'.lower())


# Condicional de desigualdad !=
print(truck!="audi") # True
print(truck!="ford") # False


# Comparaciones numericas 
print("Comparaciones numericas")
age = 34
print(age==34) # True

answer = 17
if answer != 42:
    print("Esa no es la respuesta correcta")

# Conector menor que <
print("conectores < > <= >=")
age = 19
print(age < 21) # True
print(age <= 21) # True
print(age > 21) # False
print(age >= 21) # False

# multiple condition
age_