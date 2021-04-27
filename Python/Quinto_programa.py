#nessa linha nós criamos a variavel par
par = []
#nessa linha nós criamos a variavel impar
impar = []
#nessa linha nós criaos uma lista com 6X a função random.randrange
numeros = []
x = 0
z = input("digite um número: ")
while x < int(z):
	numeros.append(x)
	x = x + 1
print("numeros", numeros)

#nessa linha nós iniciamos um loop
for value in numeros:
	
	if ((value % 2) == 0):
		par.append(value)
	else:
		impar.append(value)

print("par", par)
print("impar", impar)