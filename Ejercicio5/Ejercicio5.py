class Animal:
    def __init__(self, nombre, edad, duenio):
        self.nombre = nombre
        self.edad = edad
        self.duenio = duenio

class Perro(Animal):
    def __init__(self, nombre, edad, duenio):
        super().__init__(nombre, edad, duenio)

class Gato(Animal):
    def __init__(self, nombre, edad, duenio, tomaLeche):
        super().__init__(nombre, edad, duenio)
        self.tomaLeche = tomaLeche

class Veterinaria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.perros = [None] * 100
        self.gatos = [None] * 100
        self.cantPerros = 0
        self.cantGatos = 0

    def agregarPerro(self, perro):
        if self.cantPerros < 100:
            self.perros[self.cantPerros] = perro
            self.cantPerros += 1

    def agregarGato(self, gato):
        if self.cantGatos < 100:
            self.gatos[self.cantGatos] = gato
            self.cantGatos += 1

    def ordenarPerros(self):
        lista = self.perros[:self.cantPerros]
        lista.sort(key=lambda p: (p.edad, p.duenio, p.nombre))

        for i in range(self.cantPerros):
            self.perros[i] = lista[i]

    def ordenarGatos(self):
        lista = self.gatos[:self.cantGatos]
        lista.sort(key=lambda g: (-g.tomaLeche, -g.edad, g.nombre))

        for i in range(self.cantGatos):
            self.gatos[i] = lista[i]

    def contarDuenios(self):
        conteo = {}

        for i in range(self.cantPerros):
            p = self.perros[i]
            conteo[p.duenio] = conteo.get(p.duenio, 0) + 1

        for i in range(self.cantGatos):
            g = self.gatos[i]
            conteo[g.duenio] = conteo.get(g.duenio, 0) + 1

        for duenio, cantidad in conteo.items():
            if cantidad > 1:
                print(duenio, "tiene", cantidad, "animales")

v1 = Veterinaria("Veterinaria Central")
v2 = Veterinaria("Veterinaria Norte")

v1.agregarPerro(Perro("Max", 3, "Ana"))
v1.agregarPerro(Perro("Rocky", 3, "Luis"))
v1.agregarPerro(Perro("Bobby", 3, "Ana"))

v1.agregarGato(Gato("Michi", 2, "Ana", True))
v1.agregarGato(Gato("Pelusa", 5, "Luis", True))
v1.agregarGato(Gato("Nina", 4, "Carlos", False))

v2.agregarPerro(Perro("Firulais", 2, "Mario"))
v2.agregarPerro(Perro("Toby", 5, "Mario"))

v2.agregarGato(Gato("Luna", 1, "Mario", True))
v2.agregarGato(Gato("Sol", 6, "Pedro", False))

v1.ordenarPerros()
print("Perros:")

for i in range(v1.cantPerros):
    p = v1.perros[i]
    print(p.nombre, "-", p.edad, "años - Dueño:", p.duenio)

v1.ordenarGatos()
print("\nGatos:")

for i in range(v1.cantGatos):
    g = v1.gatos[i]

    if g.tomaLeche:
        estado = "Sí toma leche"
    else:
        estado = "No toma leche"

    print(g.nombre, "-", g.edad, "años -", estado)

print("\nDueños con más de un animal:")
v1.contarDuenios()

