#Creates a Team Class to store team data
from speakerClass import Speaker

class Team:
	def __init__(self, teamName, firstSpeaker, secondSpeaker, teamSchool,\
			firstSchool, secondSchool, firstNovice,\
			secondNovice, seed):
	
		#Variables defined by constructor
		self.name=teamName
		self.spkr1=Speaker(firstSpeaker, firstSchool, firstNovice)
		self.spkr2=Speaker(secondSpeaker, secondSchool, secondNovice)
		self.teamAffiliation=teamSchool
		self.seeded=seed
		
		#initializations for all teams (they haven't had any rounds yet)
		self.judges=[]
		self.opponents=[]
		self.wasPullUp=False
		self.hitPullUp=False
		self.govs=[0,0,0,0,0]
		self.roundWins=[0,0,0,0,0]
		self.totalWins=0
		self.totalSpeaks=0
		self.totalRanks=0
	
	
	
	def changeTeamName(self, newTeamName):
		self.name=newTeamName
	
	def changeSeed(self, newSeed):
		self.seeded=seed
	
	def changeTeamAffiliation(self, newSchool):
		self.teamAffiliation=newSchool
	def changeSpeakerOneName(self, newName):
		self.spkr1.changeName(newName)
	def changeSpeakerTwoName(self, newName):
		self.spkr2.changeName(newName)
	
	def updateARoundResult(self, roundNumber, opponent, judge, goved, \
			       win_loss, spkr1Spks, spkr2Spks, spkr1Ranks, \
			       spkr2Ranks):

		self.opponents[roundNumber]=opponent
		self.judges[roundNumber]=judge
		self.govs[roundNumber]=goved
		self.wins[roundNumber]=win_loss
		self.spkr1.speaks[roundNumber]=spkr1Spks
		self.spkr2.speaks[roundNumber]=spkr2Spks
		self.spkr1.ranks[roundNumber]=spkr1Ranks
		self.spkr2.ranks[roundNumber]=spkr2Ranks

		self.totalSpeaks=sum(self.spkr1.speaks)+sum(self.spkr2.speaks)
		self.totalRanks=sum(self.spkr1.ranks)+sum(self.spkr2.ranks)
		self.totalWins=sum(self.roundWins)
	
	def wasPullUp(self):
		self.wasPullUp=True
	def hitPullUp(self):
		self.hitPullUp=True
	

	

