# Trabajando con listas
print("el dia de hoy aprendere a trabjar con listas".upper())
magicians =  ["harry", "ron", "hermione", "snape"]
print(magicians)

print(magicians[0], magicians[1], magicians[2], magicians[3])

# ciclo for
for magician in magicians:
    print(magician)

# Argumento de print end="" quita el salto de linea
# A esto se le conoce como looping

# Ahora vamos a imprimir un mensaje para cada mago

for magician in magicians:
    print(f"{magician.title()} ese fue un gran hechizo.")
    print(f"No puedo esperar a ver el siguiente hechizo, {magician.upper()}\n")
print("Gracias a todos. Fue un gran espectaculo")

# identificacion
"""
python utiliza la identificacion para determinar 
cuando una linea de codigo esta conectada a la 
linea de codigo anterior.

basicamente, se utilizan 4 espacios en blanco para
obligarlos a escribir codigo ordenado y estructurado.
"""

magicians = ["aice", "david", "caroline"]
for magician in magicians:
 print(magician) # identacion error 


 # error de logica - logic error - identation error 
 for magician in magicians:
    print(magician)
    print(f"no puedo esperar a ver el sigiente truco, {magician}")

# identacion inecesaria 
message = "hello python world!"
#    print(message)

# no olvidar los dos puntos - sintax error 
for magician in magicians 
   print(magician)
   

