# Clase Bus
class Bus:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.pasajeros = 0
    # a) Subir pasajeros al bus
    def subirPasajeros(self, x):
        self.pasajeros += x
        if self.pasajeros > self.capacidad:
            self.pasajeros = self.capacidad
        print("Pasajeros actuales:", self.pasajeros)
    # b) Cobrar pasaje
    def cobrarPasaje(self):
        costo = 1.50
        total = self.pasajeros * costo
        print("Total recaudado:", total, "bs")
    # c) Mostrar asientos disponibles
    def asientosDisponibles(self):
        disponibles = self.capacidad - self.pasajeros
        print("Asientos disponibles:", disponibles)
# d) Crear instancia del bus
if __name__ == "__main__":
    bus = Bus(40)
    bus.subirPasajeros(25)
    bus.cobrarPasaje()
    bus.asientosDisponibles()
