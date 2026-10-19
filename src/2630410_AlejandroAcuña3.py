# ==============================================================================
# PORTADA / COVER PAGE
# ==============================================================================
# Nombre del estudiante: Alejandro Acuña
# Matrícula: [2630410]
# Grupo: [IM-12]
# Materia: Fundamentos de Programación - Colecciones en Python
# Fecha: 18 de octubre de 2026
# ==============================================================================

# ==============================================================================
# RESUMEN EJECUTIVO
# ==============================================================================
# En Python, las listas, tuplas y diccionarios son estructuras de datos
# fundamentales para almacenar y organizar colecciones de elementos. Una lista
# (list) es una secuencia ordenada y mutable que permite agregar, eliminar y
# modificar elementos dinámicamente. Una tupla (tuple) es una secuencia ordenada
# e inmutable diseñada para datos fijos que no deben alterarse tras su creación.
# Un diccionario (dict) es una estructura de mapeo clave-valor que permite
# búsquedas rápidas mediante claves únicas. La mutabilidad de las listas permite
# cambios en el mismo objeto, mientras que la inmutabilidad de las tuplas
# garantiza la integridad de los datos. Los diccionarios asocian claves
# descriptivas con valores para modelar entidades complejas. Este archivo
# presenta seis programas completos que cubren operaciones básicas con listas,
# geometría con tuplas, catálogo de precios con diccionarios, seguimiento de
# calificaciones con diccionarios y listas, recuento de frecuencias de palabras
# y un libro de contactos CRUD basado en diccionarios.
# ==============================================================================

# ==============================================================================
# PRINCIPIOS Y BUENAS PRÁCTICAS
# ==============================================================================
# 1. Usar listas cuando necesites agregar, eliminar o reordenar elementos con frecuencia.
# 2. Usar tuplas para datos que no deben cambiar (coordenadas, fechas, registros fijos).
# 3. Usar diccionarios cuando necesites buscar información por una clave única.
# 4. Evitar modificar una lista mientras la recorres con un ciclo for.
# 5. Usar nombres de claves descriptivos en los diccionarios (ej. "name", "price").
# 6. Escribir código legible usando lower_snake_case para variables y
#    UPPER_SNAKE_CASE para constantes, con mensajes claros en pantalla.
# ==============================================================================

import math


# ==============================================================================
# PROBLEMA 1: SHOPPING LIST BASICS (OPERACIONES CON LISTAS)
# ==============================================================================
# Problem 1: Shopping list basics
# Description: Convierte una cadena de texto separada por comas en una lista de
# productos típicos del mercado, agrega un nuevo producto al final, muestra el
# total de elementos y verifica si un producto específico existe en la lista.
#
# Inputs:
# - initial_items_text (str): Lista de productos separados por comas.
# - new_item (str): Producto nuevo a agregar.
# - search_item (str): Producto a buscar.
#
# Outputs:
# - "Items list:" <items_list>
# - "Total items:" <len_list>
# - "Found item:" true|false
#
# Validations:
# - Verificar que las entradas no estén vacías tras aplicar strip().
# - Limpiar espacios extra en cada elemento de la lista.
# - Manejar entradas vacías mostrando un mensaje de error.
#
# Test cases:
# 1) Normal: initial_items_text="aguacate, jitomate, cebolla", new_item="cilantro", search_item="jitomate"
#    -> Items list: ['aguacate', 'jitomate', 'cebolla', 'cilantro'], Total items: 4, Found item: true
# 2) Border: initial_items_text="  aguacate  ", new_item="  mango  ", search_item="AGUACATE"
#    -> Items list: ['aguacate', 'mango'], Total items: 2, Found item: false (case-sensitive)
# 3) Error: initial_items_text="   ", new_item="cilantro", search_item="jitomate"
#    -> Error: invalid input
# ==============================================================================

