def pedirNumeros():
	pergunta = input("Montar a tabuada de: ")
	iniciando = input("Começar por: ")
	terminando = input("Terminar em: ")
	resposta = {}
	resposta["pergunta"] = int(pergunta)
	resposta["iniciando"] = int(iniciando)
	resposta["terminando"] = int(terminando)
	if resposta["iniciando"] > resposta["terminando"]:
		print("O número de inicio não pode ser maior que o número de finalização")
		return pedirNumeros()
	return resposta

def multiplicar(numero1, numero2):
	return numero1 * numero2

def imprimirContas(pergunta, iniciando, terminando):
	print()
	print("Vou mostrar a tabuada de", pergunta, "começando em ", iniciando, "e terminando em ", terminando, ":")
	while iniciando <= terminando:
		print(pergunta, "x", iniciando, "=", multiplicar(pergunta, iniciando))
		iniciando = iniciando + 1
	return

def main():
	numeros = pedirNumeros()
	imprimindo = imprimirContas(numeros["pergunta"], numeros["iniciando"], numeros["terminando"])


main()