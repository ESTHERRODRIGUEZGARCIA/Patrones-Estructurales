# Patrones-Estructurales

Click [aquí](https://github.com/ESTHERRODRIGUEZGARCIA/Patrones-Estructurales.git) para ver el enlace del repositorio.

Trabajo hecho por:
1. [Esther Rodríguez García](https://github.com/ESTHERRODRIGUEZGARCIA)

## Ejercicio 1: Expansión del Sistema Integral de Pizzería "Delizioso" con Menús Personalizados y Almacenamiento en CSV utilizando los Patrones Builder y Composite

#### Objetivos:

1. Desarrollo de Menús Personalizados

2. Patrones de Diseño: Composite y Builder

3. Interacción con CSV

4. Restricciones

#### Entrega:

Informe: Implementación de Sistema de Pedido en Pizzería

El propósito de esta implementación es crear un sistema de pedido para una pizzería que permita a los clientes personalizar sus pizzas y seleccionar combos predefinidos.

Se ha aplicado el patrón de diseño Builder para la creación de pizzas personalizadas, lo que proporciona flexibilidad en la construcción de pizzas con ingredientes específicos. También se ha utilizado el patrón Composite para representar los distintos combos ofrecidos por la pizzería. La clase Combo actúa como un componente que puede contener tanto elementos individuales como otros combos, facilitando la gestión de estructuras complejas de combos.

Los datos del cliente y de los combos se almacenan en archivos CSV para garantizar la persistencia y la identificación única. Se ha asignado un identificador único a cada entrada utilizando la biblioteca uuid, asegurando la integridad de los datos y facilitando la recuperación.

La interfaz de usuario, desarrollada con PyQt5, ofrece una experiencia amigable para que los clientes seleccionen entre diferentes tipos de combos y personalicen sus pizzas. La modularidad del código facilita la extensión y el mantenimiento.

Conclusiones:

La implementación del sistema de pedido en la pizzería aprovecha patrones de diseño para lograr una estructura modular y extensible. La elección de almacenar datos en archivos CSV con identificadores únicos facilita la gestión y persistencia de la información del cliente. La interfaz de usuario proporciona una experiencia amigable para realizar pedidos eficientemente.



## Ejercicio 2: Sistema Avanzado de Gestión Documental del SAMUR-Protección Civil con Composite y Proxy


#### Entrega

En este ejercicio, se abordaron diversos objetivos centrados en la aplicación de patrones de diseño en Python para modelar una estructura de documentos y garantizar la seguridad mediante el uso del patrón Proxy. Se implementó el patrón Composite para diseñar una jerarquía de clases que representan documentos, enlaces y carpetas, permitiendo la manipulación de la estructura de manera eficiente. Además, se empleó el patrón Proxy para controlar y registrar el acceso a documentos específicos, añadiendo una capa de seguridad y trazabilidad.

La implementación del sistema incluyó la creación de funciones que facilitan la navegación, creación, y eliminación de elementos en la estructura. Se diseñó un mecanismo de autenticación de usuarios, con registro y acceso seguro mediante contraseñas. Se utilizaron funciones específicas para cargar y guardar la información de usuarios en un archivo CSV.

Además, se cumplió con la tarea de desarrollar pruebas que validan la implementación correcta y el comportamiento seguro del sistema. Se diseñó un menú interactivo que permite a los usuarios autenticados realizar diversas acciones, asegurando la coherencia y seguridad de las operaciones. En resumen, el ejercicio logró integrar de manera efectiva los patrones de diseño Composite y Proxy, ofreciendo un sistema robusto y seguro para la gestión de documentos.



