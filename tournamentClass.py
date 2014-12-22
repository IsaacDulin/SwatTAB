from speakerClass import Speaker
from teamClass import Team

#A simple class just designed to store the many lists that are created in the
#course of the tournament. This single object will contain all the data
#and will be pickled to a file for saving.

class Tournament:
	def __init__(self, listOfAllTeams, listOfAllJudges):
		self.listOfTeams=listOfAllTeams
		self.listOfJudges=listOfAllJudges
