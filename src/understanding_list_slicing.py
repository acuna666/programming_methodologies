players = ["charly", "juan", "iancarlo", "lisandro"]
print("lista original", players)

#slicing 
print(players[0:2]) # ["charly", "juan"]

# el slicing nos permite trabajar con un grupo 
# especifico de una lista: al resulatado se le conoce como
# "un slice".

print("1:4", players[1:4]) # ["juan", "iancarlo", "lisandro"]
print(":3", players[:3]) # ["charly", "juan", "iancarlo"]
print("2:", players[2:]) # ["iancarlo", "lisandro"]
print("[-3:]", players[-3:]) # ["juan", "iancarlo", "lisandro"]

# players = ["chalrly", "juan", "iancarlo", "lisandro"]
# casos especiales de slicing
print(players[1:6]) # ["juan", "iancarlo", "lisandro"]
print(players[6:1])
print(players[:0])

 # looping through a slice
 print("looping through a slice")
 students = ["raul", "juan", "iancarlo", "lisandro"]
 # slicing 







# como podemos copiar una lista?
my_food = ["piza", "tacos", "flautas"]
my_friend_food = my_food # manera erronea de copiar una lista 

# tres maneras de copiar una lista 
# metodo 1 - utilizando slicing
my_friend_food2 = my_food[:]
#metodo 2 - utilizando el metodo de las listas .copy()
my_friend_food3 = my_food. copy()






