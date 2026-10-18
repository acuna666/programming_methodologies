"""
==============================================================================
PORTADA
==============================================================================
Nombre del estudiante: Alejandro Acuña
Matrícula: [2630410]
Grupo: [IM-12]
Materia: Fundamentos de Programación / Python
Tarea: Manejo de Cadenas de Texto (t_strings)
==============================================================================

==============================================================================
RESUMEN EJECUTIVO
==============================================================================
En Python, una cadena de texto (string) es una secuencia inmutable de caracteres 
(tipo de dato 'str'). Debido a su inmutabilidad, cualquier modificación (como 
convertir a mayúsculas o eliminar espacios) genera un nuevo objeto en memoria en 
lugar de modificar el original. Las operaciones básicas incluyen concatenación, 
cálculo de longitud, slicing (rebanado), búsqueda de patrones, reemplazo y formato.
Validar y normalizar el texto de entrada (como nombres, correos o contraseñas) es 
crucial para evitar errores en tiempo de ejecución y asegurar que los datos procesados 
sean confiables. Este script incluye 6 problemas que demuestran el uso de métodos 
de string (strip, split, join, title, lower, find, count, replace), slicing, f-strings 
y métodos de clasificación de caracteres. Cada problema cuenta con descripción, 
diseño de entradas y salidas, validaciones y 3 casos de prueba (normal, borde y error).
==============================================================================

==============================================================================
PRINCIPIOS Y BUENAS PRÁCTICAS
==============================================================================
1. Inmutabilidad de cadenas: Entender que operaciones como text.replace() o 
   text.strip() devuelven una nueva cadena sin alterar la variable original.
2. Normalización de entrada: Limpiar siempre el texto del usuario con strip() y 
   lower()/upper() antes de realizar comparaciones o validaciones.
3. Evitar "números mágicos": Documentar qué extrae cada slice o índice específico.
4. Métodos nativos de string: Preferir los métodos integrados de Python (split, 
   join, isalnum) en lugar de reimplementar lógica manual básica.
5. Orden de validación claro: Verificar primero que la cadena no esté vacía 
   (tras usar strip) y luego validar el formato o estructura.
6. Código limpio y nomenclatura en inglés: Usar lower_snake_case para variables, 
   UPPER_SNAKE_CASE para constantes y mensajes de salida claros en inglés.
==============================================================================
"""

# ==============================================================================
# PROBLEMA 1: Formateador de nombre completo (nombre + iniciales)
# ==============================================================================

"""
Problem 1: Full name formatter (name + initials)
Descripción:
    Normaliza el nombre completo de una persona eliminando espacios innecesarios
    y corrigiendo el formato de mayúsculas/minúsculas. Muestra el nombre en 
    Title Case y genera las iniciales en mayúsculas separadas por puntos.

Entradas:
    - full_name (string): Nombre completo del usuario, puede contener espacios 
      extra y mayúsculas/minúsculas mezcladas.

Salidas:
    - "Formatted name: <Name In Title Case>"
    - "Initials: <X.X.X.>"

Validaciones:
    - full_name no debe estar vacío después de strip().
    - Debe contener al menos dos palabras (nombre y apellido).
    - No aceptar cadenas compuestas solo por espacios.

Casos de prueba:
    1) Normal: "alejandro acuña" -> Formatted name: Alejandro Acuña, Initials: A.A.
    2) Borde: "  a   b  " -> Formatted name: A B, Initials: A.B.
    3) Error: "  Alejandro  " -> Error: invalid input
"""

def format_full_name(full_name: str) -> None:
    cleaned_input = full_name.strip()
    
    # Validación 1: Verificar que no esté vacío
    if not cleaned_input:
        print("Error: invalid input")
        return
        
    words = cleaned_input.split()
    
    # Validación 2: Verificar que tenga al menos dos palabras
    if len(words) < 2:
        print("Error: invalid input")
        return
        
    formatted_words = [word.capitalize() for word in words]
    formatted_name = " ".join(formatted_words)
    initials = ".".join([word[0].upper() for word in words]) + "."
    
    print(f"Formatted name: {formatted_name}")
    print(f"Initials: {initials}")


