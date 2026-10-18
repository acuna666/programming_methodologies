# Investigación sobre Sensores y Actuadores

## 1. Conceptos básicos

### ¿Qué es un sensor?
Es un dispositivo electrónico o mecánico diseñado para detectar cambios o magnitudes físicas en su entorno (como temperatura, luz, movimiento, presión) y convertirlos en una señal eléctrica u otra señal comprensible para un sistema de control.

### ¿Qué es un atuador?
Es un dispositivo capaz de recibir una señal de control (generalmente eléctrica) y transformarla en una acción física o mecánica sobre un entorno, como mover un objeto, abrir una válvula o generar calor.

### ¿Cuál es la diferencia entre un sensor y un actuador?
La diferencia principal radica en su función dentro del flujo de información y energía: el **sensor** mide o detecta el mundo físico y envía esa información al sistema (entrada), mientras que el **actuador** recibe órdenes del sistema y modifica o actúa sobre el mundo físico (salida).

### ¿Qué función tienen dentro de un sistema mecatrónico?
En un sistema mecatrónico, los sensores actúan como los "sentidos" al recopilar datos del entorno y del estado del sistema, permitiendo que la unidad de procesamiento tome decisiones. Por su parte, los actuadores funcionan como los "músculos", ejecutando las órdenes físicas necesarias para que el sistema cumpla con su objetivo automatizado.

**Ejemplo de un sistema sencillo:**
Una **puerta automática** de un centro comercial. 
* **Sensor:** Un sensor de presencia o de movimiento infrarrojo que detecta cuando una persona se acerca.
* **Actuador:** El motor eléctrico que abre y cierra las hojas de la puerta al recibir la señal del sensor.

---

## 2. Investigación de sensores

### • Temperatura
* **Qué variable detecta o mide:** El nivel de calor o frío del ambiente o de un objeto.
* **Principio básico de funcionamiento:** Utiliza componentes (como termistores o termopares) cuya resistencia eléctrica cambia en función de la temperatura.
* **Qué tipo de señal puede entregar:** Analógica o digital.
* **Un ejemplo de sensor comercial:** Termistor NTC o sensor LM35.
* **Una aplicación donde pueda utilizarse:** Sistemas de aire acondicionado y refrigeración.

### • Luz
* **Qué variable detecta o mide:** La intensidad luminosa o el brillo del entorno.
* **Principio básico de funcionamiento:** Emplea materiales fotorresistivos (como las Celdas LDR o fotodiodos) que varían su conductividad eléctrica al recibir fotones de luz.
* **Qué tipo de señal puede entregar:** Analógica o digital.
* **Un ejemplo de sensor comercial:** Fotorresistencia LDR o sensor BH1750.
* **Una aplicación donde pueda utilizarse:** Lámparas automáticas que se encienden de noche.

### • Proximidad
* **Qué variable detecta o mide:** La presencia o distancia de un objeto cercano sin necesidad de contacto físico.
* **Principio básico de funcionamiento:** Emite ondas (ultrasónicas, infrarrojas o campos magnéticos) y mide el tiempo o la alteración en el rebote al chocar con un objeto.
* **Qué tipo de señal puede entregar:** Digital o analógica.
* **Un ejemplo de sensor comercial:** Sensor ultrasónico HC-SR04.
* **Una aplicación donde pueda utilizarse:** Sistemas de reversa y estacionamiento en automóviles.

### • Presión
* **Qué variable detecta o mide:** La fuerza ejercida por un gas o líquido por unidad de área.
* **Principio básico de funcionamiento:** Utiliza elementos piezoeléctricos o membranas deformables que generan una señal eléctrica proporcional a la fuerza aplicada.
* **Qué tipo de señal puede entregar:** Analógica.
* **Un ejemplo de sensor comercial:** Transductor de presión MPX5700.
* **Una aplicación donde pueda utilizarse:** Monitoreo de presión en neumáticos o calderas industriales.

