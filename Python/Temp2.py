pergunta = input("Escolha um número: ")
lista = []
#lista.append(pergunta)

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
print(soma)

media = soma / a
print("A média dos números fornecidos é:", media)