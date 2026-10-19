"""
==============================================================================
PORTADA
==============================================================================
Nombre del estudiante: Alejandro Acuña
Matrícula: [2630410]
Grupo: [IM-12]
Materia: Fundamentos de Programación / Python
Tarea: Tipos Numéricos (int, float) y Valores Booleanos
==============================================================================

==============================================================================
RESUMEN EJECUTIVO
==============================================================================
En Python, los tipos numéricos principales son 'int' (números enteros sin decimales) 
y 'float' (números de punto flotante con decimales). La diferencia fundamental radica 
en cómo representan las cantidades: 'int' se usa para conteos discretos y exactos, 
mientras que 'float' permite medir magnitudes continuas con precisión decimal. 
Los valores booleanos ('bool', con estados True o False) representan la veracidad de 
una condición y se obtienen principalmente mediante operadores relacionales 
(<, >, <=, >=, ==, !=) y lógicos (and, or, not). Validar los rangos de entrada y 
prevenir la división entre cero es crucial para asegurar la estabilidad del software 
y evitar fallos en tiempo de ejecución. Este archivo aborda 6 problemas numéricos 
reales (conversión de temperatura, cálculo de nómina, elegibilidad de descuentos, 
estadísticas básicas, evaluación de préstamos e índice de masa corporal), incluyendo 
descripción, diseño de entradas/salidas, validaciones estrictas y 3 casos de prueba 
(normal, borde y error) para cada uno.
==============================================================================

==============================================================================
PRINCIPIOS Y BUENAS PRÁCTICAS
==============================================================================
1. Selección adecuada de tipos: Usar 'int' para cantidades contables e índices, 
   y 'float' para magnitudes continuas, monedas o mediciones físicas.
2. Reutilización de expresiones: Guardar cálculos intermedios complejos en 
   variables descriptivas para mejorar la legibilidad y evitar redundancias.
3. Validación previa: Verificar la validez de los rangos (como sueldos o horas 
   no negativas) e ingresos mayores a cero antes de realizar operaciones matemáticas.
4. Nomenclatura limpia y descriptiva: Emplear variables en 'lower_snake_case', 
   constantes en 'UPPER_SNAKE_CASE' y mensajes de salida claros en inglés.
5. Interpretación transparente de booleanos: Documentar explícitamente qué representa 
   'true' y 'false' en las decisiones de negocio del programa.
==============================================================================
"""

# ==============================================================================
# PROBLEMA 1: Conversor de temperatura y bandera de rango
# ==============================================================================

"""
Problem 1: Temperature converter and range flag
Descripción:
    Convierte una temperatura ingresada en grados Celsius (float) a las escalas
    Fahrenheit y Kelvin. Adicionalmente, determina un valor booleano 'is_high_temperature'
    que es True si la temperatura en Celsius es mayor o igual a 30.0 °C.

Entradas:
    - temp_c (float): Temperatura expresada en grados Celsius.

Salidas:
    - "Fahrenheit:" <temp_f>
    - "Kelvin:" <temp_k>
    - "High temperature:" true|false

Validaciones:
    - Comprobar que temp_c se pueda convertir a flotante.
    - Rechazar temperaturas por debajo del cero absoluto físico (-273.15 °C o 0.0 K).

Casos de prueba:
    1) Normal: temp_c = 42.5 -> Fahrenheit: 108.5, Kelvin: 315.65, High temperature: true
    2) Borde: temp_c = 30.0 -> Fahrenheit: 86.0, Kelvin: 303.15, High temperature: true
    3) Error: temp_c = -350.0 -> Error: invalid input
"""

ABSOLUTE_ZERO_CELSIUS = -273.15
HIGH_TEMP_THRESHOLD = 30.0

