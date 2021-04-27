def somaLista(lista):
	resposta = 0
	for value in lista:
		resposta += value
	return resposta 


def subLista(lista):
	resposta = 0
	for value in lista:
		resposta -= value
	return resposta


def multLista(lista):
	resposta = 1
	for value in lista:
		resposta *= value
	return resposta


def divLista(lista):
	resposta = lista[0]
	lista.pop(0)
	for value in lista:
		resposta /= value
	return resposta

ml = [1, 2, 3, 4, 5]
s = somaLista(ml)
sub = subLista(ml)
mult = multLista(ml)
div = divLista(ml)

print(s)
print(sub)
print(mult)
print(div)