def run_problem_1(initial_items_text: str, new_item: str, search_item: str) -> None:
    print("\n--- PROBLEM 1: Shopping list basics ---")
    
    clean_initial = initial_items_text.strip()
    clean_new = new_item.strip()
    clean_search = search_item.strip()
    
    if not clean_initial or not clean_new or not clean_search:
        print("Error: invalid input")
        return

    # Separar y limpiar los elementos de la lista
    raw_items = clean_initial.split(",")
    items_list = [item.strip() for item in raw_items if item.strip()]
    
    if not items_list:
        print("Error: invalid input")
        return

    # Agregar nuevo elemento
    items_list.append(clean_new)
    
    # Realizar búsqueda
    is_in_list = clean_search in items_list
    
    print(f"Items list: {items_list}")
    print(f"Total items: {len(items_list)}")
    print(f"Found item: {str(is_in_list).lower()}")


# Casos de prueba para el Problema 1
print("=== Running Test Cases for Problem 1 ===")
run_problem_1("aguacate, jitomate, cebolla", "cilantro", "jitomate")  # Caso Normal
run_problem_1("  aguacate  ", "  mango  ", "AGUACATE")                # Caso Borde
run_problem_1("   ", "cilantro", "jitomate")                          # Caso Error


# ==============================================================================
# PROBLEMA 2: POINTS AND DISTANCES WITH TUPLES (TUPLAS)
# ==============================================================================
# Problem 2: Points and distances with tuples
# Description: Recibe coordenadas para dos puntos geográficos o de mapa en un plano 2D,
# crea tuplas inmutables para cada punto, calcula la distancia euclidiana y determina
# el punto medio entre ambos.
#
# Inputs:
# - x1, y1 (float o str convertible): Coordenadas del Punto A.
# - x2, y2 (float o str convertible): Coordenadas del Punto B.
#
# Outputs:
# - "Point A:" (x1, y1)
# - "Point B:" (x2, y2)
# - "Distance:" <distance>
# - "Midpoint:" (mx, my)
#
# Validations:
# - Validar que las 4 entradas puedan convertirse a float.
# - Mostrar mensaje de error si la conversión de tipo falla.
#
# Test cases:
# 1) Normal: x1=19.4326, y1=-99.1332, x2=20.6597, y2=-103.3496 (CDMX a Guadalajara aprox.)
#    -> Point A: (19.4326, -99.1332), Point B: (20.6597, -103.3496), Distance: 4.3782, Midpoint: (20.04615, -101.2414)
# 2) Border: x1=25.6866, y1=-100.3161, x2=25.6866, y2=-100.3161 (Mismo punto en Monterrey)
#    -> Point A: (25.6866, -100.3161), Point B: (25.6866, -100.3161), Distance: 0.0, Midpoint: (25.6866, -100.3161)
# 3) Error: x1="cdmx", y1=-99.1332, x2=20.6597, y2=-103.3496
#    -> Error: invalid input
# ==============================================================================

def run_problem_2(x1_raw, y1_raw, x2_raw, y2_raw) -> None:
    print("\n--- PROBLEM 2: Points and distances with tuples ---")
    
    try:
        x1 = float(x1_raw)
        y1 = float(y1_raw)
        x2 = float(x2_raw)
        y2 = float(y2_raw)
    except (ValueError, TypeError):
        print("Error: invalid input")
        return

    point_a = (x1, y1)
    point_b = (x2, y2)

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    midpoint = ((x1 + x2) / 2.0, (y1 + y2) / 2.0)

    print(f"Point A: {point_a}")
    print(f"Point B: {point_b}")
    print(f"Distance: {round(distance, 4)}")
    print(f"Midpoint: {midpoint}")


# Casos de prueba para el Problema 2
print("\n=== Running Test Cases for Problem 2 ===")
run_problem_2(19.4326, -99.1332, 20.6597, -103.3496) # Caso Normal
run_problem_2(25.6866, -100.3161, 25.6866, -100.3161) # Caso Borde
run_problem_2("cdmx", -99.1332, 20.6597, -103.3496)   # Caso Error


