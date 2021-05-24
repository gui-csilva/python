class cargo:
	def __init__(self, nome, mediaSalarial, horasTrabalhadas):
		self.nome = nome
		self.mediaSalarial = mediaSalarial
		self.horasTrabalhadas = horasTrabalhadas

	def getNome(self):
		return self.nome

	def getMediaSalarial(self):
		return self.mediaSalarial
	
	def getHorasTrabalhadas(self):
		return self.horasTrabalhadas

	def aumentarPercentualSalario(self, percentual):
		self.mediasalarial = self.mediasalarial + (self.mediaSalarial * (percentual/100) )
		return self.getMediaSalarial()

	def setHorasTrabalhadas(self, horasNovas):
		self.horasTrabalhadas = horasNovas
		return self.horasTrabalhadas