def convert_temperature(temp_c_input) -> None:
    try:
        temp_c = float(temp_c_input)
    except (ValueError, TypeError):
        print("Error: invalid input")
        return

    if temp_c < ABSOLUTE_ZERO_CELSIUS:
        print("Error: invalid input")
        return

    temp_f = (temp_c * 9 / 5) + 32
    temp_k = temp_c + 273.15
    is_high_temperature = temp_c >= HIGH_TEMP_THRESHOLD

    print(f"Fahrenheit: {round(temp_f, 2)}")
    print(f"Kelvin: {round(temp_k, 2)}")
    print(f"High temperature: {str(is_high_temperature).lower()}")


# ==============================================================================
# PROBLEMA 2: Horas trabajadas y pago de horas extra
# ==============================================================================

"""
Problem 2: Work hours and overtime payment
Descripción:
    Calcula el sueldo semanal bruto de un trabajador a partir de las horas trabajadas 
    y su tarifa horaria. Las primeras 40 horas se pagan a tarifa normal; las horas 
    adicionales (> 40) se pagan al 150% de la tarifa normal. Determina además si 
    hubo horas extra mediante la bandera 'has_overtime'.

Entradas:
    - hours_worked (float): Total de horas laboradas en la semana.
    - hourly_rate (float): Pago por hora normal.

Salidas:
    - "Regular pay:" <regular_pay>
    - "Overtime pay:" <overtime_pay>
    - "Total pay:" <total_pay>
    - "Has overtime:" true|false

Validaciones:
    - hours_worked >= 0.0
    - hourly_rate > 0.0

Casos de prueba:
    1) Normal: hours_worked = 48.0, hourly_rate = 12.5 -> Regular: 500.0, Overtime: 150.0, Total: 650.0, Has overtime: true
    2) Borde: hours_worked = 40.0, hourly_rate = 18.0 -> Regular: 720.0, Overtime: 0.0, Total: 720.0, Has overtime: false
    3) Error: hours_worked = -10.0, hourly_rate = 15.0 -> Error: invalid input
"""

REGULAR_HOURS_LIMIT = 40.0
OVERTIME_MULTIPLIER = 1.5

def calculate_payroll(hours_worked_input, hourly_rate_input) -> None:
    try:
        hours_worked = float(hours_worked_input)
        hourly_rate = float(hourly_rate_input)
    except (ValueError, TypeError):
        print("Error: invalid input")
        return

    if hours_worked < 0.0 or hourly_rate <= 0.0:
        print("Error: invalid input")
        return

    regular_hours = min(hours_worked, REGULAR_HOURS_LIMIT)
    overtime_hours = max(0.0, hours_worked - REGULAR_HOURS_LIMIT)

    regular_pay = regular_hours * hourly_rate
    overtime_pay = overtime_hours * hourly_rate * OVERTIME_MULTIPLIER
    total_pay = regular_pay + overtime_pay
    has_overtime = hours_worked > REGULAR_HOURS_LIMIT

    print(f"Regular pay: {round(regular_pay, 2)}")
    print(f"Overtime pay: {round(overtime_pay, 2)}")
    print(f"Total pay: {round(total_pay, 2)}")
    print(f"Has overtime: {str(has_overtime).lower()}")


# ==============================================================================
# PROBLEMA 3: Elegibilidad de descuento con booleanos
# ==============================================================================

"""
Problem 3: Discount eligibility with booleans
Descripción:
    Evalúa si un cliente es elegible para recibir un 10% de descuento en su compra.
    La regla otorga el descuento si el cliente es estudiante, adulto mayor o si 
    el monto total de la compra es mayor o igual a 1000.0.

Entradas:
    - purchase_total (float): Monto bruto de la compra.
    - is_student_text (string): "YES" o "NO".
    - is_senior_text (string): "YES" o "NO".

Salidas:
    - "Discount eligible:" true|false
    - "Final total:" <final_total>

Validaciones:
    - purchase_total >= 0.0
    - Normalizar textos de entrada a mayúsculas y validar que sean estrictamente "YES" o "NO".

Casos de prueba:
    1) Normal: purchase_total = 750.0, is_student = "YES", is_senior = "NO" -> Eligible: true, Final total: 675.0
    2) Borde: purchase_total = 1000.0, is_student = "NO", is_senior = "NO" -> Eligible: true, Final total: 900.0
    3) Error: purchase_total = -100.0, is_student = "NO", is_senior = "NO" -> Error: invalid input
"""

