class Persona:
    def __init__(self, nombre, carnet, edad):
        self._nombre = nombre
        self._carnet = carnet
        self._edad = edad

    def mostrar(self):
        print("Nombre:", self._nombre)
        print("Carnet:", self._carnet)
        print("Edad:", self._edad)


class Estudiante(Persona):
    def __init__(self, nombre, carnet, edad, matricula, carrera):
        super().__init__(nombre, carnet, edad)
        self._matricula = matricula
        self._carrera = carrera

    def mostrar(self):
        super().mostrar()
        print("Matricula:", self._matricula)
        print("Carrera:", self._carrera)

    def misma_carrera(self, otro):
        return self._carrera == otro._carrera


class Docente(Persona):
    def __init__(self, nombre, carnet, edad, antiguedad, sueldo):
        super().__init__(nombre, carnet, edad)
        self._antiguedad = antiguedad
        self._sueldo = sueldo

    def mostrar(self):
        super().mostrar()
        print("Antiguedad:", self._antiguedad)
        print("Sueldo:", self._sueldo)

e1 = Estudiante("Ana", 111, 20, 1001, "Sistemas")
e2 = Estudiante("Luis", 222, 25, 1002, "Industrial")
d1 = Docente("Carlos", 333, 25, 10, 5000)

print("\n ESTUDIANTE 1 ")
e1.mostrar()

print("\n ESTUDIANTE 2 ")
e2.mostrar()

print("\n DOCENTE ")
d1.mostrar()


print("\n VERIFICAR EDAD ")

if e1._edad == d1._edad:
    print("El estudiante 1 tiene la misma edad que el docente")

if e2._edad == d1._edad:
    print("El estudiante 2 tiene la misma edad que el docente")


print("\n VERIFICAR CARRERA ")

if e1.misma_carrera(e2):
    print("Ambos estudiantes son de la misma carrera")
else:
    print("Los estudiantes son de diferentes carreras")
