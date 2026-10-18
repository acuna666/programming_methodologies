# Investigación sobre Tipos de Robots Móviles

## 1. Conceptos básicos

*   *¿Qué es un robot móvil?:* Es un sistema autónomo o semiautónomo capaz de desplazarse a través de su entorno físico utilizando un sistema de locomoción (como ruedas, orugas o patas), en lugar de estar anclado a un solo lugar.
*   *¿Qué diferencia existe entre un robot móvil y un robot manipulador fijo?:* La diferencia principal radica en su movilidad y espacio de trabajo. Un robot manipulador fijo está montado sobre una base estática y solo puede alcanzar los objetos dentro de su radio de acción limitado. En cambio, un robot móvil puede trasladarse por diferentes áreas, ampliando de forma ilimitada su espacio de operación y aplicación.
*   *¿Qué función cumple el sistema de locomoción de un robot?:* Su función es proveer la capacidad de movimiento y desplazamiento controlado al robot, permitiéndole interactuar dinámicamente con su entorno físico y superar traslados de un punto a otro.
*   *¿Qué significa que un robot tenga movilidad omnidireccional?:* Significa que el robot puede moverse de manera simultánea e independiente en cualquier dirección del plano horizontal (adelante, atrás, de lado o en diagonal) y girar sobre su propio eje sin necesidad de cambiar la orientación de su chasis previamente.
*   *¿Qué relación existe entre la disposición de las ruedas y los movimientos que puede realizar el robot?:* La geometría y la orientación de las ruedas determinan directamente los grados de libertad del robot. Dependiendo de cómo estén colocadas, el mecanismo limitará o facilitará ciertos movimientos, permitiendo giros cerrados, desplazamientos laterales o movimientos coordinados complejos.

---

## 2. Robot diferencial con rueda de castor

Esta configuración utiliza dos ruedas motrices independientes montadas sobre un mismo eje central y una o más ruedas de castor (locas) para mantener el equilibrio y la estabilidad del robot.

*   *Cómo están colocadas las ruedas motrices:* Se ubican de manera simétrica a los lados izquierdo y derecho del chasis, cada una accionada por su propio motor de forma independiente.
*   *Para qué sirve la rueda de castor o rueda loca:* Sirve como soporte mecánico pasivo para evitar que el robot se incline o caiga, permitiendo que rote libremente en cualquier dirección sin oponer resistencia al movimiento de las ruedas principales.
*   *Cómo avanza el robot en línea recta:* Ambas ruedas motrices giran hacia adelante a la misma velocidad y dirección exacta.
*   *Cómo puede girar hacia la izquierda o hacia la derecha:* Para girar a la izquierda, la rueda derecha gira más rápido que la izquierda (o la izquierda retrocede mientras la derecha avanza). Para girar a la derecha, ocurre lo inverso.
*   *Qué sucede cuando una rueda gira más rápido que la otra:* El robot realiza un giro curvo hacia el lado de la rueda que se mueve más lento o se detiene.
*   *Cómo puede realizar un giro sobre su propio eje:* Una rueda gira hacia adelante y la otra gira hacia atrás a la misma velocidad, provocando que el robot rote sobre su centro sin desplazarse linealmente.
*   *Ventajas de esta configuración:* Mecánicamente es muy sencilla de construir, económica, fácil de controlar mediante código y requiere pocos componentes electrónicos.
*   *Limitaciones:* No posee movilidad omnidireccional; para cambiar de dirección lateralmente requiere realizar maniobras de avance y retroceso (como un automóvil convencional).
*   *Aplicaciones donde se utiliza:* Robots aspiradoras domésticas, plataformas educativas de aprendizaje, vehículos de guía automática (AGV) simples en almacenes.

