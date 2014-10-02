#Creates a class to store individual speakers. Two of these will be member 
#variables of each team class

class Speaker: 
	def __init__(self):
		self.name="john"
		
		self.roundOneSpeaks=0
		self.roundTwoSpeaks=0
		self.roundThreeSpeaks=0
		self.roundFourSpeaks=0
		self.roundFiveSpeaks=0
		self.roundSixSpeaks=0

		self.roundOneRanks=0
		self.roundTwoRanks=0
		self.roundThreeRanks=0
		self.roundFourRanks=0
		self.roundFiveRanks=0

		self.totalSpeaks=0
		self.totalRanks=0
		self.affiliation="Swarthmore"
	def __init__(self, testvar):
		self.name=testvar

	def update(self):
		self.totalSpeaks=self.roundOneSpeaks+self.roundTwoSpeaks+\
				self.roundThreeSpeaks+self.roundFourSpeaks+\
				self.roundFiveSpeaks

		self.totalRanks=self.roundOneRanks+self.roundTwoRanks+\
				self.roundThreeRanks+self.roundFourRanks+\
				self.roundFiveRanks
	def changeName(self, newName):
		self.name=newName
	def changeAffil(self, newAffil):
		self.affiliation=newAffil
	
