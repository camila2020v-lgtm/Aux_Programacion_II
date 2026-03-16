class Videojuego:
    def __init__(self, nombre="", plataforma="", jugadores=1):
        self.nombre = nombre
        self.plataforma = plataforma
        self.jugadores = jugadores

    def agregarJugadores(self, cantidad=None):
        if cantidad is None:
            self.jugadores = self.jugadores + 1
        else:
            self.jugadores = self.jugadores + cantidad

v1 = Videojuego("Tekken", "PlayStation", 1)
v2 = Videojuego("Metal Slug", "Arcade", 2)
v1.agregarJugadores()
cantidad = int(input("Ingrese cantidad de jugadores a agregar: "))
v2.agregarJugadores(cantidad)

print("\nVideojuego 1")
print("Nombre:", v1.nombre)
print("Plataforma:", v1.plataforma)
print("Jugadores:", v1.jugadores)

print("\nVideojuego 2")
print("Nombre:", v2.nombre)
print("Plataforma:", v2.plataforma)
print("Jugadores:", v2.jugadores)