DISCOUNT_RATE = 0.10
MIN_PURCHASE_FOR_DISCOUNT = 1000.0

def evaluate_discount(purchase_total_input, is_student_text: str, is_senior_text: str) -> None:
    try:
        purchase_total = float(purchase_total_input)
    except (ValueError, TypeError):
        print("Error: invalid input")
        return

    if purchase_total < 0.0:
        print("Error: invalid input")
        return

    student_clean = str(is_student_text).strip().upper()
    senior_clean = str(is_senior_text).strip().upper()

    if student_clean not in ["YES", "NO"] or senior_clean not in ["YES", "NO"]:
        print("Error: invalid input")
        return

    is_student = (student_clean == "YES")
    is_senior = (senior_clean == "YES")

    discount_eligible = is_student or is_senior or (purchase_total >= MIN_PURCHASE_FOR_DISCOUNT)
    
    if discount_eligible:
        final_total = purchase_total * (1.0 - DISCOUNT_RATE)
    else:
        final_total = purchase_total

    print(f"Discount eligible: {str(discount_eligible).lower()}")
    print(f"Final total: {round(final_total, 2)}")


# ==============================================================================
# PROBLEMA 4: Estadísticas básicas de tres números enteros
# ==============================================================================

"""
Problem 4: Basic statistics of three integers
Descripción:
    Toma tres valores enteros y calcula su suma, promedio (float), valor máximo, 
    valor mínimo y determina mediante el booleano 'all_even' si los tres son pares.

Entradas:
    - n1 (int): Primer número entero.
    - n2 (int): Segundo número entero.
    - n3 (int): Tercer número entero.

Salidas:
    - "Sum:" <sum_value>
    - "Average:" <average_value>
    - "Max:" <max_value>
    - "Min:" <min_value>
    - "All even:" true|false

Validaciones:
    - Verificar que los tres datos de entrada puedan convertirse a int.

Casos de prueba:
    1) Normal: n1 = 6, n2 = 14, n3 = 22 -> Sum: 42, Average: 14.0, Max: 22, Min: 6, All even: true
    2) Borde: n1 = 0, n2 = 0, n3 = 0 -> Sum: 0, Average: 0.0, Max: 0, Min: 0, All even: true
    3) Error: n1 = "xyz", n2 = 8, n3 = 12 -> Error: invalid input
"""

def calculate_integer_stats(n1_input, n2_input, n3_input) -> None:
    try:
        n1 = int(n1_input)
        n2 = int(n2_input)
        n3 = int(n3_input)
    except (ValueError, TypeError):
        print("Error: invalid input")
        return

    sum_value = n1 + n2 + n3
    average_value = sum_value / 3.0
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

    print(f"Sum: {sum_value}")
    print(f"Average: {round(average_value, 2)}")
    print(f"Max: {max_value}")
    print(f"Min: {min_value}")
    print(f"All even: {str(all_even).lower()}")


# ==============================================================================
# PROBLEMA 5: Elegibilidad de préstamo (ingreso y relación de deuda)
# ==============================================================================

