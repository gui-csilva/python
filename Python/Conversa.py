pai1 = "Pai: Filho você quer almoçar? "
respostaA = "a) Claro!"
respostaB = "b) Não, valeu."
pergunta = input("Escolha umas das alternativas e coloque ela aqui: ")
a = respostaA
b = respostaB

def conversa(pai, respostaA, respostaB, pergunta):
	triste = "Ok, ;-;"
	print(pai)
	print(perguntaA, "", respostaB)
	print(pergunta)
	if pergunta == "a":
		print("Tá bom, onde você quer almoçar? ")
	elif pergunta == "b":
		return triste
	pai = "Pai: Ok, vou pegar a chave do carro! "
	respostaA = "a) No restauranteda esquina. "
	respostaB = "b) Na feira. "
	print(respostaA, "", respostaB)
	print(pergunta)
	if pergunta == a:
		print(pai)
	elif pergunta == b:
		print(pai)
	print("*Na", pergunta, "*")
	print("Você: muito obrigado por me trazer aqui pai! ")

dialogo = conversa(pai1, respostaA, respostaB, pergunta)
print(dialogo)
