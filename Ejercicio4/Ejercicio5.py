import math
from abc import ABC, abstractmethod

class Figura(ABC):
    def __init__(self, color):
        self._color = color   # atributo protegido

    @abstractmethod
    def obtenerArea(self):
        pass

class Cuadrado(Figura):
    def __init__(self, color, lado):
        super().__init__(color)
        self._lado = lado

    def obtenerArea(self):
        return self._lado * self._lado

    def mostrar(self):
        print("Cuadrado - Color:", self._color, "Area:", self.obtenerArea())


class Triangulo(Figura):
    def __init__(self, color, lado1, lado2, lado3):
        super().__init__(color)
        self._lado1 = lado1
        self._lado2 = lado2
        self._lado3 = lado3

    def obtenerArea(self):

        s = (self._lado1 + self._lado2 + self._lado3) / 2
        return (s * (s - self._lado1) * (s - self._lado2) * (s - self._lado3)) ** 0.5

    def mostrar(self):
        print("Triangulo - Color:", self._color, "Area:", self.obtenerArea())


class Redondo(Figura):
    def __init__(self, color, radio):
        super().__init__(color)
        self._radio = radio

    def obtenerArea(self):
        return math.pi * self._radio ** 2

    def mostrar(self):
        print("Redondo - Color:", self._color, "Area:", self.obtenerArea())

c1 = Cuadrado("Rojo", 4)
c2 = Cuadrado("Azul", 5)

t1 = Triangulo("Verde", 3, 4, 5)
t2 = Triangulo("Amarillo", 5, 5, 6)

r1 = Redondo("Negro", 3)
r2 = Redondo("Blanco", 6)

print("\n FIGURAS")
c1.mostrar()
c2.mostrar()
t1.mostrar()
t2.mostrar()
r1.mostrar()
r2.mostrar()

print("\n MAYOR AREA")

if c1.obtenerArea() > t1.obtenerArea():
    print("El mayor es el CUADRADO de color:", c1._color)
else:
    print("El mayor es el TRIANGULO de color:", t1._color)

