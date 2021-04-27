#nessa linha criamos uma variavel em forma de lista com as letras do alfabeto
#a = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
a = ["A","E","I","O","U"]
#nessa linha criamos uma variavel com a função input 
z = input("escolha um número de 1 a 10: ")
#nessa linha criamos a a variavel lista em forma de uma lista vazia
lista = []
#nessa linha criamos uma variavel com o integer 0
b = 0
#nessa linha usamos o while loop que faz o programa entender que "enquanro b dor menor que z então"
while b < int(z):
	#nessa linha usamos uma função que adiciona itens a variavel lista
	lista.append(b)
	#nessa linha fizemos com que toda vez que o programa passar por essa linha vai acrecentar uma unidade a variavel b 
	b = b + 1
#nessa linha fizemos com que o programa fizesse a impressão dos números de 0 até o número desejado
print("lista:", lista)

#nessa linha iniciamos um loop
for value in a:
	#nessa linha fizemos a impressão do valor
	print(value)
	#nessa linha demos um espaço de um valor para o outro
	print()
#nessa linha iniciamos outro loop
	for v in lista:
		#nessa linha fizemos a impressão do valor
		print(value,v)
		#nessa linha demos um espaço de um valor para o outro
		#print()