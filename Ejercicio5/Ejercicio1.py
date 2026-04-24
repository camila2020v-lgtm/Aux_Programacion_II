class Libro:
    def __init__(self, nombre, autor, anio):
        self.nombre = nombre
        self.autor = autor
        self.anio = anio

    def mostrar(self):
        print("Libro:", self.nombre, "| Autor:", self.autor, "| Año:", self.anio)

class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cantLibros = 0
        self.libros = [None] * 100

    def agregarLibro(self, libro):
        self.libros[self.cantLibros] = libro
        self.cantLibros += 1

    def buscarLibro(self, nombre):
        for i in range(self.cantLibros):
            if self.libros[i].nombre.lower() == nombre.lower():
                print("Libro encontrado en", self.nombre)
                self.libros[i].mostrar()
                return True
        return False

b1 = Biblioteca("Biblioteca Central")
b2 = Biblioteca("Biblioteca Oscura")

import time
modo = int(time.time()) % 2

if modo == 0:
    b1.agregarLibro(Libro("It", "Stephen King", 1986))
    b1.agregarLibro(Libro("El Resplandor", "Stephen King", 1977))

    b2.agregarLibro(Libro("Dracula", "Bram Stoker", 1897))
    b2.agregarLibro(Libro("Frankenstein", "Mary Shelley", 1818))
else:
    b1.agregarLibro(Libro("It", "Stephen King", 1986))
    b1.agregarLibro(Libro("El Resplandor", "Stephen King", 1977))
    b1.agregarLibro(Libro("Carrie", "Stephen King", 1974))

    b2.agregarLibro(Libro("Dracula", "Bram Stoker", 1897))

nombre_buscar = input("Libro: ")

encontrado = b1.buscarLibro(nombre_buscar)
if not encontrado:
    encontrado = b2.buscarLibro(nombre_buscar)

if not encontrado:
    print("No encontrado")

if b1.cantLibros > b2.cantLibros:
    print("Gana:", b1.nombre)
elif b2.cantLibros > b1.cantLibros:
    print("Gana:", b2.nombre)
else:
    print("Empate")
