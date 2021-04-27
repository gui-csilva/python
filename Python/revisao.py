pergunta = input("escolha um número: ")
pergunta2 = input("escolha outro número: ")

pergunta = int(pergunta)
pergunta2 = int(pergunta2)

def soma(soma, soma2):
	resultado = soma + soma2
	return resultado

def subtracao(sub, sub2):
	resultado = sub - sub2
	return resultado

def multiplicacao(mult, mult2):
	resultado = mult * mult2
	return resultado

def divisao(div, div2):
	resultado = div / div2
	return resultado


soma = soma(pergunta, pergunta2)
subtracao = subtracao(pergunta, pergunta2)
multiplicacao = multiplicacao(pergunta, pergunta2)
divisao = divisao(pergunta, pergunta2)

print("soma:", soma, "/", "subtracao:", subtracao, "/", "multiplicacao:", multiplicacao, "/", "divisao:", divisao)