# ==============================================================================
# PROBLEMA 3: PRODUCT CATALOG WITH DICTIONARY (DICCIONARIOS)
# ==============================================================================
# Problem 3: Product catalog with dictionary
# Description: Mantiene un catálogo de abarrote o panadería con precios en pesos (MXN).
# Busca un producto, valida la cantidad a comprar y calcula el costo total.
#
# Inputs:
# - product_name (str): Nombre del producto a buscar.
# - quantity (int o str convertible): Cantidad a comprar.
#
# Outputs:
# - Si existe y cantidad > 0:
#     "Unit price:" <unit_price>
#     "Quantity:" <quantity>
#     "Total:" <total_price>
# - Si no existe o cantidad <= 0:
#     "Error: product not found" O "Error: invalid input"
#
# Validations:
# - product_name no debe estar vacío tras aplicar strip().
# - quantity debe ser un entero estrictamente mayor a 0.
# - Verificar la existencia de la clave antes de acceder al diccionario.
#
# Test cases:
# 1) Normal: product_name="aguacate", quantity=3
#    -> Unit price: 45.0, Quantity: 3, Total: 135.0
# 2) Border: product_name="concha", quantity=1
#    -> Unit price: 12.5, Quantity: 1, Total: 12.5
# 3) Error: product_name="rambutan", quantity=2
#    -> Error: product not found
# ==============================================================================

def run_problem_3(product_name: str, quantity_raw) -> None:
    print("\n--- PROBLEM 3: Product catalog with dictionary ---")
    
    product_prices = {
        "aguacate": 45.0,
        "concha": 12.5,
        "jitomate": 28.0,
        "tortillas": 22.0
    }

    clean_product = str(product_name).strip()
    
    try:
        quantity = int(quantity_raw)
        if quantity <= 0 or not clean_product:
            print("Error: invalid input")
            return
    except (ValueError, TypeError):
        print("Error: invalid input")
        return

    if clean_product not in product_prices:
        print("Error: product not found")
        return

    unit_price = product_prices[clean_product]
    total_price = unit_price * quantity

    print(f"Unit price: {unit_price}")
    print(f"Quantity: {quantity}")
    print(f"Total: {round(total_price, 2)}")


# Casos de prueba para el Problema 3
print("\n=== Running Test Cases for Problem 3 ===")
run_problem_3("aguacate", 3)   # Caso Normal
run_problem_3("concha", 1)     # Caso Borde
run_problem_3("rambutan", 2)   # Caso Error


# ==============================================================================
# PROBLEMA 4: STUDENT GRADES WITH DICT AND LIST (DICCIONARIOS Y LISTAS)
# ==============================================================================
# Problem 4: Student grades with dict and list
# Description: Almacena nombres de estudiantes hispanos como claves y listas de
# calificaciones (escala 0-100) como valores. Calcula el promedio y determina si aprobó (>= 70.0).
#
# Inputs:
# - student_name (str): Nombre del estudiante.
#
# Outputs:
# - Si el estudiante existe:
#     "Grades:" <grades_list>
#     "Average:" <average>
#     "Passed:" true|false
# - Si no existe:
#     "Error: student not found"
#
# Validations:
# - Validar que student_name no esté vacío.
# - Confirmar que la clave exista en el diccionario.
# - Verificar que la lista de calificaciones no esté vacía antes del promedio.
#
# Test cases:
# 1) Normal: student_name="Mateo"
#    -> Grades: [90.0, 85.0, 88.0], Average: 87.67, Passed: true
# 2) Border: student_name="Sofía"
#    -> Grades: [70.0, 70.0], Average: 70.0, Passed: true
# 3) Error: student_name="Rodrigo"
#    -> Error: student not found
# ==============================================================================

