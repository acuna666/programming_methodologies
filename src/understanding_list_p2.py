#Agregando elementos a una lista
motorcycles = ['honda', 'mortalica', 'yamaha']
print(motorcycles) # ['honda', 'mortalica', 'yamaha']

# Metodo append () agrega un elemto al final de la lista
motorcycles.append('kawasaki')
print(motorcycles) 

























## metodo .pop() Elimina el ultimo elemnto de una lista,
# pero nos permite utilizar el elemento despues de eliminarlo
motorcycles_4 = ['honda', 'zuzuki', 'hd', 'mortalica']
print(motorcycles_4)
motorcycles_4.pop()
print(motorcycles_4)
deleted_motorcycle = motorcycles_4.pop()
print(f"tu motocicleta borrada es: {deleted_motorcycle}")
print(motorcycles_4)

# se puede utilizar tambien para eliminar un  elemento espesifico.
motorcycles_5 = ['honda', 'zuzuki', 'hd', 'mortalica']
print(motorcycles_5)
motorcycles_5.pop(0)
print(motorcycles_5) # lista sin honda

# metodo .remove (), permite eliminar elemtos por su valor.
print("aqui aprendi a utlilizar el metodo remove".upper())
motorcycles_6 = ['honda', 'yamaha', 'zuzuki', 'ducati']
print(motorcycles_6)
motorcycles_6.remove("yamaha")
print(motorcycles_6)

# ordenar lista 
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort() # ordenar la lista de manera permanente 
# argumento opcional de sort (reverse = true )
print(cars)
# tarea. estudiar el metodo de las listas .reverse()

