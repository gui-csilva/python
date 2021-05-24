def sortNumbers(lista):
	listaOrganizada = []
	a = len(lista)
	for value in range(a):
		menor = min(lista)
		listaOrganizada.append(menor)
		lista.remove(menor)
	return listaOrganizada



print(sortNumbers([9,5,4,3,2,0,-1, -2, -3, -1, -2, 0.2, 0.3, 0.4, 0.1, 100, 20000000, 12]))