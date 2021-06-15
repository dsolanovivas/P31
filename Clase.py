


t = ("A","B")
#print(t)

l= list(t)
#print(l)



#listas
myList = []
myList2 = [1,2,3,4,5,6,7,8,9]

#print("Elemento")
for elemento in myList2:
    #print (elemento)
    pass

#print("Index")
for index in range(0,len(myList2),1):
    #print (myList2[index])
    pass


myList2.append(10)
#print (myList2)

myList2.extend([11,12,13])
#print (myList2)

myList2.extend([10,11,15])
#print (myList2)

myList2.remove(10)
#print (myList2)

pos = myList2.index(12)
#print("la pos es : " + str(pos) )

cuente = myList2.count(11)
#print("hay " + str(cuente))

myList2.reverse()
#print(myList2)







# print("Mis Pekemones")
# Darwin="XYZ"
# mispekemones = 'YSGLZQUQSKRQSBVLVJGQ'
# for pe in mispekemones:
#     if pe in Darwin:
#         print(pe + " Si esta en mis pekkemones")
#     else:
#         print(pe + " No esta en mis pekkemones")


def elevar(num):
    return (num**2)

lambda_func1 = lambda x,y : x**2 + y

resultado = lambda_func1(3,4)
print(resultado)

resultado2 = elevar(3)
print(resultado2)

lambda_func2 = lambda y : y%2 != 0
impar= lambda_func2(7)
par = lambda_func2(6)

print("el numero 7 es " + str(impar))
print("el numero 6 es " + str(par))

lambda_func3 = lambda texto : texto[::-1]

mitextovoletado= lambda_func3("Soy del grupo 31")
print("Voletado: "+ mitextovoletado)

lambda_func4 = lambda x, y, z : x**2 + y if z==True else x**2 + y + 1  
print(lambda_func4(3, 1, True))
print(lambda_func4(4, 2, False))
print(lambda_func4(5, 3, True))

def multiplo(num):
    if num%5 == 0:
        return True

LamMult = lambda numero: numero%5!=0

numeros = [1, 2, 5, 10, 14, 15, 23, 50, 78]

Multi = list(filter(LamMult, numeros))
print(Multi)

def doblarNumero(num):
    return (num*2)

lamtrip = lambda num : num*3

doble = list(map(lamtrip, numeros))
print(doble)


tipos_documentos = ('C', 'TI', 'P')
compradores = [
    {
        'tipo_documento' : 'C', 
        'numero_documento' : 12345998, 
        'cantidad_adultos' : 2, 
        'cantidad_menores' : 0
    },
    {'tipo_documento': 'P',
        'numero_documento': 39543111, 'cantidad_adultos': 1, 'cantidad_menores': 3},
    {'tipo_documento': 'TI',
        'numero_documento': 16454393, 'cantidad_adultos': 0, 'cantidad_menores': 3}
]
totalBoletas('24/05/2021', tipos_documentos, compradores)
