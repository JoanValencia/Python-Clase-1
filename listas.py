#valores = [1, 2, 3, 4, 5]

#nuevo_valor = input("Ingrese el nuevo valor: ")
#valores += [nuevo_valor]
#valores.append(nuevo_valor)    #Agrega un nuevo valor a la lista
#valores.pop(0)                 #elimina el valor en el item 0
#print valores

#valores = range(101)       #(Lista por rango)rango de 0 a 100
#valores = range(50,101)    #rango de 50 a 100
#valores = range(50,101,5)  #rango de 50 a 100 en saltos de 5

#print valores

#n = 0
#m = 0
#for i in valores:  #itera todos los elementos de la lista
#    if i % 2 == 0: #condición pares
#        n += i
#    else:          #impares
#        m += i
#print "Suma pares = " + str(n)
#print "Suma impares = " + str(m)

#for i in valores:
#    print i ** 2   #imprime el cuadrado de cada valor

#valores = [x ** 2 for x in range(1,101)]               #(Lista por comprensión)Guarda el cuadrado de cada valor dentro de la lista
valores = [x ** 2 for x in range(1,101) if x % 5 == 0]  #con filtro de multiplos de 5 
print valores
print len(valores)  #muestra el tamaño de la lista
print sum(valores)  #suma los valores de la lista
