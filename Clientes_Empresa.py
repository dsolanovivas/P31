#POO
class Cliente:

    NoDocumento = 0
    Nombre = ""
    Apellidos = ""
    Edad = 0
    Fecha_nacimiento = ""

    def __init__(self, nodocumento, nombre, apellidos, edad, fechanac):
        self.NoDocumento = nodocumento
        self.Nombre = nombre
        self.Apellidos = apellidos
        self.Edad = edad
        self.Fecha_nacimiento = fechanac

    def mostrar_cliente(self):
        print(f"Los datos son {self.Nombre} {self.Apellidos} {self.Edad} {self.Fecha_nacimiento}")
        return

    def actualizar_fecha(self, fecha):
        self.Fecha_nacimiento=fecha

class Empresa:

    Nombre= ""
    NIT=""

    
    def __init__(self, nit, nombre):
        self.Nombre = nombre
        self.NIT = nit
    



