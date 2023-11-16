from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    """
    La clase Componente base declara operaciones comunes tanto para operaciones simples como
    Objetos complejos de una composición.
    """

    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        """
        Opcionalmente, el componente base puede declarar una interfaz para configurar y
        acceder a un padre del componente en una estructura de árbol. También puede
        proporcione alguna implementación predeterminada para estos métodos.
        """

        self._parent = parent

    """
    En algunos casos, sería beneficioso definir el concepto de gestión infantil.
    operaciones directamente en la clase Componente base. De esta manera, no necesitarás
    exponer cualquier clase de componente concreto al código del cliente, incluso durante el
    ensamblaje del árbol de objetos. La desventaja es que estos métodos estarán vacíos durante
    los componentes a nivel de hoja.
    """

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def is_composite(self) -> bool:
        """
        Puede proporcionar un método que permita al código del cliente determinar si un
        El componente puede tener hijos.
        """

        return False

    @abstractmethod
    def operation(self) -> str:
        """
        El componente base puede implementar algún comportamiento predeterminado o dejarlo en manos de
        clases concretas (declarando el método que contiene el comportamiento como
        "abstracto").
        """

        pass


class Leaf(Component):
    """
    La clase Leaf representa los objetos finales de una composición. una hoja no puede
    tener hijos.

    Por lo general, son los objetos Hoja los que hacen el trabajo real, mientras que los objetos Compuestos
    los objetos solo delegan en sus subcomponentes.
    """

    def operation(self) -> str:
        return "Leaf"


class Composite(Component):
    """
    La clase Composite representa los componentes complejos que pueden tener
    niños. Por lo general, los objetos compuestos delegan el trabajo real a sus
    niños y luego "resumir" el resultado.
    """

    def __init__(self) -> None:
        self._children: List[Component] = []

    """
    Un objeto compuesto puede agregar o eliminar otros componentes (tanto simples como
    complejo) hacia o desde su lista secundaria.
    """

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        """
        El Compuesto ejecuta su lógica primaria de una manera particular. Él
        atraviesa recursivamente a través de todos sus hijos, recopilando y sumando
        sus resultados. Dado que los hijos del compuesto pasan estas llamadas a sus
        hijos, etc., como resultado se recorre todo el árbol de objetos.
        """

        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Branch({'+'.join(results)})"


def client_code(component: Component) -> None:
    """
    El código del cliente funciona con todos los componentes a través de la interfaz base.
    """

    print(f"RESULT: {component.operation()}", end="")


def client_code2(component1: Component, component2: Component) -> None:
    """
    Gracias a que las operaciones de gestión de niños se declaran en el
    clase Component base, el código del cliente puede funcionar con cualquier componente, simple o
    complejos, sin depender de sus clases concretas.
    """

    if component1.is_composite():
        component1.add(component2)

    print(f"RESULT: {component1.operation()}", end="")


if __name__ == "__main__":
    # This way the client code can support the simple leaf components...
    simple = Leaf()
    print("Client: I've got a simple component:")
    client_code(simple)
    print("\n")

    # ...as well as the complex composites.
    tree = Composite()

    branch1 = Composite()
    branch1.add(Leaf())
    branch1.add(Leaf())

    branch2 = Composite()
    branch2.add(Leaf())

    tree.add(branch1)
    tree.add(branch2)

    print("Client: Now I've got a composite tree:")
    client_code(tree)
    print("\n")

    print("Client: I don't need to check the components classes even when managing the tree:")
    client_code2(tree, simple)