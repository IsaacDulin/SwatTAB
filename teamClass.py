#Creates a Team Class to store team data
from speakerClass import Speaker

class Team:
	def __init__(self):
		self.name="testName"
		self.spkr1=Speaker("Jodie")
		self.spkr2=Speaker("Will")
		self.wins=0
		self.seeded=0
		self.govs=0
		self.judges=[]
		self.opponents=[]
		self.wasPullUp=False
		self.hitPullUp=False
		self.teamAffiliation="Harvard"

	

