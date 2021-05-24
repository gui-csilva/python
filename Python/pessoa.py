class Pessoa:
	def __init__(self, nome = None, sexo = None, idade = None):
		self.nome = nome
		self.sexo = sexo
		self.idade = idade

	def printPessoa(self):
		print(self.nome, "/", self.sexo, "/", self.idade)

	def setSexo(self, sexo):
		self.sexo = sexo

	def setNome(self, nome):
		self.nome = nome

	def setIdade(self, idade):
		self.idade = idade

	def getSexo(self):
		return self.sexo

	def getNome(self):
		return self.nome

	def getIdade(self):
		return self.idade
	
	def trocarDeSexo(self):
		if self.getSexo() == "M":
			self.setSexo("F")
		elif self.getSexo() == "F":
			self.setSexo("M")
		else:
			print("Essa pessoa não tem sexo.")



pessoaA = Pessoa("Junior", "M", 13)
pessoaB = Pessoa("Julia", "F", 22)
pessoaC = Pessoa("Sebastião")
# pessoaA.printPessoa()
# pessoaB.printPessoa()
# pessoaC.printPessoa()


pessoaC.setSexo("M")
pessoaC.setIdade(71)
#pessoaC.printPessoa()
pessoaC.trocarDeSexo()
#pessoaC.printPessoa()

pessoas = [pessoaA, pessoaB, pessoaC]

for value in pessoas:
	if value.getIdade() < 70:
		value.printPessoa()