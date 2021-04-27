#nessa linha nós importamos a pacote random
import random

#nessa linha nós criamos uma variavel lista vazia
n1 = []
#nessa linha nós criamos uma variavel com o integer 0 dentro dela
c = 0

#nessa linha nós começamos um while loop
while c < 6:
	#nessa linha nós criamos uma variavel que recebe a função randrange
	rnum = random.randrange(1,61)
	#nessa linha fizemos com que o programa entende que: se rnum não for eencontrado dentro da lista n1 então
	if(rnum not in n1):
		#nessa linha nós usamos uma função que faz com que itens da variavel rnum sejam adicionados a variavel n1 (Só da para usar essa função com listas)
		n1.append(rnum)
		#nessa linha nós fizemos com que toda vez que o programa passar por aqui acrecente uma unidade a variavel c
		c += 1
	
	#else:
		#print("estou no else")

#nessa linha nós imprimimos na tela a variavel n1
print(n1)