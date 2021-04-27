#Nessa linha pedimos o primeiro número
PN = input("Por favor digite o primeiro numero: ")
#Nessa linha pedimos o segundo número
SN = input("Por favor digite o segundo numero: ")

#Criando uma variavel para a função int(PN)
intpn = int(PN)
#Criando uma variavel para a função int(SN)
intsn = int(SN)

#Nessa linha vai ser feita a conta de adição dos números colocados.
Adicao = intpn + intsn
#Nessa linha vai ser feita a conta de subtração dos números colocados.
Subtracao = intpn - intsn
#Nessa linha vai ser feita a conta de multiplicação dos números colocados.
Multiplicacao = intpn * intsn
#Nessa linha vai ser feita a conta de divisão dos números colocados.
Divisao = intpn / intsn


#Nessa linha vai sair o resultado da adição
print("Adicao: " + str(Adicao))

#Nessa linha vai sair o resultado da subtração
print("subtracao: " + str(Subtracao))

#Nessa linha vai sair o resultado da multiplicação
print("multiplicacao: " + str(Multiplicacao))

#Nessa linha vai sair o resultado da divisão
print("divisao: " + str(Divisao))