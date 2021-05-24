import Cargo
import Pessoa

estagiario = Cargo("estagiario", 1300.00, 20)
secretaria = Cargo("secretaria", 2200.00, 40)
supervisor = Cargo("supervisor", 6000.00, 60)

pessoaA = Pessoa("Junior", "M", 13, 64889900, 43237168351, 302163271, 886535673, 4000.50, estagiario)
pessoaB = Pessoa("Julia", "F", 22, 79172334, 45910735481, 111225368, 547351564, 1000.90, secretaria)
pessoaC = Pessoa("Sebastião", "M", 45, 73921539, 3710018624130, 142623567, 789017203, 2500.75, supervisor)

pessoaA.printPessoa()
pessoaB.printPessoa()
pessoaC.printPessoa()