import calculadora

numero1 = input("escolha um número: ")
numero2 = input("escolha outro número: ")
numero1 = int(numero1)
numero2 = int(numero2)

print(calculadora.soma(numero1, numero2))
print(calculadora.subtracao(numero1, numero2))
print(calculadora.multplicacao(numero1, numero2))
print(calculadora.divisao(numero1, numero2))