### Movimientos del robot diferencial:
*   Rueda izquierda Avanza - Rueda derecha Avanza = Movimiento: *Avanza*
*   Rueda izquierda Detenida - Rueda derecha Avanza = Movimiento: *Gira a la izquierda / Curva*
*   Rueda izquierda Avanza - Rueda derecha Detenida = Movimiento: *Gira a la derecha / Curva*
*   Rueda izquierda Avanza - Rueda derecha Retrocede = Movimiento: *Giro sobre su propio eje (en sentido horario)*
*   Rueda izquierda Retrocede - Rueda derecha Avanza = Movimiento: *Giro sobre su propio eje (en sentido antihorario)*
*   Rueda izquierda Retrocede - Rueda derecha Retrocede = Movimiento: *Retrocede*

---

## 3. Robots omnidireccionales con ruedas Omni

### Funcionamiento y características generales:
*   *Cómo está construida:* Es una rueda convencional que cuenta con una serie de pequeños rodillos libres montados de forma perpendicular a lo largo de toda su circunferencia exterior.
*   *Para qué sirven los pequeños rodillos colocados alrededor de la rueda:* Permiten que la rueda ruede libremente en su dirección principal impulsada por el motor, pero también facilitan que ruede pasivamente de manera lateral gracias a la rotación de los rodillos.
*   *En qué dirección puede generar fuerza la rueda:* Genera fuerza de empuje únicamente en la dirección en la que apunta la rueda motriz; los movimientos laterales ocurren por la libertad de giro pasivo de los rodillos.
*   *Por qué puede deslizarse libremente en otra dirección:* Debido a que los rodillos giran sin fricción significativa en el eje transversal al giro principal del motor.
*   *Cómo esta característica permite generar movimientos que una rueda convencional no puede realizar:* Permite que vectores de fuerza de múltiples ruedas se combinen para lograr un desplazamiento lateral o en diagonal sin necesidad de girar físicamente el chasis del robot.

### Configuración de tres ruedas:
*   *Cómo se distribuyen normalmente las ruedas alrededor del robot:* Se colocan formando un triángulo simétrico, separadas a 120 grados una de otra alrededor del centro del chasis.
*   *Orientación aproximada entre ellas:* Cada rueda apunta hacia afuera formando ángulos equidistantes de 120°.
*   *Cómo puede desplazarse lateralmente y en diagonal:* Variando la velocidad relativa de las tres ruedas, se generan fuerzas vectoriales que desplazan el robot en cualquier ángulo plano.
*   *Cómo puede girar sobre su propio eje:* Haciendo que las tres ruedas giren de manera coordinada en la misma dirección circunferencial (horaria o antihoraria).
*   *Qué sucede cuando las tres ruedas giran a diferentes velocidades:* El robot se desplaza en una dirección resultante vectorial combinada mientras ajusta su orientación de giro de manera simultánea.

---

## 4. Robot omnidireccional con ruedas Mecanum

*   *Cómo están construidas:* Son similares a las ruedas Omni, pero sus rodillos periféricos están montados en un ángulo de 45 grados respecto al plano de rotación de la rueda principal.
*   *Cómo están colocados sus rodillos:* Se disponen en un ángulo inclinado (usualmente a 45°), formando un patrón simétrico en el vehículo.
*   *Qué diferencia existe entre una rueda Mecanum y una rueda Omni convencional:* En la rueda Omni los rodillos rotan de forma perpendicular (90°) al plano de la rueda, mientras que en la Mecanum los rodillos están inclinados a 45°, lo que permite descomponer fuerzas longitudinales en fuerzas laterales directas con mayor eficiencia de tracción.
*   *Por qué generalmente se utilizan cuatro ruedas:* Se implementa una configuración de cuatro ruedas para equilibrar las fuerzas diagonales generadas por los rodillos inclinados y lograr un control omnidireccional completo y estable.
*   *Cómo deben orientarse las ruedas respecto al chasis:* Deben montarse formando una configuración de "X" o diamante, asegurando que los rodillos apunten hacia el centro o hacia afuera según el diseño cinemático requerido.

