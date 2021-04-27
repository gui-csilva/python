def fatorial(parametro):
	a = int(parametro)
	b = a * (a - 1)
	a = a - 1
	while a > 1:
		a = a - 1
		b = b * a
	return b

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

def imprimirResposta(numeroCalculado, resultado):
	a = numeroCalculado
	string = ""
	string = string + str(a) + " = "
	while a > 1:
		string = string + str(a) + " x "
		a = a - 1
	string = string + str(a) + " = " + str(resultado)
	return string

def main():
	a = input("Escolha um número de 15 para baixo: ")
	numeroInserido = validarInput(a)
	resultado = fatorial(numeroInserido)
	impressao = imprimirResposta(numeroInserido, resultado)
	print(impressao)

main()