# ==============================================================================
# PROBLEMA 2: Validador simple de correo (estructura + dominio)
# ==============================================================================

"""
Problem 2: Simple email validator (structure + domain)
Descripción:
    Valida si una dirección de correo tiene un formato básico correcto: contiene 
    exactamente un '@', tiene al menos un '.' en el dominio y no incluye espacios. 
    Si es válido, extrae y muestra la parte del dominio.

Entradas:
    - email_text (string): Dirección de correo a validar.

Salidas:
    - "Valid email: true" o "Valid email: false"
    - Si es válido: "Domain: <domain_part>"

Validaciones:
    - email_text no debe estar vacío tras strip().
    - No debe contener ningún espacio en blanco.
    - Debe contener exactamente un carácter '@'.
    - Debe contener al menos un '.' después del '@'.

Casos de prueba:
    1) Normal: "user@domain.com" -> Valid email: true, Domain: domain.com
    2) Borde: "a@b.co" -> Valid email: true, Domain: b.co
    3) Error: "user name@domain.com" o "user@@domain.com" -> Valid email: false
"""

def validate_email(email_text: str) -> None:
    cleaned_email = email_text.strip()
    
    # Validación 1: No vacío y sin espacios intermedios
    if not cleaned_email or " " in cleaned_email:
        print("Valid email: false")
        return

    # Validación 2: Exactamente un símbolo '@'
    if cleaned_email.count("@") != 1:
        print("Valid email: false")
        return

    at_index = cleaned_email.find("@")
    domain_part = cleaned_email[at_index + 1:]

    # Validación 3: Usuario no vacío, dominio no vacío y '.' presente en el dominio
    if at_index == 0 or not domain_part or "." not in domain_part:
        print("Valid email: false")
        return

    print("Valid email: true")
    print(f"Domain: {domain_part}")


# ==============================================================================
# PROBLEMA 3: Verificador de palíndromos (ignorando espacios y mayúsculas)
# ==============================================================================

"""
Problem 3: Palindrome checker (ignoring spaces and case)
Descripción:
    Determina si una frase es un palíndromo (se lee igual de izquierda a derecha 
    que de derecha a izquierda), ignorando espacios y diferencia entre mayúsculas 
    y minúsculas.

Entradas:
    - phrase (string): Frase u oración a evaluar.

Salidas:
    - "Is palindrome: true" o "Is palindrome: false"

Validaciones:
    - phrase no debe estar vacía tras strip().
    - Debe tener una longitud mínima de 3 caracteres válidos tras eliminar espacios.

Casos de prueba:
    1) Normal: "Anita lava la tina" -> Is palindrome: true
    2) Borde: "Aba" -> Is palindrome: true
    3) Error: "  " o "Hi" -> Error: invalid input
"""

MIN_PALINDROME_LENGTH = 3

def check_palindrome(phrase: str) -> None:
    cleaned_phrase = phrase.strip()
    normalized_phrase = cleaned_phrase.replace(" ", "").lower()
    
    if len(normalized_phrase) < MIN_PALINDROME_LENGTH:
        print("Error: invalid input")
        return
        
    is_palindrome = normalized_phrase == normalized_phrase[::-1]
    
    if is_palindrome:
        print("Is palindrome: true")
    else:
        print("Is palindrome: false")


# ==============================================================================
# PROBLEMA 4: Estadísticas de palabras en una oración
# ==============================================================================

