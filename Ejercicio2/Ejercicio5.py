# Clase Jugador
class Jugador:
    def __init__(self, nombre, diamantes):
        self.nombre = nombre
        self.diamantes = diamantes
    # b) Calcular stacks
    def getStacks(self):
        return self.diamantes // 64
    
# Clase ServidorMinecraft
class ServidorMinecraft:
    def __init__(self):
        self.jugadores = []
    # a) Agregar jugador
    def agregarJugador(self, jugador):
        if len(self.jugadores) < 10:
            self.jugadores.append(jugador)
        else:
            print("Servidor lleno")
    # b) Mostrar stacks de cada jugador
    def mostrarStacks(self):
        for j in self.jugadores:
            print(j.nombre, "tiene", j.getStacks(), "stacks")
    # c) Jugador con más diamantes
    def jugadorMasDiamantes(self):
        mayor = self.jugadores[0]
        for j in self.jugadores:
            if j.diamantes > mayor.diamantes:
                mayor = j
        print("Jugador con mas diamantes:", mayor.nombre)

    # d) Total de diamantes
    def totalDiamantes(self):
        total = 0
        for j in self.jugadores:
            total += j.diamantes
        print("Total de diamantes:", total)

# Programa principal
if __name__ == "__main__":
    servidor = ServidorMinecraft()
    servidor.agregarJugador(Jugador("Alex",120))
    servidor.agregarJugador(Jugador("Steve",300))
    servidor.agregarJugador(Jugador("Juan",70))
    servidor.mostrarStacks()
    servidor.jugadorMasDiamantes()
    servidor.totalDiamantes()

