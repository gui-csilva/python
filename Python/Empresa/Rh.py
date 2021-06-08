import Pessoa
class Rh:
	def __init__(self, pessoa):
		self.pessoa = pessoa
		self.ferias = False

	def salarioComPlr(self):
		salario = self.pessoa.getSalario()
		bonus = self.pessoa.getSalario() * 2.5
		plr = salario + bonus
		return plr

	def plr(self):
		bonus = self.pessoa.getSalario() * 2.5
		return bonus

	def setFerias(self, ferias):
		self.ferias = ferias

	def getFerias(self):
		return self.ferias

	def valorFerias(self):
		tercoSalario = self.pessoa.getSalario() / 3
		return tercoSalario

	def retornarSalarioComTerco(self):
		tercoSalario = self.pessoa.getSalario() / 3
		resultadoTerco = self.pessoa.getSalario() + tercoSalario
		return resultadoTerco