### • Posición
* **Qué variable detecta o mide:** La ubicación exacta o el ángulo de giro de un componente mecánico.
* **Principio básico de funcionamiento:** Emplea principios ópticos, magnéticos o potenciómetros para registrar desplazamientos lineales o angulares.
* **Qué tipo de señal puede entregar:** Analógica o digital (como pulsos de un encoder).
* **Un ejemplo de sensor comercial:** Encoder óptico rotativo.
* **Una aplicación donde pueda utilizarse:** Control de posición en ejes de brazos robóticos.

### • Velocidad o movimiento
* **Qué variable detecta o mide:** La rapidez con la que se desplaza un objeto o la ocurrencia de movimiento en un área.
* **Principio básico de funcionamiento:** Calcula el cambio de posición de un objeto por unidad de tiempo (por efecto Doppler, óptico o inercial).
* **Qué tipo de señal puede entregar:** Digital (frecuencia de pulsos).
* **Un ejemplo de sensor comercial:** Sensor de efecto Hall o tacómetro.
* **Una aplicación donde pueda utilizarse:** Velocímetros de bicicletas y automóviles.

### • Fuerza o peso
* **Qué variable detecta o mide:** La carga o peso aplicado sobre una superficie.
* **Principio básico de funcionamiento:** Se basa en galgas extensiométricas que cambian su resistencia al estirarse o comprimirse bajo una carga.
* **Qué tipo de señal puede entregar:** Analógica (generalmente requiere amplificación).
* **Un ejemplo de sensor comercial:** Celda de carga (Load Cell).
* **Una aplicación donde pueda utilizarse:** Básculas digitales industriales o de cocina.

---

### Tabla resumen de sensores

| Tipo de sensor | Variable que mide | Principio de funcionamiento | Ejemplo | Aplicación |
| :--- | :--- | :--- | :--- | :--- |
| **Temperatura** | Calor / Frío | Cambio de resistencia por temperatura | Sensor LM35 | Climatización |
| **Luz** | Intensidad luminosa | Variación de conductividad por fotones | Celda LDR | Alumbrado público |
| **Proximidad** | Distancia sin contacto | Rebote de ondas ultrasónicas/infrarrojas | HC-SR04 | Sensores de reversa |
| **Presión** | Fuerza de fluidos por área | Deformación de membrana piezoeléctrica | MPX5700 | Control industrial |
| **Posición** | Ubicación / Ángulo | Lectura óptica o magnética de desplazamiento | Encoder óptico | Robótica |
| **Velocidad** | Rapidez de desplazamiento | Cálculo de cambio de posición por tiempo | Sensor de efecto Hall | Velocímetros |
| **Fuerza o peso** | Carga aplicada | Deformación física de galgas extensiométricas | Celda de carga | Básculas digitales |

---

## 3. Clasificación de sensores

### • Sensores analógicos y digitales
* **Analógicos:** Entregan una señal de salida continua que varía de forma proporcional a la magnitud medida (por ejemplo, de 0 a 5 volts).
* **Digitales:** Convierten la señal física en valores discretos, comúnmente en formato binario (ceros y unos o pulsos digitales).
* **Diferencia clave y criterio:** Los analógicos entregan un rango infinito de valores continuos que requieren un conversor para ser leídos por microcontroladores, mientras que los digitales entregan datos ya procesados en estados lógicos definidos.

### • Sensores de contacto y sin contacto
* **De contacto:** Requieren que el elemento sensor toque físicamente el objeto a medir (por ejemplo, un interruptor mecánico de límite o *limit switch*).
* **Sin contacto:** Detectan la variable a distancia mediante campos magnéticos, luz u ondas, sin fricción física (por ejemplo, un sensor ultrasónico).
* **Diferencia clave y criterio:** El desgaste mecánico; los de contacto sufren fricción y deterioro físico con el uso constante, mientras que los de sin contacto tienen mayor durabilidad operativa.

