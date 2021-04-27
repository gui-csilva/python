# def sortlist(lista, numero):
# 	listavazia = []
# 	list_low = []
# 	list_high = []

# 	contador = 0
# 	contarlista = len(lista)
# 	while contador < contarlista:
# 		if lista[contador] <= numero:
# 			list_low.append(lista[contador])
# 		else:
# 			list_high.append(lista[contador])
# 		contador = contador + 1 
# 	listavazia.append(list_low)
# 	listavazia.append(list_high)
# 	return listavazia

# resultado = sortlist([1,2,3,4,5,6,7,8,9,0], 5)
# print(resultado)

#__________________________________________________________________________________________________________________

def sortlist(lista, numero):
	listavazia = []
	list_low = []
	list_high = []
	for value in lista:
		if value <= numero:
			list_low.append(value)
		else:
			list_high.append(value)
	listavazia.append(list_low)
	listavazia.append(list_high)
	return listavazia

resultado = sortlist([1,2,3,4,5,6,7,8,9,0], 5)
print(resultado)