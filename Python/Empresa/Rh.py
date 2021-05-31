import Pessoa
class Rh:
	def __init__(self, pessoa):
		self.pessoa = pessoa

	def salarioComPlr(self):
		salario = self.pessoa.getSalario()
		bonus = self.pessoa.getSalario() * 2.5
		plr = salario + bonus
		return plr

	def plr(self):
		bonus = self.pessoa.getSalario() * 2.5
		return bonus		