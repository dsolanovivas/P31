class GestionAlmacenO:

    inventario = {}

    def __init__(self, diccionario2):
        self.inventario.update(diccionario2)


    def agregar(self, codigo, diccionario):

       nuevodiccionario={codigo:diccionario}
       self.inventario.update(nuevodiccionario)
        
    def actualizar(self, codigo, diccionario):

       nuevodiccionario={codigo:diccionario}
       self.inventario.update(nuevodiccionario)
        
    def remover (self, codigo):
        self.inventario.pop(codigo)
            

    

    