### • Sensores activos y pasivos
* **Activos:** Requieren una fuente externa de energía para generar la señal o excitar el fenómeno que miden (por ejemplo, un sensor ultrasónico que emite ondas).
* **Pasivos:** No necesitan una fuente de alimentación externa para generar su respuesta, ya que transforman directamente la energía física del entorno en electricidad (por ejemplo, un termopar).
* **Diferencia clave y criterio:** La necesidad de alimentación externa para operar y generar la medición.

---

## 4. Investigación de actuadores

### • Motor de corriente directa (DC)
* **Qué tipo de energía utiliza:** Eléctrica de corriente continua.
* **Qué movimiento produce:** Movimiento rotatorio continuo.
* **Cómo funciona de manera general:** Al aplicar corriente a sus bobinas internas, genera campos magnéticos que interactúan con imanes permanentes, haciendo girar el eje central.
* **Una ventaja:** Fácil control de velocidad variando el voltaje aplicado.
* **Una limitación:** Requiere mantenimiento debido al desgaste de las escobillas tradicionales.
* **Una aplicación real:** Motores de tracción en juguetes o ventiladores pequeños.

### • Servomotor
* **Qué tipo de energía utiliza:** Energía eléctrica (con un circuito de control interno).
* **Qué movimiento produce:** Movimiento rotatorio controlado con precisión en un ángulo específico (generalmente entre 0° y 180°).
* **Cómo funciona de manera general:** Recibe una señal de control codificada por ancho de pulso (PWM) que le indica la posición exacta a la que debe girar mediante un sistema de engranajes y retroalimentación interna.
* **Una ventaja:** Alta precisión en el posicionamiento angular.
* **Una limitación:** Su rango de giro suele estar limitado mecánicamente.
* **Una aplicación real:** Control de dirección en autos a escala o articulaciones de robots.

### • Motor paso a paso (Stepper)
* **Qué tipo de energía utiliza:** Energía eléctrica en pulsos secuenciales.
* **Qué movimiento produce:** Movimiento rotatorio dividido en incrementos discretos llamados "pasos".
* **Cómo funciona de manera general:** Su rotor gira en pasos precisos al energizar de forma secuencial las distintas bobinas del estator.
* **Una ventaja:** Excelente precisión para posicionamiento sin necesidad de sistemas de retroalimentación complejos.
* **Una limitación:** Tiende a perder fuerza si se sobrecarga y consume energía incluso cuando está detenido.
* **Una aplicación real:** Impresoras 3D y máquinas de corte CNC.

### • Solenoid (Solenoide)
* **Qué tipo de energía utiliza:** Energía eléctrica.
* **Qué movimiento produce:** Movimiento lineal de corto alcance (empuje o tracción).
* **Cómo funciona de manera general:** Al circular corriente por una bobina, se genera un campo magnético que atrae un émbolo metálico hacia su interior.
* **Una ventaja:** Respuesta rápida y diseño compacto y sencillo.
* **Una limitación:** Su carrera o distancia de movimiento es muy limitada.
* **Una aplicación real:** Seguros eléctricos de puertas de automóviles.

### • Cilindro neumático
* **Qué tipo de energía utiliza:** Energía neumática (aire comprimido).
* **Qué movimiento produce:** Movimiento lineal de avance y retroceso.
* **Cómo funciona de manera general:** La presión del aire comprimido ingresa a una de las cámaras del cilindro, empujando un pistón hacia adelante o hacia atrás.
* **Una ventaja:** Capacidad de generar grandes fuerzas de manera limpia y rápida.
* **Una limitación:** Requiere de compresores e infraestructura de aire acondicionado/presurizado.
* **Una aplicación real:** Líneas de ensamblaje industrial para empujar piezas.

### • Cilindro hidráulico
* **Qué tipo de energía utiliza:** Energía hidráulica (aceite a alta presión).
* **Qué movimiento produce:** Movimiento lineal de alta potencia.
* **Cómo funciona de manera general:** Utiliza un fluido incompresible (aceite) impulsado por una bomba para mover un pistón con una fuerza descomunal.
* **Una ventaja:** Capacidad para levantar cargas extremadamente pesadas.
* **Una limitación:** Sistema voluminoso y con riesgo de fugas de aceite.
* **Una aplicación real:** Brazos de excavadoras y maquinaria pesada.

