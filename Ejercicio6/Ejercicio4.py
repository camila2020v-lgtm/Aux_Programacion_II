class Mueble:
    def __init__(self, tipo, material):
        self.tipo = tipo
        self.material = material

class Habitacion:
    def __init__(self, nombre, tamanio):
        self.nombre = nombre
        self.tamanio = tamanio
        self.cantMuebles = 0
        self.muebles = [None]*100

    def agregarMueble(self, m):
        if self.cantMuebles < 100:
            self.muebles[self.cantMuebles] = m
            self.cantMuebles += 1

class Departamento:
    def __init__(self, nroPuerta, nroPiso):
        self.nroPuerta = nroPuerta
        self.nroPiso = nroPiso
        self.nroHab = 0
        self.hab = [None]*100

    def agregarHabitacion(self, nombre, tamanio):
        if self.nroHab < 100:
            self.hab[self.nroHab] = Habitacion(nombre, tamanio)
            self.nroHab += 1

    def totalMuebles(self):
        s = 0
        for i in range(self.nroHab):
            s += self.hab[i].cantMuebles
        return s

class Parqueo:
    def __init__(self, capacidad, precioH):
        self.capacidad = capacidad
        self.cantAuto = 0
        self.precioH = precioH
        self.parqueo = [""]*100

    def agregarAuto(self, placa):
        if self.cantAuto < self.capacidad:
            self.parqueo[self.cantAuto] = placa
            self.cantAuto += 1
            print("Se guardo:", placa)
        else:
            print("Parqueo lleno")


class Edificio:
    def __init__(self, nombre, superficie):
        self.nombre = nombre
        self.superficie = superficie
        self.cantDep = 0
        self.deps = [None]*100
        self.parqueo = None

    def agregarDep(self, d):
        if self.cantDep < 100:
            self.deps[self.cantDep] = d
            self.cantDep += 1

    def agregarParqueo(self, p):
        self.parqueo = p

ed = Edificio("Central", 500)
ed.agregarParqueo(Parqueo(2, 5))

d1 = Departamento(101, 1)
d1.agregarHabitacion("Sala", 20)
d1.agregarHabitacion("Cocina", 10)

d2 = Departamento(102, 1)
d2.agregarHabitacion("Sala", 25)

d3 = Departamento(201, 2)
d3.agregarHabitacion("Sala", 30)
d3.agregarHabitacion("Cuarto", 15)

ed.agregarDep(d1)
ed.agregarDep(d2)
ed.agregarDep(d3)

Y = 1
X = 1
Z = 101

mayor = None
for i in range(ed.cantDep):
    d = ed.deps[i]
    if d.nroPiso == Y:
        if mayor is None or d.nroHab > mayor.nroHab:
            mayor = d

print("Piso", Y, "con más habitaciones:", mayor.nroPuerta)

for i in range(ed.cantDep):
    d = ed.deps[i]
    if d.nroPuerta == Z and d.nroPiso == X:
        d.hab[0].agregarMueble(Mueble("Silla", "Madera"))

maxM = 0
for i in range(ed.cantDep):
    d = ed.deps[i]
    if d.totalMuebles() > maxM:
        maxM = d.totalMuebles()

for i in range(ed.cantDep):
    d = ed.deps[i]
    if d.totalMuebles() == maxM:
        print("Depto con más muebles:", d.nroPuerta)

Zpiso = 1
mejor = None

for i in range(ed.cantDep):
    d = ed.deps[i]
    if d.nroPiso == Zpiso:
        for j in range(d.nroHab):
            h = d.hab[j]
            if mejor is None or h.cantMuebles > mejor.cantMuebles:
                mejor = h

print("Habitación con más muebles:", mejor.nombre)

def primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

nueva = [None]*100
k = 0

for i in range(ed.cantDep):
    d = ed.deps[i]
    if not primo(d.nroHab):
        nueva[k] = d
        k += 1

ed.deps = nueva
ed.cantDep = k

print("Departamentos que quedan:")
for i in range(ed.cantDep):
    print(ed.deps[i].nroPuerta)

ed.parqueo.agregarAuto("123ABC")
ed.parqueo.agregarAuto("456DEF")
ed.parqueo.agregarAuto("789GHI")
