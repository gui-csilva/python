#nessa linha criamos uma lista dcom os dias da semana e a string 123
lista = ["seg","ter","qua","qui","sex","sáb","dom",str(123)]
#nessa linha iniciamos um loop
for value in lista:
	#nessa linha vai mostrando os itens da lista 
	print(value)
	#linha mostra a primeira unidade de tal item da lista
	print(value[0])
	#linha mostra a segunda unidade de tal item da lista
	print(value[1])
	#linha mostra a terceira unidade de tal item da lista
	print(value[2])
	#nessa linha mostra o tipo da lista
	print(type(value))
	#nessa linha mostra quantas unidades tem cada string
	print(len(value))
	#nesa linha da um espaço para mostrar os dados da próxima string
	print()