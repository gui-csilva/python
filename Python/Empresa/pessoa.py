class Pessoa:
	#construtor que cria o objeto da classe pessoa. Toda vez que alguém chamar "Pessoa("Junior", "M", 13)" essa função é executada. 
	def __init__(self, nome = None, sexo = None, idade = None, cep = None, cpf = None, rg = None, telefone = None, salario = None, cargo = None):
		self.nome = nome
		self.sexo = sexo
		self.idade = idade
		self.cep = cep
		self.cpf = cpf
		self.rg = rg
		self.telefone = telefone
		self.salario = salario
		self.cargo = cargo

	def printPessoa(self):
		print(self.nome, "/", self.sexo, "/", self.idade, "/", self.cep, "/", self.cpf, "/", self.rg, "/", self.telefone, "/", self.salario, "/", self.cargo)

	def setSexo(self, sexo):
		self.sexo = sexo

	def setNome(self, nome):
		self.nome = nome

	def setIdade(self, idade):
		self.idade = idade
	
	def setCep(self, cep):
		self.cep = cep
	
	def setCpf(self, cpf):
		self.cpf = cpf
	
	def setRg(self, rg):
		self.rg = rg
	
	def setTelefone(self, telefone):
		self.telefone = telefone
	
	def setSalario(self, salario):
		self.salario = salario
	
	def setCargo(self, cargo):
		self.cargo = cargo

	def getSexo(self):
		return self.sexo

	def getNome(self):
		return self.nome

	def getIdade(self):
		return self.idade
	
	def getCep(self):
		return self.cep

	def getCpf(self):
		return self.cpf

	def getRg(self):
		return self.rg

	def getTelefone(self):
		return self.telefone

	def getalario(self):
		return self.salario

	def getCargo(self):
		return self.cargo
	


	# def trocarDeSexo(self):
	# 	if self.getSexo() == "M":
	# 		self.setSexo("F")
	# 	elif self.getSexo() == "F":
	# 		self.setSexo("M")
	# 	else:
	# 		print("Essa pessoa não tem sexo.")



# pessoaA = Pessoa("Junior", "M", 13)
# pessoaB = Pessoa("Julia", "F", 22)
# pessoaC = Pessoa("Sebastião")
# # pessoaA.printPessoa()
# # pessoaB.printPessoa()
# # pessoaC.printPessoa()


# pessoaC.setSexo("M")
# pessoaC.setIdade(71)
# #pessoaC.printPessoa()
# pessoaC.trocarDeSexo()
# #pessoaC.printPessoa()

# pessoas = [pessoaA, pessoaB, pessoaC]

# for value in pessoas:
# 	if value.getIdade() < 70:
# 		value.printPessoa()