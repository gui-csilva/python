#lista.append(pergunta)

def media():
	pergunta = input("Escolha um número: ")
	lista = []
	while pergunta != "c":
		pergunta = int(pergunta)
		lista.append(pergunta)
		pergunta = input("Escolha outro número ou aperte c para finalizar: ")
	print(lista)
	a = len(lista)
	b = 0
	soma = 0
	while b < a:
		soma = soma + lista[b]
		b = b + 1
	media = soma / a
	return media

media = media()
print("A média dos números fornecidos é:", media)