"""
Problem 4: Sentence word stats (lengths and first/last word)
Descripción:
    Analiza una oración para contar el total de palabras, identificar la primera 
    y última palabra, y encontrar la palabra más corta y la más larga por longitud.

Entradas:
    - sentence (string): Texto u oración a analizar.

Salidas:
    - "Word count: <n>"
    - "First word: <...>"
    - "Last word: <...>"
    - "Shortest word: <...>"
    - "Longest word: <...>"

Validaciones:
    - sentence no debe estar vacía tras strip().
    - Debe contener al menos una palabra válida después de aplicar split().

Casos de prueba:
    1) Normal: "Python programming language is powerful" -> Count: 5, First: Python, Last: powerful, Shortest: is, Longest: programming
    2) Borde: "   SingleWord   " -> Count: 1, First/Last/Shortest/Longest: SingleWord
    3) Error: "   " -> Error: invalid input
"""

def analyze_sentence(sentence: str) -> None:
    cleaned_sentence = sentence.strip()
    
    if not cleaned_sentence:
        print("Error: invalid input")
        return

    words = cleaned_sentence.split()
    if not words:
        print("Error: invalid input")
        return

    word_count = len(words)
    first_word = words[0]
    last_word = words[-1]

    shortest_word = min(words, key=len)
    longest_word = max(words, key=len)

    print(f"Word count: {word_count}")
    print(f"First word: {first_word}")
    print(f"Last word: {last_word}")
    print(f"Shortest word: {shortest_word}")
    print(f"Longest word: {longest_word}")


# ==============================================================================
# PROBLEMA 5: Clasificador de fortaleza de contraseña
# ==============================================================================

"""
Problem 5: Password strength classifier
Descripción:
    Clasifica una contraseña como "weak", "medium" o "strong" según su longitud 
    y variedad de tipos de caracteres.

Reglas:
    - Weak: Longitud < 8 o falta de variedad de caracteres.
    - Medium: Longitud >= 8 y al menos dos categorías de caracteres.
    - Strong: Longitud >= 8 y contiene mayúsculas, minúsculas, dígitos y símbolos especiales.

Entradas:
    - password_input (string): Contraseña a evaluar.

Salidas:
    - "Password strength: weak" | "medium" | "strong"

Validaciones:
    - password_input no debe estar vacía.

Casos de prueba:
    1) Normal: "Pass123!" -> Password strength: strong
    2) Borde: "Pass2024" -> Password strength: medium
    3) Error: "1234" o "" -> Password strength: weak / Error: invalid input
"""

MIN_PASSWORD_LENGTH = 8

def classify_password(password_input: str) -> None:
    if not password_input:
        print("Error: invalid input")
        return

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for char in password_input:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum():
            has_special = True

    types_count = sum([has_upper, has_lower, has_digit, has_special])
    
    if len(password_input) >= MIN_PASSWORD_LENGTH and types_count == 4:
        strength = "strong"
    elif len(password_input) >= MIN_PASSWORD_LENGTH and types_count >= 2:
        strength = "medium"
    else:
        strength = "weak"

    print(f"Password strength: {strength}")


# ==============================================================================
# PROBLEMA 6: Formateador de etiqueta de producto (ancho fijo)
# ==============================================================================

"""
Problem 6: Product label formatter (fixed-width text)
Descripción:
    Genera una etiqueta de producto en una sola línea combinando el nombre del 
    producto y su precio. La cadena resultante debe medir exactamente 30 caracteres: 
    se recorta si supera la longitud o se rellena con espacios si es más corta.

Formato:
    Product: <NAME> | Price: $<PRICE>

Entradas:
    - product_name (string): Nombre del producto.
    - price_value (float o string numérico): Precio numérico positivo.

Salidas:
    - "Label: '<exactamente 30 caracteres>'"

Validaciones:
    - product_name no debe estar vacío tras strip().
    - price_value debe ser un número válido mayor o igual a 0.

Casos de prueba:
    1) Normal: product_name="Laptop", price_value="999.99" -> Exactamente 30 caracteres
    2) Borde: product_name="Ultra Super Deluxe High End Mechanical Keyboard", price_value="150.0" -> Recortado a 30 caracteres
    3) Error: product_name="", price_value="-50" -> Error: invalid input
"""

LABEL_LENGTH = 30

