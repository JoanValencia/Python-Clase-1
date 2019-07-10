from random import randint

lista = []

n = randint(0,9)
print n

rep = False

lista.append(n)
"""
if n1 == n2:
    n2 = randint(0,9)
else:
    lista.append(n2)
    n3 = randint(0,9)
print lista
"""

if n in lista:
    lista.append(n)
    else:
      n = randint(0,9)  
print lista      
