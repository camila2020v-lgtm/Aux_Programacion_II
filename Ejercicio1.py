# Clase Anime
class Anime:
    def __init__(self, nombre, genero, nroEpisodios):
        self.nombre = nombre
        self.genero = genero
        self.nroEpisodios = nroEpisodios
        self.episodios = []

    def __str__(self):
        return f"Anime: {self.nombre}, Género: {self.genero}, Episodios: {self.nroEpisodios}"

# Clase Televisor
class Televisor:
    def __init__(self, marca="", resolucion=0, tipo=""):
        self.marca = marca
        self.resolucion = resolucion
        self.tipo = tipo

    def __str__(self):
        return f"Televisor: Marca={self.marca}, Resolución={self.resolucion}p, Tipo={self.tipo}"

# Clase Instrumento
class Instrumento:
    def __init__(self, nombre, material, tipo):
        self.nombre = nombre
        self.material = material
        self.tipo = tipo

    def __str__(self):
        return f"Instrumento: {self.nombre}, Material={self.material}, Tipo={self.tipo}"

# Clase Principal
if __name__ == "__main__":

    # Crear 2 objetos Anime
    anime1 = Anime("School Days", "Romance/Drama", 12)
    anime2 = Anime("High School of the Dead", "Acción/Terror", 12)

    # Crear 2 objetos Televisor
    tv1 = Televisor("Samsung", 1080, "LED")
    tv2 = Televisor("LG", 4, "OLED")

    # Crear 2 objetos Instrumento
    inst1 = Instrumento("Guitarra", "Madera", "Cuerda")
    inst2 = Instrumento("Flauta", "Metal", "Aire")

    # Mostrar resultados
    print(anime1)
    print(anime2)

    print(tv1)
    print(tv2)

    print(inst1)
    print(inst2)
