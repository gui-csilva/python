#Programação editada.

#Criar um programa que pede o nome do usuario, o ano de nascimento do usuarios, e dois numeros.

#Nessa linha eu criei a primeira pergunta
nome = input("Qual seu nome? ");
#Nessa linha eu criei a segunda pergunta
ADN = input("Qual é seu ano de nacimento? ");
#Nessa linha eu criei a primeira exigencia
PN = input("Coloque um número aqui! ");
#Nessa linha eu criei a segunda exigencia
SN = input("coloque outro número aqui! ");
#Nessa linha foi programado para subtrair o ano de hoje pela resposta da segunda pergunta
idade = 2021 - int(ADN)
#Nessa linha foi somado o número da primeira e da segunda exigencia
soma = int(PN) + int(SN)


#Nessa linha foi dado o nome da pessoa
print("Nome:" + nome)
#Nessa linha foi escrito a idade e o ano de nacimento da pessoa
print("idade:" + str(idade) + "/" + ADN)
#Nessa linha foi escrita a soma dos dois números que a pessoa escreveu
print("a soma dos seus números foi:" + str(soma))





#Programação normal.

nome = input("Qual seu nome? ");
ADN = input("Qual é seu ano de nacimento? ");
PN = input("Coloque um número aqui! ");
SN = input("coloque outro número aqui! ");
idade = 2021 - int(ADN)
soma = int(PN) + int(SN)

#nome = "Vitor"

#segundoNome = nome
print("Nome:" + nome)
print("idade:" + str(idade) + "/" + ADN)
print("a soma dos seus números foi:" + str(soma))
#print("segundoNome")
#print(segundoNome)