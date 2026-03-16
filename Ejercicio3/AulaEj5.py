class Aula:

    def __init__(self, nombreAula, piso):
        self.nombreAula = nombreAula
        self.piso = piso
        self.estudiantes = [
            ["Luis", 67],
            ["Aracely", 89]
        ]
    def mostrarDatos(self, tipo=None):
        if tipo is None:
            print("Nombre del aula:", self.nombreAula)
            print("Piso:", self.piso)
            print("\nEstudiantes y notas:")
            for e in self.estudiantes:
                print(e[0], "-", e[1])
        elif tipo == "estado":
            print("\nEstado de estudiantes:")
            for e in self.estudiantes:
                if e[1] >= 51:
                    print(e[0], "-", e[1], "- APROBADO")
                else:
                    print(e[0], "-", e[1], "- REPROBADO")

a1 = Aula("Aula 101", 1)

print("DATOS DEL AULA")
a1.mostrarDatos()

print("\nRESULTADOS")
a1.mostrarDatos("estado")

