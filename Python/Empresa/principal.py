import Cargo
import Pessoa
import Rh
import random

estagiario = Cargo.Cargo("estagiario", 1300.00, 20)
secretaria = Cargo.Cargo("secretaria", 2200.00, 40)
supervisor = Cargo.Cargo("supervisor", 6000.00, 60)

funcionarios = [
	Pessoa.Pessoa("Junior", "M", 13, 64889900, 43237168351, 302163271, 886535673, 4000.50, estagiario),
	Pessoa.Pessoa("Julia", "F", 22, 79172334, 45910735481, 111225368, 547351564, 1000.90, secretaria),
	Pessoa.Pessoa("Sebastião", "M", 45, 73921539, 3710018624130, 142623567, 789017203, 2500.75, supervisor)
]

# print(type(funcionarios[0]))

for value in funcionarios:
	pessoaRh = Rh.Rh(value)
	print(value.getNome())
	print("Salario: ", value.getSalario())
	print("plr: ", pessoaRh.plr())
	print("salarioComPlr: ", pessoaRh.salarioComPlr())
	if random.randrange(1,3) == 20:
		pessoaRh.setFerias(True)
	if pessoaRh.getFerias() == True:
		print("férias: ", pessoaRh.valorFerias())
		print("salarioComFérias: ", pessoaRh.retornarSalarioComTerco())
	print()



# pessoaA.printPessoa()
# print()
# pessoaB.printPessoa()
# print()
# pessoaC.printPessoa()
# print("----")
# print(type(secretaria))