---

### Tabla resumen de actuadores

| Actuador | Energía utilizada | Movimiento | Ventaja principal | Limitación principal | Aplicación real |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Motor DC** | Eléctrica DC | Rotatorio continuo | Fácil control de velocidad | Desgaste de escobillas | Ventiladores |
| **Servomotor** | Eléctrica + PWM | Rotatorio controlado (ángulos) | Alta precisión angular | Rango de giro limitado | Robótica |
| **Motor paso a paso** | Pulsos eléctricos | Rotatorio por pasos discretos | Posicionamiento exacto sin sensores extra | Pérdida de pasos por sobrecarga | Impresoras 3D |
| **Solenoide** | Eléctrica | Lineal corto | Respuesta muy rápida | Carrera de movimiento reducida | Chapas eléctricas |
| **Cilindro neumático** | Aire comprimido | Lineal | Fuerza limpia y ágil | Requiere compresor externo | Automatización de líneas |
| **Cilindro hidráulico** | Aceite a presión | Lineal de gran potencia | Fuerza de carga inmensa | Sistema complejo y propenso a fugas | Maquinaria pesada |

---

## 5. Comparación de actuadores

### • Motor DC vs. Servomotor
* **Diferencia:** El motor DC gira continuamente sin un control exacto de su posición final, mientras que el servomotor está diseñado para posicionarse con precisión milimétrica en un ángulo específico.
* **Situación de elección:** Elegiría un **servomotor** para controlar la dirección de un mecanismo que requiere una posición fija (como el timón de un robot), y un **motor DC** si solo necesito que una rueda ruede libremente y sin parar.
  * *Razón:* El servo incluye un sistema de control interno y retroalimentación que asegura la posición exacta, algo de lo carece un motor DC común.

### • Servomotor vs. Motor paso a paso
* **Diferencia:** El servomotor utiliza un sistema de control por lazo cerrado con realimentación para mantener una posición bajo carga, mientras que el motor paso a paso se mueve por incrementos fijos mediante lazo abierto contando los pulsos eléctricos enviados.
* **Situación de elección:** Elegiría un **motor paso a paso** para una impresora 3D donde se requiere un control milimétrico de avance capa por capa, y un **servomotor** para el control de alerones en un modelo a escala sometido a fuerzas externas variables.
  * *Razón:* El motor paso a paso es ideal para recorridos repetitivos y exactos sin carga excesiva, mientras que el servomotor compensa fuerzas externas activamente para no perder su posición.

### • Actuador neumático vs. Actuador hidráulico
* **Diferencia:** El neumático funciona con aire comprimido (ideal para fuerzas moderadas y velocidades altas de forma limpia), mientras que el hidráulico utiliza aceite a alta presión (ideal para fuerzas inmensas y cargas muy pesadas).
* **Situación de elección:** Elegiría un **actuador neumático** para una línea de empaque rápido donde se requiere empujar cajas ligeras limpiamente, y un **actuador hidráulico** para el brazo de una grúa que debe levantar toneladas de peso.
  * *Razón:* El aire comprimido es más ágil pero compresible y limitado en fuerza; el aceite hidráulico es incompresible, lo que le permite soportar cargas de alta potencia estructural.

---

## 6. Sensores y actuadores en un sistema real

**Sistema seleccionado:** Brazo robótico industrial.

* **Función que cumple:** Manipular, trasladar y posicionar piezas con precisión dentro de una línea de ensamblaje automatizada.

### Diagrama de relación (Mermaid)

```mermaid
graph TD
    A[PLC / Unidad de Control] -->|Señal de control| B(Servomotores / Actuadores)
    B -->|Movimiento mecánico| C[Entorno / Piezas]
    D[Sensores de Proximidad y Posición] -->|Retroalimentación de datos| A