"""
Problem 5: Loan eligibility (income and debt ratio)
Descripción:
    Calcula la relación entre pagos de deuda e ingresos mensuales (debt_ratio)
    y determina la elegibilidad de un préstamo según las siguientes condiciones:
    - Ingreso mensual >= 8000.0
    - Relación de deuda <= 0.4 (40%)
    - Puntaje crediticio >= 650

Entradas:
    - monthly_income (float): Ingreso mensual bruto.
    - monthly_debt (float): Pagos mensuales de deudas.
    - credit_score (int): Puntaje del historial crediticio.

Salidas:
    - "Debt ratio:" <debt_ratio>
    - "Eligible:" true|false

Validaciones:
    - monthly_income > 0.0 (evita división entre cero).
    - monthly_debt >= 0.0
    - credit_score >= 0

Casos de prueba:
    1) Normal: monthly_income = 12500.0, monthly_debt = 2500.0, credit_score = 720 -> Debt ratio: 0.2, Eligible: true
    2) Borde: monthly_income = 8000.0, monthly_debt = 3200.0, credit_score = 650 -> Debt ratio: 0.4, Eligible: true
    3) Error: monthly_income = 0.0, monthly_debt = 1500.0, credit_score = 700 -> Error: invalid input
"""

MIN_INCOME_FOR_LOAN = 8000.0
MAX_DEBT_RATIO = 0.4
MIN_CREDIT_SCORE = 650

def evaluate_loan_eligibility(income_input, debt_input, score_input) -> None:
    try:
        monthly_income = float(income_input)
        monthly_debt = float(debt_input)
        credit_score = int(score_input)
    except (ValueError, TypeError):
        print("Error: invalid input")
        return

    if monthly_income <= 0.0 or monthly_debt < 0.0 or credit_score < 0:
        print("Error: invalid input")
        return

    debt_ratio = monthly_debt / monthly_income
    
    eligible = (
        monthly_income >= MIN_INCOME_FOR_LOAN and
        debt_ratio <= MAX_DEBT_RATIO and
        credit_score >= MIN_CREDIT_SCORE
    )

    print(f"Debt ratio: {round(debt_ratio, 2)}")
    print(f"Eligible: {str(eligible).lower()}")


# ==============================================================================
# PROBLEMA 6: Índice de Masa Corporal (BMI) y banderas de categoría
# ==============================================================================

"""
Problem 6: Body Mass Index (BMI) and category flag
Descripción:
    Calcula el Índice de Masa Corporal (BMI) según la fórmula peso / (estatura^2) 
    y clasifica el resultado en tres banderas booleanas independientes:
    'is_underweight' (< 18.5), 'is_normal' (18.5 <= BMI < 25.0) e 'is_overweight' (>= 25.0).

Entradas:
    - weight_kg (float): Peso corporal en kilogramos.
    - height_m (float): Estatura en metros.

Salidas:
    - "BMI:" <bmi_redondeado>
    - "Underweight:" true|false
    - "Normal:" true|false
    - "Overweight:" true|false

Validaciones:
    - weight_kg > 0.0
    - height_m > 0.0

Casos de prueba:
    1) Normal: weight_kg = 82.0, height_m = 1.80 -> BMI: 25.31, Underweight: false, Normal: false, Overweight: true
    2) Borde: weight_kg = 59.94, height_m = 1.80 -> BMI: 18.5, Underweight: false, Normal: true, Overweight: false
    3) Error: weight_kg = 82.0, height_m = -1.80 -> Error: invalid input
"""

BMI_UNDERWEIGHT_LIMIT = 18.5
BMI_OVERWEIGHT_LIMIT = 25.0

def calculate_bmi(weight_input, height_input) -> None:
    try:
        weight_kg = float(weight_input)
        height_m = float(height_input)
    except (ValueError, TypeError):
        print("Error: invalid input")
        return

    if weight_kg <= 0.0 or height_m <= 0.0:
        print("Error: invalid input")
        return

    bmi = weight_kg / (height_m ** 2)
    
    is_underweight = bmi < BMI_UNDERWEIGHT_LIMIT
    is_normal = (BMI_UNDERWEIGHT_LIMIT <= bmi < BMI_OVERWEIGHT_LIMIT)
    is_overweight = bmi >= BMI_OVERWEIGHT_LIMIT

    print(f"BMI: {round(bmi, 2)}")
    print(f"Underweight: {str(is_underweight).lower()}")
    print(f"Normal: {str(is_normal).lower()}")
    print(f"Overweight: {str(is_overweight).lower()}")


