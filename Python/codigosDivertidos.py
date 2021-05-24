import math

def numeros():
    base = input("Escolha um número para ser a base da potência: ")
    numeroElevado = input("Escolha um número para ser o expoente: ")
    base = int(base)
    numeroElevado = int(numeroElevado)
    #print(base)
    #print(numeroElevado)
    print()
    resultado = (base, numeroElevado)
    return resultado

def calcular(n1, n2):
    return math.pow(n1, n2)

def main():
    resultado = numeros()
    potencia = calcular(resultado[0], resultado[1])
    print(potencia)

main()
