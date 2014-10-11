#Creates a class to store individual speakers. Two of these will be member 
#variables of each team class. These will primarily be used to tab the top 
#speakers.

class Speaker: 
	def __init__(self, spkrName, affil, novice):
		self.name=spkrName
		self.affiliation=affil

		self.speaks=[0,0,0,0,0]
		self.ranks=[0,0,0,0,0]

		self.novice=novice
		
		self.update()

	def update(self):
		self.totalSpeaks=sum(self.speaks)

		self.totalRanks=sum(self.speaks)

	def changeName(self, newName):
		self.name=newName

	def changeAffil(self, newAffil):
		self.affiliation=newAffil
	
	def changeNoviceStatus(self, newNoviceStatus):
		self.novice=newNoviceStatus

	def inputSpeaks(self, roundNumber, speaks):
		self.speaks[roundNumber]=speaks
	
	def inputRanks(self, roundNumber, ranks):
		self.ranks[roundNumber]=ranks
		
