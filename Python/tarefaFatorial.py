#Essa função calcula o resultado fatorial de um numero.
#Param: parametro - Integer
#Return: b - Integer
def fatorial(parametro):
	a = int(parametro)
	b = a * (a - 1)
	a = a - 1
	while a > 1:
		a = a - 1
		b = b * a
	return b

#Fornecido como parametro um numero inteiro, validamos se o numero e 0, 1, negativo ou maior que 15
#Param: ncalculado - Integer
#Response: a - Integer
def validarInput(ncalculado):
	a = int(ncalculado)
	if a == 0 or a == 1:
		return 1
	elif a < 0:
		a = input("Não existe fatorial de negativo. Escolha outro número: ")
		return validarInput(a)
	elif a > 15:
		a = input("O número digitado não pode passar de 15. Por favor digite outro número: ")
		return validarInput(a)
	return a


#Fornecido 2 parametros, um numero para se calular o fatorial e o resultado deste numero fatorial, a funcao imprime de modo verboso o que esta sendo calculado
#Param - numeroCalulado - Integer (numero a ser calculado)
#Param - resultado - Integer (Calculo fatorial do numero calculado)
#return - string - String (Frase concatenada com a equacao total)
def imprimirResposta(numeroCalculado, resultado):
	a = numeroCalculado
	string = ""
	string = string + str(a) + " = "
	while a > 1:
		string = string + str(a) + " x "
		a = a - 1
	string = string + str(a) + " = " + str(resultado)
	return string

#Essa função é o centro do código, ela chama todas as funções.
def main():
	a = input("Escolha um número de 15 para baixo: ")
	numeroInserido = validarInput(a)
	resultado = fatorial(numeroInserido)
	impressao = imprimirResposta(numeroInserido, resultado)
	print(impressao)


#Vitor Vannuchi adicionou este comentario.
main()