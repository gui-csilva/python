def fatorial (parametro):
	string = ""
	a = int(parametro)
	string = string + str(a) + " = "
	if a == 0 or a == 1:
		return 1
	elif a < 0:
		a = input("Não existe fatorial de negativo. Escolha outro número: ")
		return fatorial(a)
	elif a > 15:
		a = input("O número digitado não pode passar de 15. Por favor digite outro número: ")
		return fatorial(a)
	else:
		b = a * (a - 1)
		string = string + str(a)
		a = a - 1
		while a > 1:
			string = string + " x " + str(a)
			a = a - 1
			b = b * a
		string = string + " x " + str(a) + " = " + str(b)
		return string

a = input("Escolha um número de 15 para baixo: ")

bnn = fatorial(a)
print(bnn)