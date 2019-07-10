#import random as rn         #librería as alias
from random import randint 

#n = random.randint(10,20)   #nombrelibreria.funcion
#n = rn.randint(10,20)       #alias.funcion
#n = randint(10,20)          #funcion

#n = randint(0,100)
#print n
#adivinado = False
#for i in range(5):
#    a = input("Ingrese su valor: ")
#    if a < n:
#        print "El numero a adivinar es mayor"
#    elif a > n:                 #Else if
#        print "El numero a adivinar es menor"
#    else:
#        print "Ganaste"
#        adivinado = True
#        break
#if not adivinado:
#    print "El numero aleatorio fue " + str(n)
        
"""
lista = []
for i in range(3):
    lista.append(randint(0,100))
print lista
adivinado = False
for i in range(5):
    a = input("Ingrese su valor: ")
    if a in lista:
        print "Ganaste"
        adivinado = True
        break
    else:
        print "sigue intentando"
if not adivinado:
    cad = ""
    for i in lista:
        cad += str(i) + ", "
    print "Los numeros aleatorios eran " + cad[:-2]     #-2 para que no muestre la ultima coma
"""
