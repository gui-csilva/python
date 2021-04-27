# def fatorial (parametro):
# 	a = int(parametro)
# 	if a == 0 or a == 1:
# 		return 1
# 	elif a < 0:
# 		a = input("Não existe fatorial de negativo. Escolha outro número: ")
# 		return fatorial(a)
# 	else:
# 		b = a * (a - 1)
# 		a = a - 1
# 		while a > 1:
# 			a = a - 1
# 			b = b * a
# 		return b

# a = input("Escolha um número inteiro: ")

# bnn = fatorial(a)
# print(bnn)

# Passo 1 - Ter a palavra normal
# Passo 2 - Contar os caracteres/letras da palavra normal
# Passo 3 - Criar a variavel contador que recebe contador - 1
# Passo 4 - Criar a variavel Palavra invertida e colocar uma string vazia dentro dela
# Pass 5 - Iniciar um while loop (enquanto contador for maior ou igual a 0 entao)
# Passo 6 - Variavel palavra invertida recebe palavra invertida + parametro na posicao do contador
# Passo 7 - Subtrair 1 do contador
#Passo 8 - Fazer um IF (se palavra normal for igual a palavra invertida entao )
#Passo 9 - Retornar True
#Passo 10 - Fazer um Else (se as palavras nao forem iguais entao)
#Passo 11 - Retornar False

def is_palindromo(palavra_digitada):
	palavra_inserida = len(palavra_digitada)
	contador = palavra_inserida - 1
	palavra_invertida = ""
	while contador >= 0:
		palavra_invertida = palavra_invertida + palavra_digitada[contador]
		contador = contador - 1
	if palavra_digitada == palavra_invertida:
		return True
	else:
		return False


a = input("Escolha uma palavra: ")
variavel = is_palindromo(a)
print(variavel)



# palavra_inserida = 8

# 35: criamos a variavel contador que recebe palavra_inserida - 1, ou seja nesse caso 7.
# contador = 7

# 36: criamos a variavel palavra_invertida que recebe uma string vazia.
# palavra invertida = ""

# 37: iniciamos um loop (enquanto contador for maior ou igaula  0 entao)
# contador = 7

# 38: palavra_invertida no inicio é = ""
# palavra_digitada[contador] = "a"
# o resultado da palavra_invertida é = "a"

# 39: contador = 6
# loop roda pela segunda vez
# contador = 6
# palavra_digitada[contador] = "i"
# palavra_invertida = "ai"
# contador = 5
# loop roda pela terceira vez
# contador = 5
# palavra_digitada[contador] = "c"
# palavra_invertida = "aic"
# contador = 4
# loop roda até o final
# contador = 0
# palavra_digitada[contador] = "m"
# palavra_invertida = "aicnalem"
# contador = -1

# 40: Se "melancia" for = "aicnalem" entao
# retornar True.(linha 41)

# 42: Se nao entao
# retornar False.(linha 43)