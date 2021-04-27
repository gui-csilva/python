#IDE (programa que nos ajuda a escarever códigos)
#String ou str (qualquer coisa escrita entre duas aspas) 
#single quote = apostrofe = 1 aspa; quote = aspas = " "
#"conversa";#string
#'F'; #caracter
#-10 até 10 int = Integer = numero inteiro
#10;
#-10; 
#Float= número decimal= 10.9
#3.4;
#String"10"
#Variaveis - Variables - VAR
#Jeferson = "minha variavel"
#type = mostra o tipo da variavel
#input = faz uma pergunta que espera resposta essa resposta pode ser usada para uma variavel
#print = imprimi o que você quiser na tela
#cls = limpar tela do cmd
#str = transforma integer em string
#int = transforma string em integer
#contatenacao = quando você soma? junta duas strings
#recebe: =
#igual: ==
#boolean = fala se é verdadeiro ou falso; Se você chamar a função 0 da falso, mas se você chamar qualquer outra coisa vai dar true
#bool() = fala se é verdadeiro ou falso
#if = é uma função reservada que te da uma resposta baseado em uma comparação
#elif = é uma função reservada que te da uma resposta baseado em uma comparação


#Criar um programa que pede o nome do usuario, o ano de nascimento do usuarios, e dois numeros.
#nome = input("Qual seu nome? ");
#ADN = input("Qual é seu ano de nacimento? ");
#PN = input("Coloque um número aqui! ");
#SN = input("coloque outro número aqui! ");
#idade = 2021 - int(ADN)
#soma = int(PN) + int(SN)

#nome = "Vitor"

#segundoNome = nome
#print("Nome:" + nome)
#print("idade:" + str(idade) + "/" + ADN)
#print("a soma dos seus números foi:" + str(soma))
#print("segundoNome")
#print(segundoNome)
#lists/Array = faz uma lista com qualquer tipo. Se usa esses símbolos para fazer a lista: []. Em uma lista a vírgula separa os elementos
#len = contas os elementos de strings e listas
#lista[2:] = mostra o elemento 2 da lista e os elemnetos que estão a diante
#lista[:2] = mostra um elemento anterior do elemento 2 e os que estão anteriormente
#para usar duas condições diferentes com o mesmo resultado entra as condições coloque or ou |. O :(então só é usado no final)

import random

a = random.randrange(1,11)
b = random.randrange(11,21)
c = random.randrange(21,31)
d = random.randrange(31,41)
e = random.randrange(41,51)
f = random.randrange(51,61)

print(str(a) + "-" + str(b) + "-" + str(c) + "-" + str(d)+ "-" + str(e) + "-" + str(f))