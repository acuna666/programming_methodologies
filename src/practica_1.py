"""
crear una listra con 
los primeros diez numeros cuadraticos.
"""
squares = []
for value in range(0,11):
    square = value**2
    squares.append(square)
print(squares)