def run_problem_4(student_name: str) -> None:
    print("\n--- PROBLEM 4: Student grades with dict and list ---")
    
    PASSING_SCORE = 70.0
    student_grades = {
        "Mateo": [90.0, 85.0, 88.0],
        "Ximena": [60.0, 65.0, 58.0],
        "Sofía": [70.0, 70.0]
    }

    clean_name = str(student_name).strip()
    
    if not clean_name:
        print("Error: invalid input")
        return

    if clean_name not in student_grades:
        print("Error: student not found")
        return

    grades_list = student_grades[clean_name]
    
    if not grades_list:
        print("Error: invalid input")
        return

    average = sum(grades_list) / len(grades_list)
    is_passed = average >= PASSING_SCORE

    print(f"Grades: {grades_list}")
    print(f"Average: {round(average, 2)}")
    print(f"Passed: {str(is_passed).lower()}")


# Casos de prueba para el Problema 4
print("\n=== Running Test Cases for Problem 4 ===")
run_problem_4("Mateo")    # Caso Normal
run_problem_4("Sofía")    # Caso Borde (Justo en el límite de aprobación)
run_problem_4("Rodrigo")  # Caso Error


# ==============================================================================
# PROBLEMA 5: WORD FREQUENCY COUNTER (FRECUENCIA DE PALABRAS)
# ==============================================================================
# Problem 5: Word frequency counter
# Description: Convierte una oración en español a minúsculas, remueve signos de puntuación
# simples, cuenta la frecuencia de cada palabra usando un diccionario y determina
# la palabra más común.
#
# Inputs:
# - sentence (str): Oración de texto a analizar.
#
# Outputs:
# - "Words list:" <words_list>
# - "Frequencies:" <freq_dict>
# - "Most common word:" <word>
#
# Validations:
# - La oración no debe estar vacía tras aplicar strip().
# - Se limpian signos de puntuación básicos (.,!?;:¡¿).
# - Garantizar que la lista de palabras no esté vacía.
#
# Test cases:
# 1) Normal: sentence="el taco de pastor con todo es el mejor taco"
#    -> Words list: [...], Frequencies: {...}, Most common word: "taco"
# 2) Border: sentence="hola hola hola"
#    -> Words list: ['hola', 'hola', 'hola'], Frequencies: {'hola': 3}, Most common word: "hola"
# 3) Error: sentence="   "
#    -> Error: invalid input
# ==============================================================================

def run_problem_5(sentence: str) -> None:
    print("\n--- PROBLEM 5: Word frequency counter ---")
    
    clean_sentence = str(sentence).strip().lower()
    
    if not clean_sentence:
        print("Error: invalid input")
        return

    # Remover signos de puntuación comunes en español e inglés
    for symbol in [".", ",", "!", "?", ";", ":", "¡", "¿"]:
        clean_sentence = clean_sentence.replace(symbol, "")

    words_list = clean_sentence.split()
    
    if not words_list:
        print("Error: invalid input")
        return

    freq_dict = {}
    for word in words_list:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1

    # Encontrar la palabra de mayor frecuencia
    most_common_word = None
    max_count = -1
    for word, count in freq_dict.items():
        if count > max_count:
            max_count = count
            most_common_word = word

    print(f"Words list: {words_list}")
    print(f"Frequencies: {freq_dict}")
    print(f"Most common word: {most_common_word}")


# Casos de prueba para el Problema 5
print("\n=== Running Test Cases for Problem 5 ===")
run_problem_5("el taco de pastor con todo es el mejor taco") # Caso Normal
run_problem_5("hola hola hola")                              # Caso Borde
run_problem_5("   ")                                        # Caso Error