### Combinación de movimientos de las cuatro ruedas:
*   *Avance:* Las cuatro ruedas giran hacia adelante a la misma velocidad.
*   *Retroceso:* Las cuatro ruedas giran hacia atrás a la misma velocidad.
*   *Movimiento hacia la izquierda:* Las ruedas delanteras izquierda y trasera derecha giran hacia adentro (opuestas), mientras que las delanteras derecha y trasera izquierda giran hacia afuera.
*   *Movimiento hacia la derecha:* Se invierte el sentido de rotación cruzado anterior.
*   *Movimiento diagonal:* Se combinan velocidades específicas en las ruedas opuestas para cancelar fuerzas en un eje y sumar vectores en el otro.
*   *Giro sobre el propio eje:* Las dos ruedas de un lado giran hacia adelante y las dos del lado opuesto giran hacia atrás.

---

## 5. Robot con dirección Ackermann

Investiga la geometría de dirección utilizada en automóviles y algunos robots móviles grandes[span_1](start_span)[span_1](end_span).

*   *Cómo se distribuyen las ruedas:* Cuenta con ruedas delanteras orientables conectadas a un mecanismo de dirección y ruedas traseras fijas que proporcionan la tracción principal.
*   *Qué ruedas normalmente proporcionan la dirección:* Las ruedas delanteras.
*   *Qué ruedas pueden proporcionar la tracción:* Generalmente las ruedas traseras (o las cuatro en sistemas de tracción integral).
*   *Por qué las ruedas interiores y exteriores no giran exactamente con el mismo ángulo durante una curva:* Debido a que la rueda interior recorre un radio de giro más pequeño que la rueda exterior, la geometría Ackermann asegura que ambas ruedas giren sobre un centro común sin derrapar.
*   *Qué es el radio de giro:* Es la distancia mínima en forma de circunferencia que necesita el vehículo para completar un giro completo de 360 grados.
*   *Por qué un vehículo Ackermann no puede desplazarse directamente hacia un costado:* Porque sus ruedas no tienen libertad lateral ni rodillos pasivos; depende totalmente del ángulo de orientación frontal para avanzar de forma curvilínea.
*   *Qué semejanzas tiene con la dirección de un automóvil convencional:* Es exactamente la misma geometría de dirección utilizada en los automóviles comerciales modernos.

---

## 6. Comparación de configuraciones

Tabla comparativa de los sistemas investigados[span_2](start_span)[span_2](end_span):

| Configuración | Número típico de ruedas | Movimiento lateral | Giro sobre su eje | Complejidad mecánica | Complejidad de control |
| :--- | :--- | :--- | :--- | :--- | :--- |
| *Diferencial + castor*[span_3](start_span)[span_3](end_span) | 2 motrices + 1 o más caster | No | Sí | Baja | Baja |
| *Omni de 3 ruedas*[span_4](start_span)[span_4](end_span) | 3 | Sí | Sí | Media | Media |
| *Omni de 4 ruedas*[span_5](start_span)[span_5](end_span) | 4 | Sí | Sí | Media | Media-Alta |
| *Mecanum*[span_6](start_span)[span_6](end_span) | 4 | Sí | Sí | Alta | Alta |
| *Ackermann*[span_7](start_span)[span_7](end_span) | 4 | No | Limitado | Alta | Media |

### Explicación de configuraciones ideales por caso:
*   *Robot pequeño para aprender programación y control:* Se prefiere la configuración *Diferencial + castor*, ya que su lógica matemática de control y su circuitería son muy sencillas de implementar en plataformas educativas[span_8](start_span)[span_8](end_span).
*   *Robot que necesita desplazarse dentro de un almacén con espacios reducidos:* Se recomienda una configuración *Omni o Mecanum*, ya que su movilidad omnidireccional les permite girar y transular en pasillos estrechos sin necesidad de hacer maniobras de reversa[span_9](start_span)[span_9](end_span).
*   *Plataforma que necesita moverse lateralmente sin cambiar su orientación:* La mejor opción es utilizar ruedas *Mecanum o Omni*, debido a su capacidad de traslación lateral pura[span_10](start_span)[span_10](end_span).
*   *Vehículo autónomo que debe circular de manera similar a un automóvil:* Se debe utilizar la dirección *Ackermann*, ya que está diseñada específicamente para altas velocidades y estabilidad en superficies viales reales[span_11](start_span)[span_11](end_span).
*   *Robot para una competencia donde sea necesario cambiar rápidamente de dirección:* Las configuraciones omnidireccionales (*Mecanum u Omni*) son ideales por su agilidad y capacidad de respuesta vectorial inmediata[span_12](start_span)[span_12](end_span).
*   *Robot móvil sencillo que utilice únicamente dos motores:* La configuración *Diferencial*, ya que cada motor controla una rueda de forma independiente sin requerir mecanismos de dirección adicionales[span_13](start_span)[span_13](end_span).

