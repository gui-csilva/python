#nessa linha nós importamos a função random
import random
#nessa linha nós usamos essa função
numerosorteado = random.randrange(1 , 11)

#nessa linha nós fizemos a primeira exigencia
a = input("tente adivinhar um numero de 1 a 10, você tem três chances: ")
#nessa linha nós transformamos a exigencia que era uma string em integer
a = int(a)
#numerosorteado = random.randrange(1 , 11)

#nessa linha nós usamos a função if para dizer "parabéns você acertou o número sorteado!!!" se a pessoa tivesse acertado
if a == numerosorteado: 
	#nessa linha nós colocamos o recado "parabéns você acertou o número sorteado!!!"
	print("parabéns você acertou o número sorteado!!!")
#nessa linha nós usamos a função else para dizer "você errou o número sorteado" se a pessoa tivesse errado
else:
	#nessa linha nós colocamos o recado "você errou o número sorteado"
	print("você errou o número sorteado")

	#nessa linha colocamos outra chance caso a pessoa tenha errado
	a = input("Tente novamente. Essa é sua segunda chance: ")
	#nessa linha nós tranformamos a segunda chace que era uma string em um integer
	a = int(a)
	#numerosorteado = random.randrange(1 , 11)

	#nessa linha nós usamos a função if para dizer "parabéns você acertou o número sorteado!!!" se a pessoa tivesse acertado
	if a == numerosorteado: 
		#nessa linha nós colocamos o recado "parabéns você acertou o número sorteado!!!"
		print("parabéns você acertou o número sorteado!!!")
	#nessa linha nós usamos a função else para dizer "você errou o número sorteado" se a pessoa tivesse errado
	else:
		#nessa linha nós colocamos o recado "você errou o número sorteado"
		print("você errou o número sorteado")

		#nessa linha colocamos outra chance caso a pessoa tenha errado
		a = input("Tente novamente. Essa é sua terceira chance: ")
		#nessa linha nós tranformamos a segunda chace que era uma string em um integer
		a = int(a)
		#numerosorteado = random.randrange(1 , 11)

		#nessa linha nós usamos a função if para dizer "parabéns você acertou o número sorteado!!!" se a pessoa tivesse acertado
		if a == numerosorteado: 
			#nessa linha nós colocamos o recado "parabéns você acertou o número sorteado!!!"
			print("parabéns você acertou o número sorteado!!!")
		#nessa linha nós usamos a função else para dizer "você errou o número sorteado" se a pessoa tivesse errado
		else:
			#nessa linha nós colocamos o recado "você errou o número sorteado"
			print("você errou o número sorteado")

			#nessa linha foi feita a mensagem "acabaram suas chances você perdeu" no caso da pessoa não conseguir acertar o número
			print("Acabaram suas chances você perdeu.")			