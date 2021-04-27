#nessa linha criamos a variavel par
par = []
#nessa linha criamos a variavel a
a = [1,2,3,4,5,6,7,8,9,10]
#nessa linha criamos a variavel impar
impar = [] 
#nessa linha iniciamos um loop
for v in a:
	#nessa linha imprimimos a string par
	print("par")
	#nessa linha mostra os números pares
	print(par)
	#nessa linha imprimimos a string impar
	print("impar")
	#nessa linha mostra os números impares
	print(impar)
	#nessa linha da um espaço
	print()	
	#nessa linha colocamos uma função para indentificar se o número é par
	if(v % 2) == 0:
		#nessa linha execultamos a função para indicar se o número é par
		par.append(v)
	#nessa linha colocamos uma função para indentificar se o número é não é par
	else: 
		#nessa linha execultamos a função para falar indicar que o número é impar
		impar.append(v)

#nessa linha mostra todos os números pares
print(par)
#nessa linha mostra todos os números
print(a)
#nessa linha msotra todos os números imapares
print(impar)