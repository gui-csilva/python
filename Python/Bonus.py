def Multiplicar():
	pergunta = input("Montar a tabuada de: ")
	iniciando = input("Começar por: ")
	terminando = input("Terminar em: ")
	pergunta = int(pergunta)
	iniciando = int(iniciando)
	terminando = int(terminando)
	if iniciando > terminando:
		print("O número final tem que ser maior que o número inicial. ")
		return Multiplicar()
	print()
	print("Vou montar a tabuada de: ", pergunta, "começando em ", iniciando, "e terminando em ", terminando, ":")
	while iniciando <= terminando:
		print(pergunta, "x", iniciando, "=", pergunta * iniciando)
		iniciando = iniciando + 1	
	return

Multiplicar()