# ==============================================================================
# PROBLEMA 6: SIMPLE CONTACT BOOK (AGENDA CRUD)
# ==============================================================================
# Problem 6: Simple contact book
# Description: Implementa una agenda de contactos telefónicos mexicanos (10 dígitos)
# con diccionario que permite agregar/actualizar ("ADD"), buscar ("SEARCH") y eliminar ("DELETE").
#
# Inputs:
# - action_text (str): Acción a realizar ("ADD", "SEARCH" o "DELETE").
# - name (str): Nombre del contacto.
# - phone (str, opcional): Número telefónico de 10 dígitos (solo para "ADD").
#
# Outputs:
# - "Contact saved:" name, phone  (para ADD)
# - "Phone:" <phone>              (para SEARCH si existe)
# - "Contact deleted:" name       (para DELETE si existe)
# - "Error: contact not found"    (para SEARCH/DELETE si no existe)
# - "Error: invalid input"        (para entradas inválidas u opciones no válidas)
#
# Validations:
# - Normalizar action_text a mayúsculas.
# - Verificar que action_text pertenezca a ["ADD", "SEARCH", "DELETE"].
# - Validar cadenas no vacías para name y phone.
#
# Test cases:
# 1) Normal: action_text="ADD", name="Carlos", phone="8112345678"
#    -> Contact saved: Carlos, 8112345678
# 2) Border: action_text="search", name="Valeria" (acción en minúsculas)
#    -> Phone: 5551234567
# 3) Error: action_text="DELETE", name="Inexistente"
#    -> Error: contact not found
# ==============================================================================

contacts = {
    "Valeria": "5551234567",
    "Santiago": "3339876543"
}

def run_problem_6(action_text: str, name: str, phone: str = "") -> None:
    print("\n--- PROBLEM 6: Simple contact book ---")
    
    clean_action = str(action_text).strip().upper()
    clean_name = str(name).strip()
    clean_phone = str(phone).strip()

    VALID_ACTIONS = ["ADD", "SEARCH", "DELETE"]

    if clean_action not in VALID_ACTIONS or not clean_name:
        print("Error: invalid input")
        return

    if clean_action == "ADD":
        if not clean_phone:
            print("Error: invalid input")
            return
        contacts[clean_name] = clean_phone
        print(f"Contact saved: {clean_name}, {clean_phone}")

    elif clean_action == "SEARCH":
        if clean_name in contacts:
            print(f"Phone: {contacts[clean_name]}")
        else:
            print("Error: contact not found")

    elif clean_action == "DELETE":
        if clean_name in contacts:
            contacts.pop(clean_name)
            print(f"Contact deleted: {clean_name}")
        else:
            print("Error: contact not found")


# Casos de prueba para el Problema 6
print("\n=== Running Test Cases for Problem 6 ===")
run_problem_6("ADD", "Carlos", "8112345678")  # Caso Normal
run_problem_6("search", "Valeria")             # Caso Borde (Normalización de minúsculas)
run_problem_6("DELETE", "Inexistente")         # Caso Error


# ==============================================================================
# CONCLUSIONES
# ==============================================================================
# La selección adecuada de colecciones en Python depende directamente de las
# necesidades del problema. Las listas son ideales para conjuntos de datos
# dinámicos donde se requiere agregar, remover u ordenar elementos constantemente.
# Las tuplas ofrecen inmutabilidad y eficiencia, siendo excelentes para representar
# registros fijos como coordenadas o puntos geométricos. Los diccionarios proveen
# un rendimiento alto en búsquedas por clave, permitiendo mapear identificadores
# a datos complejos. La combinación de estas estructuras (como diccionarios de
# listas) resulta muy útil para modelar escenarios reales como registros de
# alumnos o listas de contactos.
# ==============================================================================

# ==============================================================================
# REFERENCIAS
# ==============================================================================
# Referencias:
# 1) Python Software Foundation. (2026). Built-in Types: list, tuple, dict. 
#    Python 3 Documentation.
#    https://docs.python.org/3/library/stdtypes.html
# 2) van Rossum, G., Warsaw, B., & Coghlan, A. (2001). PEP 8 – Style Guide for Python Code.
#    Python Software Foundation.
#    https://peps.python.org/pep-0008/
# 3) Lutz, M. (2013). Learning Python: Powerful Object-Oriented Programming (5th ed.). O'Reilly Media.
#    https://www.oreilly.com/library/view/learning-python-5th/9781449355722/
# 4) Sweigart, A. (2019). Automate the Boring Stuff with Python (2nd ed.). No Starch Press.
#    https://automatetheboringstuff.com/
# 5) Severance, C. (2016). Python for Everybody: Exploring Data Using Python 3.
#    https://www.py4e.com/book
# ==============================================================================