---

## 7. Análisis del movimiento

*   *Diferencial:* Para que el robot gire sobre su propio eje, las ruedas deben girar a la misma velocidad pero en direcciones opuestas (una hacia adelante y la otra hacia atrás), generando un momento de torsión neto sin desplazamiento lineal.
*   *Omni:* Los rodillos pequeños permiten que la rueda transmita fuerza únicamente en su dirección axial de giro, descomponiendo las fuerzas laterales de forma pasiva para que el robot pueda deslizarse en cualquier ángulo.
*   *Mecanum:* El robot puede desplazarse lateralmente porque la inclinación a 45° de los rodillos en las cuatro ruedas genera vectores de fuerza cruzados que se anulan en el eje longitudinal y se suman en el eje transversal.
*   *Ackermann:* El vehículo necesita avanzar o retroceder para cambiar de posición lateral o de orientación porque sus ruedas son rígidas y no pueden deslizarse de manera transversal al plano de rodadura sin generar fricción estática severa.

---

## 8. Aplicación en un robot real

*   *Nombre del robot:* Kiva System (actualmente operado como Amazon Robotics).
*   *Fabricante o institución que lo desarrolló:* Kiva Systems (adquirido por Amazon).
*   *Tipo de locomoción:* Robot móvil con tracción diferencial y ruedas de soporte estabilizadoras.
*   *Número y tipo de ruedas:* Dos ruedas motrices centrales y múltiples ruedas locas de apoyo para equilibrar la plataforma de carga.
*   *Sensors principales:* Sistemas de visión cenital, sensores de proximidad infrarrojos y lectores de códigos de barras en el suelo para geolocalización.
*   *Actuadores utilizados para el movimiento:* Motores de corriente directa (DC) sin escobillas con reductores de alta precisión y un mecanismo de elevación interno accionado por husillo.
*   *Aplicación del robot:* Automatización del transporte de estanterías completas de mercancía dentro de los centros de cumplimiento y distribución logística de Amazon.

---

## Reflexión final

*   *¿Qué configuración te pareció más sencilla de comprender?:* La configuración diferencial con rueda de castor, ya que su principio físico es idéntico al de mover un carrito manual aplicando más fuerza de un lado que del otro.
*   *¿Qué ofrece mayor libertad de movimiento?:* Las configuraciones omnidireccionales con ruedas Mecanum y Omni, porque pueden moverse hacia cualquier punto cardinal de forma instantánea sin cambiar la orientación del chasis.
*   *¿Qué configuración utilizarías para construir tu primer robot móvil?:* Una configuración diferencial, debido a su accesibilidad económica, facilidad de armado mecánico y simplicidad en la programación de los motores.
*   *¿Por qué no existe una sola configuración de ruedas adecuada para todos los robots?:* Porque cada aplicación industrial, doméstica o de investigación prioriza necesidades distintas como velocidad, capacidad de carga, eficiencia energética, precisión de terreno o espacio operativo disponible.

---

## Referencias

*   Siegwart, R., Nourbakhsh, I. R., & Scaramuzza, D. (2011). Introduction to Autonomous Mobile Robots. MIT Press.
*   Craig, J. J. (2005). Robotics: Introduction to Control and Mechanics. Pearson Education.
*   Boston Dynamics. (2025). Documentación técnica de plataformas móviles y sistemas de locomoción. [https://www.bostondynamics.com](https://www.bostondynamics.com)
*