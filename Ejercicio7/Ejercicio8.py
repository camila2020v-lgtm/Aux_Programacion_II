class SueldoInvalidoException(Exception):
    pass
class CargoInvalidoException(Exception):
    pass
class Empleado:
    def __init__(self, nombre, cargo, sueldo):
        self.nombre = nombre
        self.cargo = cargo
        self.sueldo = sueldo
    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Cargo:", self.cargo)
        print("Sueldo:", self.sueldo, "Bs")
class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []
    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)
    def mostrar_empleados(self):
        print("\nEMPRESA:", self.nombre)
        for e in self.empleados:
            print("-------------------")
            e.mostrar()
empresa = Empresa("Empresa Bolivia")
n = int(input("Cantidad de empleados: "))
for i in range(n):
    print("\nEmpleado", i + 1)
    nombre = input("Nombre: ")
    while True:
        try:
            cargo = input("Cargo: ")
            if any(c.isdigit() for c in cargo):
                raise CargoInvalidoException
            break
        except CargoInvalidoException:
            print("Error: el cargo solo debe contener letras.")
    sueldo = float(input("Sueldo: "))
    try:
        if sueldo < 2500:
            raise SueldoInvalidoException
    except SueldoInvalidoException:
        print("Sueldo inválido.")
        print("Se asignaron automáticamente 2500 Bs.")
        sueldo = 2500
    empleado = Empleado(nombre, cargo, sueldo)
    empresa.agregar_empleado(empleado)
empresa.mostrar_empleados()