# ==============================================================================
# EJECUCIÓN PRINCIPAL / SUITE DE PRUEBAS
# ==============================================================================

if __name__ == "__main__":
    print("=== PROBLEMA 1 PRUEBAS ===")
    convert_temperature(42.5)        # Normal
    convert_temperature(30.0)        # Borde
    convert_temperature(-350.0)      # Error

    print("\n=== PROBLEMA 2 PRUEBAS ===")
    calculate_payroll(48.0, 12.5)    # Normal
    calculate_payroll(40.0, 18.0)    # Borde
    calculate_payroll(-10.0, 15.0)   # Error

    print("\n=== PROBLEMA 3 PRUEBAS ===")
    evaluate_discount(750.0, "YES", "NO")   # Normal
    evaluate_discount(1000.0, "NO", "NO")   # Borde
    evaluate_discount(-100.0, "NO", "NO")   # Error

    print("\n=== PROBLEMA 4 PRUEBAS ===")
    calculate_integer_stats(6, 14, 22)      # Normal
    calculate_integer_stats(0, 0, 0)        # Borde
    calculate_integer_stats("xyz", 8, 12)   # Error

    print("\n=== PROBLEMA 5 PRUEBAS ===")
    evaluate_loan_eligibility(12500.0, 2500.0, 720) # Normal
    evaluate_loan_eligibility(8000.0, 3200.0, 650)   # Borde
    evaluate_loan_eligibility(0.0, 1500.0, 700)      # Error

    print("\n=== PROBLEMA 6 PRUEBAS ===")
    calculate_bmi(82.0, 1.80)        # Normal
    calculate_bmi(59.94, 1.80)       # Borde
    calculate_bmi(82.0, -1.80)       # Error

"""
==============================================================================
CONCLUSIONES
==============================================================================
1. Los tipos enteros ('int') y flotantes ('float') interactúan de forma armónica 
   en aplicaciones reales; 'int' proporciona exactitud discreta mientras que 
   'float' aporta la flexibilidad decimal necesaria para cálculos científicos o financieros.
2. Las evaluaciones comparativas devuelven valores booleanos ('bool') que actúan 
   como interruptores de control, permitiendo estructurar decisiones claras (if/else).
3. Validar activamente las entradas evita que ocurran excepciones graves en tiempo 
   de ejecución, como el fallo por división entre cero ('ZeroDivisionError') o valores no físicos.
4. Combinar expresiones lógicas con 'and', 'or' y 'not' permite formalizar reglas 
   complejas de negocio de manera expresiva y compacta.
5. Estos patrones fundamentales se replican constantemente en sistemas reales de 
   nómina, motores de descuento, evaluación crediticia y procesamiento de datos biomédicos.
==============================================================================

==============================================================================
REFERENCIAS
==============================================================================
References:
1) Python Software Foundation. (2024). Built-in Types: Numeric Types — int, float. 
   Python Official Documentation. 
   https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

2) Python Software Foundation. (2024). Boolean Values — bool. 
   Python Official Documentation. 
   https://docs.python.org/3/library/stdtypes.html#boolean-values

3) Real Python. (2023). Python Booleans: Use Logical Operators and Compare Objects. 
   Real Python Tutorials. 
   https://realpython.com/python-boolean/

4) GeeksforGeeks. (2024). Python Data Types: int, float, and bool. 
   GeeksforGeeks Programming Guides. 
   https://www.geeksforgeeks.org/python-data-types/

5) W3Schools. (2024). Python Operators & Type Casting Guide. 
   W3Schools Online Web Tutorials. 
   https://www.w3schools.com/python/python_operators.asp
==============================================================================
"""