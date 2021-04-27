def vogais(palavra):
	lista = ""
	string = "aeiou "
	contador = 0
	contando = len(palavra)
	while contador < contando:
		if palavra[contador] in string: 
			lista = lista + palavra[contador]
		contador = contador + 1 
	return lista

#______________________________________________________________________________________________________________________

def vogaisforloop(palavra):
	lista = ""
	string = "aeiou "
	for value in palavra:
		if value in string:
			lista = lista + value
	return lista

vogais = vogaisforloop("oi eu sou o banana")
print(vogais)