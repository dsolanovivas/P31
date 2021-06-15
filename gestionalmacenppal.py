from GestionAlmacen import GestionAlmacenO


dic_claseproducto={
    "1": {
        "nombre":"Manzanas", 
        "precio":"9000.0", 
        "inventario":"65"
        },
    "2": {"nombre":"Limones", "precio":"2300.0", "inventario":"15"},
    "3": {"nombre":"Peras", "precio":"2500.0", "inventario":"38"},
    "4": {"nombre":"Arandanos", "precio":"9300.0", "inventario":"55"},
    "5": {"nombre":"Tomates", "precio":"2100.0", "inventario":"42"},
    "6": {"nombre":"Fresas", "precio":"4100.0", "inventario":"33"},
    "7": {"nombre":"Helado", "precio":"4500.0", "inventario":"41"},
    "8": {"nombre":"Galletas", "precio":"500.0", "inventario":"833"},
    "9": {"nombre":"Chocolates", "precio":"3500.0", "inventario":"806"},
    "10": {"nombre":"Jamon", "precio":"17000.0", "inventario":"10"},
            }


print("INICIAR")
myAlmacen = GestionAlmacenO(dic_claseproducto)
print(myAlmacen.inventario)

print("AGREGAR")
myAlmacen.agregar("11", {"nombre":"arroz", "precio":"3500.0", "inventario":"20"})
print(myAlmacen.inventario)

print("ACTUALIZAR")
myAlmacen.actualizar("3", {"nombre":"Peras", "precio":"1200.0", "inventario":"40"})
print(myAlmacen.inventario)

print("BORRAR")
myAlmacen.remover("10")
print(myAlmacen.inventario)