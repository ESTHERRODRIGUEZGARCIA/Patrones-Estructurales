# Patrones-Estructurales

Click [aquí](https://github.com/ESTHERRODRIGUEZGARCIA/Patrones-Estructurales.git) para ver el enlace del repositorio.

Trabajo hecho por:
1. [Esther Rodríguez García](https://github.com/ESTHERRODRIGUEZGARCIA)

## Ejercicio 1: Expansión del Sistema Integral de Pizzería "Delizioso" con Menús Personalizados y Almacenamiento en CSV utilizando los Patrones Builder y Composite

Contexto:

Tras el éxito inicial de su plataforma digital de creación y gestión de pizzas gourmet personalizadas, la cadena "Delizioso" desea llevar su propuesta al siguiente nivel. Ahora, aparte de permitir la personalización individual de pizzas, quiere ofrecer a sus clientes la posibilidad de combinar sus creaciones en menús personalizados, que podrían incluir entradas, bebidas, pizzas y postres. Estos menús pueden ser creados tanto por el cliente como por el equipo culinario de "Delizioso", con opciones preestablecidas que representan la esencia de la marca.

#### Objetivos:

1. Desarrollo de Menús Personalizados:
- Introducir la noción de un "menú", que puede contener varios elementos: entradas, bebidas, pizzas (que ya han sido definidas previamente con su sistema de creación de pizzas) y postres.
- Un "menú" puede ser simple (contener elementos básicos) o compuesto (incluir otros menús más pequeños, como un "Combo Pareja" que incluye dos menús individuales).
- Cada "menú" tendrá un código único y un precio, que se determina como la suma de los precios de sus elementos, con un descuento según la promoción aplicada.

2. Patrones de Diseño:
- Implementar el patrón Composite para modelar la relación entre los elementos y menús, facilitando la creación, modificación y cálculo de precios de menús compuestos.
- Continuar utilizando el patrón Builder para la creación detallada de las pizzas.

3. Interacción con CSV:
- Ampliar el sistema de almacenamiento en CSV para incluir los menús personalizados, de forma que se pueda registrar y recuperar la información de menús individuales y compuestos.
- Permitir que, a partir de un menú almacenado, se pueda reconstruir toda la estructura del menú con sus elementos individuales y precios.

4. Restricciones:
- Las librerías estándar de Python para la interacción con archivos CSV están permitidas.
- Se espera un diseño modular y orientado a objetos, con una clara separación de responsabilidades.
- La implementación del cálculo del precio de un "menú" debe hacerse en tiempo de ejecución y ser eficiente.

#### Entrega:

* Un diagrama UML detallando las clases, relaciones y métodos.
* Código Python correspondiente a la implementación.
* Un breve informe que justifique las decisiones de diseño tomadas y explique cómo se han aplicado los patrones de diseño.
* Un conjunto de pruebas unitarias que demuestren la correcta funcionalidad del sistema.

#### Rúbrica: Total: 30 puntos

1. Desarrollo de Menús Personalizados (9 puntos):
- Definición correcta de clases y estructuras para representar menús y elementos: 3 puntos
- Implementación correcta de menús simples y compuestos: 4 puntos
- Capacidad de calcular el precio de menús de forma adecuada, considerando descuentos y promociones: 2 puntos

2. Uso de Patrones de Diseño (8 puntos):
- Implementación adecuada del patrón Composite en la estructura de menús: 4 puntos
- Continuidad y coherencia en la utilización del patrón Builder para pizzas: 2 puntos
- Claridad y eficiencia en la integración de ambos patrones: 2 puntos

3. Interacción con CSV (7 puntos):
- Correcta implementación para almacenar menús en CSV, incluyendo todos los detalles relevantes: 3 puntos
- Capacidad de leer y reconstruir menús desde el CSV sin pérdida de información: 3 puntos
- Estructura clara y organizada del CSV: 1 punto

4. Diseño y Organización del Código (4 puntos):
- Modularidad y separación clara de responsabilidades en el código: 2 puntos
- Código limpio, bien comentado y fácil de seguir: 2 puntos

5. Informe y Justificación (1 punto):
- Claridad en la justificación de las decisiones de diseño tomadas: 0.5 puntos
- Explicación detallada de la aplicación de los patrones de diseño: 0.5 puntos

6. Pruebas Unitarias (1 punto):
- Existencia de pruebas unitarias que cubran casos básicos: 0.5 puntos
- Cobertura de casos de borde y validación de correcta funcionalidad en diferentes escenarios: 0.5 puntos


#### Observaciones Adicionales:

Se espera que los estudiantes muestren coherencia en el diseño y una clara comprensión de los conceptos aplicados.

El criterio del profesor/a puede ajustar los puntos basados en detalles específicos o criterios no mencionados explícitamente en esta rúbrica.



## Ejercicio 2: Sistema Avanzado de Gestión Documental del SAMUR-Protección Civil con Composite y Proxy

Contexto:

El SAMUR-Protección Civil, tras su proceso de digitalización, se enfrenta al reto de administrar una cantidad masiva de documentos digitales relacionados con sus activaciones y operaciones. Esta documentación no solo consiste en informes y registros, sino que también incluye imágenes, vídeos, audios y otros tipos de archivos multimedia. La necesidad de garantizar un acceso rápido pero seguro a esta información es esencial, especialmente cuando se trata de datos sensibles o confidenciales.

Enunciado del Problema:

1. Documentos: Estos son los archivos básicos en el sistema. Cada documento tiene un nombre, un tipo (texto, imagen, video, etc.) y un tamaño. El contenido de estos documentos puede ser accedido y modificado, pero para algunos documentos sensibles, es necesario llevar un registro de quién y cuándo se accede o modifica.

2. Enlaces (Links): Son referencias a otros documentos o carpetas en el sistema. No poseen contenido propio, pero ofrecen una forma rápida de acceder a la información referenciada. Su tamaño es simbólico, no correspondiente al tamaño real del archivo o carpeta al que apuntan.

3. Carpetas: Contenedores que albergan varios documentos, enlaces y otras carpetas. Su tamaño es la suma de los tamaños de todos los elementos contenidos. Se pueden expandir añadiendo más elementos en cualquier momento.

4. Proxy de Acceso: Para garantizar la seguridad y la trazabilidad en el acceso a los documentos, se implementará un proxy que actuará como intermediario. Este proxy registrará cada acceso o modificación a los documentos, especialmente aquellos que sean sensibles o confidenciales, y solo permitirá el acceso a usuarios autorizados.

#### Objetivos del Ejercicio:

- Utilizar el patrón de diseño Composite para modelar la estructura de documentos del sistema.
- Implementar el patrón Proxy para controlar y registrar el acceso a documentos específicos.
- Desarrollar en Python las clases y la lógica necesaria para representar y gestionar los documentos, enlaces y carpetas, garantizando la seguridad y trazabilidad mediante el uso del proxy.
- Implementar funciones que faciliten la navegación, creación, modificación y eliminación de elementos en el sistema.

#### Instrucciones:

- Diseñar un diagrama de clases que refleje la estructura propuesta, identificando las relaciones, interfaces y métodos esenciales.
- Implementar las clases en Python, asegurando buenas prácticas y la utilización adecuada de los patrones de diseño Composite y Proxy.
- Crear funciones que permitan navegar por la estructura, añadir documentos, modificar contenidos, eliminar elementos y acceder a través del Proxy.
- Desarrollar pruebas para validar la correcta implementación y comportamiento del sistema, especialmente en lo que respecta a la seguridad y registro de acceso a los documentos.

#### Rúbrica ejercicio 2: TOTAL: 70 puntos

1. Diagrama de clases: Subtotal: 15 puntos
- Precisión en la representación de relaciones y clases: 0-10 puntos.
- Inclusión de todos los elementos esenciales (documentos, enlaces, carpetas, proxy): 0-5 puntos.

2. Implementación en Python: Subtotal: 30 puntos
- Uso adecuado del patrón Composite para estructurar documentos: 0-10 puntos.
- Implementación correcta del patrón Proxy, incluyendo la funcionalidad de registro y control de acceso: 0-15 puntos.
- Calidad del código, buenas prácticas y legibilidad: 0-5 puntos.

3. Funciones y operaciones: Subtotal: 15 puntos
- Funcionalidad para navegar por la estructura: 0-5 puntos.
- Capacidad para añadir, modificar y eliminar documentos y carpetas: 0-5 puntos.
- Correcta interacción con el Proxy al intentar acceder a documentos sensibles: 0-5 puntos.

4. Pruebas y validación: Subtotal: 10 puntos
- Cobertura de escenarios clave y potenciales errores: 0-5 puntos.
- Correcta implementación y resultados esperados: 0-5 puntos.



Añadir a la pizzeria
combo con composite: n bebidas, n pizzas, n postres
crear tu combo: una bebida, una pizza ya predefinida, un postre
cada pedido es un token con un id

generar un id en el csv
base d e datos relacionr sql conectar con cualquiero orm(piramid) : básico flsh

Parte2:
hacer un registro: como se hace: se utilizan los logs (usuario, ontraseña...) vale con un txt pero mejor csv de quien ha acceido y eso.
(las url link)

libreria que nos hace el proxy y los registros: logging; log4python
generr crpetas que guarden ficheros donde hay que tener datos qu se acumplen. Cada doc va a tener un nombre. Base de datos jerarquizada. como hacer un json sin saber que es un json. JERARQUIA-> vamos a tener diccionaarios key value key value key value. 

