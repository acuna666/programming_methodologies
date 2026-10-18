#Combinacion o Concatenacion de Strings
from email.mime import message


first_name = 'alejandro'
last_name = 'acuña'
full_name = first_name + ' ' + last_name
print(full_name)

print("Hola", "alejandro" + " " + "acuña", first_name.title() + " " + last_name.title())

message = "¡Hola, " + full_name.title() + "!"
print(message) 

#Whitespace
"""
    White space se refiere a cualquier STring(caracter)
    que no se imprime, es decir, un espacio (" "), tabuladoras (\t) y finales de linea (\n)
    Los whitespace se utilizan comunmente para organizar las salidas
    de texto a usuario de tal manera que sea mas amigable de leer o ver para los usuarios.
"""

print("Python")
print("\tPython")
print("\t\tPython")
print("Lenguajes: \nPython \nC \nJavaScript")

# f-stings
famous_person = "charly mercury"
message = f"{famous_person.title()} una vez dijo: Python es amor"
print(message)

quote = "Python is in the air" 