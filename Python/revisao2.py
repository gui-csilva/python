# lista = [1,2,3,4,5,6,7,8,9,0]

# def isEven(value):
# 	if (value %2 == 0):
# 		return True;
# 	else:
# 		return False

# def imprimirNumerosPares(lista):
# 	for value in lista:
# 		if isEven(value):
# 			print(value)

# inp = imprimirNumerosPares(lista)


# def maiornumero(lista):
# 	memoria = lista[0]
# 	for value in lista:
# 		if value > memoria:
# 			memoria = value
# 	return memoria

# resultado = maiornumero([0,-1,-2,-3,-4,-5,-6,-7,-8,-10,100])
# print(resultado)


#revisão3

# def menornumero(lista):
# 	memoria = lista[0]
# 	for value in lista:
# 		if value < memoria:
# 			memoria = value
# 	return memoria

# resultado = menornumero([0,-1,-2,-3,-4,-5,-6,-7,-8,-10,-100])
# print(resultado)



#_________________________________________________________________________________________________________________________

#maior numero

# def maiornumero(lista):
# 	memoria = lista[0]
# 	contador = 0
# 	cdl = len(lista)
# 	while contador < cdl:
# 		if memoria < lista[contador]:
# 			memoria = lista[contador]	
# 		contador = contador + 1
# 	return memoria


# resultado = maiornumero([0,-1,-2,-3,-4,-5,-6,-7,-8,-10,100])
# print(resultado)

#______________________________________________________________________________________________________________________________

#menor numero

def menornumero(lista):
	memoria = lista[0]
	contador = 0
	cdl = len(lista)
	while contador < cdl:
		if memoria > lista[contador]:
			memoria = lista[contador]			
		contador = contador + 1
	return memoria



resultado = menornumero([0,-1,-2,-3,-4,-5,-6,-7,-8,-10,-100])
print(resultado)