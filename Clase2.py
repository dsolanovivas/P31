#Estructurado

#listado de clientes
clientes = [
    {'Nombre' : 'Duvan', 'Apellidos': 'Rodelo', 'NoDocumento': 15478791},
    {'Nombre' : 'David', 'Apellidos': 'Valera', 'NoDocumento': 98746201},
    {'Nombre' : 'Johandris', 'Apellidos': 'Cabarcas', 'NoDocumento': 74185293}
]

#Mostrar cliente segun el documento
def mostrar_cliente(clientes, documento):
    for cliente in clientes:
        if (documento == cliente['NoDocumento']):
            print(f"Los datos son {cliente['Nombre']} {cliente['Apellidos']}")
            return
    print("La persona nunca fue encontrada")

#borrar un cliente de la lista segun el documento
def borrar_cliente(clientes, documento):
    for index, cliente in enumerate(clientes):
        if (documento == cliente['NoDocumento']):
            del(clientes[index])
            print(f"El cliente {cliente} fue borrado")
            return
    print("La persona nunca fue encontrada")

print("Listado inicial")
print(clientes)

print("mostrar clientes ")
mostrar_cliente(clientes, 98746201)
mostrar_cliente(clientes, 15478791)


print("Borrar clientes ")
borrar_cliente(clientes, 74185293)
borrar_cliente(clientes, 15478791)

print("Listado final")
print(clientes)



#POO