def format_product_label(product_name: str, price_value: str) -> None:
    cleaned_name = product_name.strip()
    
    if not cleaned_name:
        print("Error: invalid input")
        return

    try:
        numeric_price = float(price_value)
        if numeric_price < 0:
            print("Error: invalid input")
            return
    except ValueError:
        print("Error: invalid input")
        return

    base_label = f"Product: {cleaned_name} | Price: ${numeric_price:.2f}"
    
    if len(base_label) > LABEL_LENGTH:
        final_label = base_label[:LABEL_LENGTH]
    else:
        final_label = base_label.ljust(LABEL_LENGTH)

    print(f"Label: '{final_label}'")


# ==============================================================================
# EJECUCIÓN PRINCIPAL / SUITE DE PRUEBAS
# ==============================================================================

if __name__ == "__main__":
    print("=== PROBLEMA 1 PRUEBAS ===")
    format_full_name("alejandro acuña")          # Normal
    format_full_name("  a   b  ")               # Borde
    format_full_name("  Alejandro  ")          # Error

    print("\n=== PROBLEMA 2 PRUEBAS ===")
    validate_email("user@domain.com")          # Normal
    validate_email("a@b.co")                   # Borde
    validate_email("user@@domain.com")         # Error

    print("\n=== PROBLEMA 3 PRUEBAS ===")
    check_palindrome("Anita lava la tina")     # Normal
    check_palindrome("Aba")                    # Borde
    check_palindrome("  ")                     # Error

    print("\n=== PROBLEMA 4 PRUEBAS ===")
    analyze_sentence("Python programming language is powerful") # Normal
    analyze_sentence("   SingleWord   ")                           # Borde
    analyze_sentence("   ")                                       # Error

    print("\n=== PROBLEMA 5 PRUEBAS ===")
    classify_password("Pass123!")              # Normal
    classify_password("Pass2024")              # Borde
    classify_password("1234")                  # Error

    print("\n=== PROBLEMA 6 PRUEBAS ===")
    format_product_label("Laptop", "999.99")   # Normal
    format_product_label("Ultra Super Deluxe High End Mechanical Keyboard", "150.0") # Borde
    format_product_label("", "-50")            # Error

"""
==============================================================================
CONCLUSIONES
==============================================================================
1. El procesamiento de cadenas es esencial en el desarrollo de software debido a 
   que la mayoría de las entradas de datos (formularios web, archivos, bases de 
   datos) se reciben inicialmente como texto sin formato.
2. El uso de métodos nativos como lower(), strip(), split() y join() simplifica 
   la limpieza de datos sin necesidad de escribir algoritmos complejos manualmente.
3. Normalizar el texto antes de realizar comparaciones previene errores lógicos 
   provocados por diferencias de mayúsculas o espacios accidentales.
4. Diseñar validaciones estrictas antes del procesamiento evita fallos críticos 
   en tiempo de ejecución (como errores de índice) y garantiza la estabilidad del programa.
5. Comprender la inmutabilidad de los strings y el manejo de slicing permite extraer 
   información específica, invertir texto y dar formato con ancho fijo de manera eficiente.
==============================================================================

==============================================================================
REFERENCIAS
==============================================================================
References:
1) Python Software Foundation. (2024). Built-in Types: Text Sequence Type — str. 
   Python Official Documentation. 
   https://docs.python.org/3/library/stdtypes.html#textseq

2) Real Python. (2023). Python String Formatting Best Practices. 
   Real Python Tutorials. 
   https://realpython.com/python-string-formatting/

3) GeeksforGeeks. (2024). Python String Methods & Operations. 
   GeeksforGeeks Programming Guides. 
   https://www.geeksforgeeks.org/python-strings/

4) W3Schools. (2024). Python String Methods Reference. 
   W3Schools Online Web Tutorials. 
   https://www.w3schools.com/python/python_ref_string.asp

5) Sweigart, A. (2019). Automate the Boring Stuff with Python: Manipulating Strings. 
   Online Book Reference. 
   https://automatetheboringstuff.com/2e/chapter6/
==============================================================================
"""