import sys
import pickle
import math
import statistics
import random

from gi.repository import Gtk
from teamClass import Team
from judgeClass import Judge
from speakerClass import Speaker
from tournamentClass import Tournament


#############################################################################
#############  FUNCTIONS TO MANAGE THE "ADD TEAM" DIALOG BOX   ##############
#############################################################################

def addATeam(button):
	addTeamBox=builder.get_object("addTeamBox")
	
	#IMPLEMENT ERROR CHECKING FOR NEW TEAMS!!!!

	teamName=builder.get_object("teamName").get_text()
	spkrOne=builder.get_object("spkrOne").get_text()
	spkrTwo=builder.get_object("spkrTwo").get_text()
		
	spkrOneNovice=builder.get_object("NoviceStatus1").get_active()
	spkrTwoNovice=builder.get_object("NoviceStatus2").get_active()

	teamAffilIndex=builder.get_object("affilComboBox").get_active()
	seedIndex=builder.get_object("seed").get_active()
	
	teamAffil=builder.get_object("schoolOptions")[teamAffilIndex][0]
	seed=builder.get_object("seedOptions")[seedIndex][0]

	if not builder.get_object("HybridStatus").get_active():
		spkrOneSchool=teamAffil
		spkrTwoSchool=teamAffil
	else:
		spkrOneSchoolIndex=builder.get_object("Spkr1Affil").get_active()
		spkrTwoSchoolIndex=builder.get_object("Spkr2Affil").get_active()
		spkrOneSchool=builder.get_object("schoolOptions")\
				[spkrOneSchoolIndex][0]
		spkrTwoSchool=builder.get_object("schoolOptions")\
				[spkrTwoSchoolIndex][0]


	#puts all our data into a new team in the main LIST OF ALL TEAMS
	listOfAllTeams.append(Team(teamName,spkrOne,spkrTwo,teamAffil,\
			spkrOneSchool, spkrTwoSchool, spkrOneNovice, \
			spkrTwoNovice, seed))

	#call the update to bring everything into the main speaker tab then 
	#clean up your mess.
	updateTeamList()
	clearAddATeamBox()
	addTeamBox.hide()


def clearAddATeamBox():
	teamName=builder.get_object("teamName").set_text("")
	spkrOne=builder.get_object("spkrOne").set_text("")
	spkrTwo=builder.get_object("spkrTwo").set_text("")
	
	teamAffil=builder.get_object("affilComboBox").set_active(-1)
	builder.get_object("Spkr1Affil").set_active(-1)
	builder.get_object("Spkr2Affil").set_active(-1)
	
	spkrOneNovice=builder.get_object("NoviceStatus1").set_active(False)
	spkrTwoNovice=builder.get_object("NoviceStatus2").set_active(False)

	builder.get_object("seed").set_active(0)

	builder.get_object("HybridStatus").set_active(False)

def updateTeamList():
	team_list=builder.get_object("teamList")
	team_list.clear()

	for i in range(0,len(listOfAllTeams)):
		listOfAllTeams[i].updateSpeaksAndRanks()
		t=team_list.append([listOfAllTeams[i].name, \
				    listOfAllTeams[i].spkr1.name, \
				    listOfAllTeams[i].spkr2.name, \
				    listOfAllTeams[i].totalSpeaks, \
				    listOfAllTeams[i].totalRanks, \
				    listOfAllTeams[i].totalWins])
		

def exitTeamAdder(button):
	addTeamBox=builder.get_object("addTeamBox")
	clearAddATeamBox()
	addTeamBox.hide()

def openTeamAdder(button):
	addTeamBox=builder.get_object("addTeamBox")
	addTeamBox.show_all()
	toggleHybridStatus(button)


def toggleHybridStatus(button):
	#Show and hide the extra row of information (The individuals' schools)
	#when the hybrid status is toggled

	hybridButton=builder.get_object("HybridStatus")
	hybridStatus=hybridButton.get_active()	

	if hybridStatus==True:		
		builder.get_object("School Affiliation1").show_all()
		builder.get_object("School Affiliation2").show_all()
		builder.get_object("Spkr1Affil").show_all()
		builder.get_object("Spkr2Affil").show_all()
		builder.get_object("addASchool1").show_all()
		builder.get_object("addASchool2").show_all()

	elif hybridStatus==False:
		builder.get_object("addASchool1").hide()
		builder.get_object("addASchool2").hide()

		builder.get_object("School Affiliation1").hide()
		builder.get_object("School Affiliation2").hide()
		builder.get_object("Spkr1Affil").set_active(-1)
		builder.get_object("Spkr2Affil").set_active(-1)
		builder.get_object("Spkr1Affil").hide()
		builder.get_object("Spkr2Affil").hide()

##############################################################################
############### FUNCTIONS TO ADD SCHOOLS TO THE TOURNAMENT ###################
##############################################################################

def addASchoolOpen(button):

	
	schoolAdder=builder.get_object("schoolAdder").show_all()
	
	builder.get_object("schoolAdderEntry").set_text("")

def addASchoolOkay(button):
	newSchool=builder.get_object("schoolAdderEntry").get_text()
	
	#Error Checking
	if newSchool=="":
		callAnError("You need to enter a school name.")
		return
	print(builder.get_object("schoolOptions"))
	schoolOpts=[]
	for i in range(0,len(builder.get_object("schoolOptions"))):
		schoolOpts.append(builder.get_object("schoolOptions")[i][0])
	if (newSchool in schoolOpts):
		callAnError("You already added this school.")
		return

	schoolList=builder.get_object("schoolOptions")
	schoolList.prepend([newSchool])
	
	builder.get_object("schoolAdder").hide()
	
def addASchoolCancel(button):
	builder.get_object("schoolAdder").hide()
	



#############################################################################
########          THESE FUNCTIONS DEAL WITH OPENING FILES         ###########
#############################################################################

def openFileBox(button):
	openBox=builder.get_object("openBox")
	openBox.show_all()

def exitOpenBox(button):
	openBox=builder.get_object("openBox")
	filePreview=builder.get_object("filePreview")
	filePreview.set_text("")
	openBox.hide()

def selectAFile(selection):
	openBox=builder.get_object("openBox")
	print(openBox.get_preview_filename())
	filePreview=builder.get_object("filePreview")
	filePreview.set_text(openBox.get_preview_filename())

def openAFile(button):
	openBox=builder.get_object("openBox")
	filePreview=builder.get_object("filePreview")
	fileName=filePreview.get_text()
	
	with open(fileName, 'rb') as input:
		mainTournament=pickle.load(input)
	global listOfAllTeams #Declare that we are editing a global variable
	global listOfAllJudges #Declare that we are editing a global variable
	listOfAllTeams=mainTournament.listOfTeams
	listOfAllJudges=mainTournament.listOfJudges
	
	
	filePreview.set_text("")
	openBox.hide()
	updateTeamList()
	updateJudges()
	print ("updated teamlist, apparently")


#############################################################################
########			SAVING FUNCTIONS		   ##########
#############################################################################

def openSaveBox(button):
	saveBox = builder.get_object("saveBox")
	saveBox.show_all()

def selectASaveFile(button):
	saveBox= builder.get_object("saveBox")
	filePreview=builder.get_object("save_preview_entry")
	filePreview.set_text(saveBox.get_preview_filename())

def saveToFile(button):
	print("called save to file")
	filePreview=builder.get_object("save_preview_entry")
	mainTournament=Tournament(listOfAllTeams,listOfAllJudges)

	with open(filePreview.get_text(), 'wb') as output:
		pickle.dump(mainTournament, output, pickle.HIGHEST_PROTOCOL)

	builder.get_object("saveBox").hide()


#############################################################################
########      	   FUNCTIONS TO HANDLE MAIN TAB EDIITNG	 	   ##########
#############################################################################
def activatedARow(trashVariable, row, columnObject):
	
	print("We activated a row! Cool!")




#############################################################################
########      	 	  FUNCTIONS TO CALCULATE SEEDS 	 	   ##########
#############################################################################

def seedingPriorityCancel(button):
	builder.get_object("seeding_Priority_Box").hide()

def seedingPriorityOkay(button):
	builder.get_object("seeding_Priority_Box").hide()

def seedingPriorityBoxOpen(button):
	builder.get_object("seeding_Priority_Box").show_all()


def fixSeed(val, size):
	val=str(val)
	while (len(val) < size):
		val= "0"+val
	return val

def calculateSeeds():
	seedingPriority=[1,2,3,4,5,6,7,8,9,10]
	seeds=[]

	if roundsSoFar==0:
		for i in range(0,len(listOfAllTeams)):
			if listOfAllTeams[i].seeded=="Full":
				seedValue=3
			elif listOfAllTeams[i].seeded=="Free":
				seedValue=3
			elif listOfAllTeams[i].seeded=="Half":
				seedValue=2
			elif listOfAllTeams[i].seeded=="None":
				seedValue=1
			seedValue+=random.random()
			print(seedValue)
			seeds.append(int(seedValue*1000))
		return seeds
	for i in range(0,len(listOfAllTeams)):
		#Wins
		winsSeed=listOfAllTeams[i].totalWins
		winsSeed=str(winsSeed)
	

		#Speaks
		speaksSeed=listOfAllTeams[i].totalSpeaks*100
		speaksSeed=fixSeed(speaksSeed,5)
	
		
		#Ranks
		ranksSeed=listOfAllTeams[i].totalRanks
		ranksSeed=7*roundsSoFar-ranksSeed
		ranksSeed=fixSeed(ranksSeed,2)
	

		#Declare these outside so we can use them later
		rndSpeaks=[]
		rndRanks=[]
		adjSpeaksSeed="00000"
		adjRanksSeed="00"
		dblAdjSpksSeed="00000"
		dblAdjRnksSeed="00"
		
		#Calculate speaks and ranks lists for calculations
		firstSpks=listOfAllTeams[i].spkr1.speaks
		secondSpks=listOfAllTeams[i].spkr2.speaks
		firstRanks=listOfAllTeams[i].spkr1.ranks	
		secondRanks=listOfAllTeams[i].spkr2.ranks
		for j in range(0,len(firstSpks)):
			rndSpeaks.append(firstSpks[j]+secondSpks[j])
			rndRanks.append(firstRanks[j]+secondRanks[j])
		rndSpeaks.sort()
		rndRanks.sort()
		adjSpeaks=rndSpeaks
		
		#Do adjusted speaks and ranks
		if roundsSoFar>=3:
		
			adjRanks=rndRanks
			adjSpeaks.pop(0)
			adjSpeaks.pop(-1)
			adjRanks.pop(0)
			adjRanks.pop(-1)
		
			#Adjusted Speaks
			adjSpeaksSeed=sum(adjSpeaks)*100
			adjSpeaksSeed=fixSeed(adjSpeaksSeed,5)
			
			#Adjusted Ranks
			adjRanksSeed=sum(adjRanks)
			adjRanksSeed=(7*(roundsSoFar-2))-adjRanksSeed
			adjRanksSeed=fixSeed(adjRanksSeed,2)
			

		if roundsSoFar>=5:
			#Calculate and apply double adj ranks
			rndSpeaks.pop(0)
			rndSpeaks.pop(0)
			rndSpeaks.pop(-1)
			rndSpeaks.pop(-1)
			rndRanks.pop(0)
			rndRanks.pop(0)
			rndRanks.pop(-1)
			rndRanks.pop(-1)
		
			#Double Adjusted Speaks
			dblAdjSpks=sum(rndSpeaks)*100
			dblAdjSpksSeed=fixSeed(dblAdjSpks,5)
			
			#Double Adjusted Ranks
			dblAdjRnks=sum(rndRanks)
			dblAdjRnks=7*(roundsSoFar-4)-dblAdjRnks
			dblAdjRnksSeed=fixSeed(dblAdjRnks,2)
		

		#Standard Deviation of Speaks
		sd=statistics.pstdev(rndSpeaks)
		stdDevSpksSeed=(math.pi/2 - math.atan(sd))*100
		stdDevSpksSeed=fixSeed(int(stdDevSpksSeed),3)

		
		
		#Wins of previous opponents
		oppsWins=0
		for j in range(0,len(listOfAllTeams[i].opponents)):
			for k in range(0,len(listOfAllTeams)):
				if listOfAllTeams[i].opponents[j]==\
						listOfAllTeams[k].name:
						oppsWins+=listOfAllTeams[k].\
							totalWins
		oppsWinsSeed=fixSeed(oppsWins,2)
	
		#Coin Flip Tiebreaker
		randSeed=str(random.random())
	

		#Add them all up using my very own INTEGER CONCATENATION
		tempSeeds=[winsSeed, speaksSeed, ranksSeed, adjSpeaksSeed, \
		adjRanksSeed, dblAdjSpksSeed, dblAdjRnksSeed, \
		stdDevSpksSeed, oppsWinsSeed, randSeed]
		seedVal=''

		for i in range(0,10):
			seedVal+=tempSeeds[seedingPriority[i]-1]
			
		seeds.append(seedVal)

	return seeds


#############################################################################
########       	        FUNCTIONS TO VIEW TEAM DETAILS	 	   ##########
#############################################################################

def viewTeamDetails(cursorChange):
	#Get the right team!
	mainTreeView=builder.get_object("masterTabTreeView")
	print(mainTreeView)
	print(mainTreeView.get_cursor()[0])
	print("above was my print statement")
	selTeam=(mainTreeView.get_cursor()[0]).get_indices()[0]
	current=listOfAllTeams[selTeam]
	
	#Set the editability (sensitiivity) and which buttons are there
	swapTeamDetailEditability(False)

	#retrieve a TON of object labels and stores them in our 
	#detailLabels list (dLs)
	dLs=[]
	checks=[]
	for i in range(0,10):
		labelName= "editATeam_entry"+str(i)
		dLs.append(builder.get_object(labelName))
	for i in range(0,5):
		labelName= "editATeam_checkbutton"+str(i+1)
		checks.append(builder.get_object(labelName))
		
	dLs[0].set_text(current.name)
	dLs[1].set_text(current.teamAffiliation)
	dLs[2].set_text(str(current.totalWins))
	dLs[3].set_text(str(current.totalSpeaks))
	dLs[4].set_text(str(current.totalRanks))
	checks[0].set_active(current.wasPullUp)
	checks[1].set_active(current.hitPullUp)
	if (current.spkr1.affiliation)!=(current.spkr2.affiliation):
		checks[2].set_active(True)
	else:
		checks[2].set_active(False)
	dLs[5].set_text(current.seeded)
	dLs[6].set_text(current.spkr1.name)
	dLs[7].set_text(current.spkr1.affiliation)
	checks[3].set_active(current.spkr1.novice)
	dLs[8].set_text(current.spkr2.name)
	dLs[9].set_text(current.spkr2.affiliation)
	checks[4].set_active(current.spkr2.novice)
	
	#Now do the individual rounds
	#hide all the rounds, then later we'll reveal the ones we've had so far
	for i in range(0,10):
		builder.get_object("editATeam_round_vbox"+str(i+1)).hide()
	
	#retrieve all relevant objects into the detail info list (dil)
	dil=[]
	for i in range(0,80):
		dil.append(builder.get_object("editATeam_entry"+str(i+10)))
	
	#Populate the information for each round
	for i in range(0,roundsSoFar):

		builder.get_object("editATeam_round_vbox"+str(i+1)).show_all()
		
		#Speaker names
		dil[i*8].set_text(current.judges[i])
		dil[i*8+1].set_text(current.opponents[i])
		if current.govs[i]==0:
			dil[i*8+2].set_text("Opp")
		else:
			dil[i*8+2].set_text("Gov")
		if current.roundWins[i]==0:
			dil[i*8+3].set_text("Loss")
		else:
			dil[i*8+3].set_text("Win")
		dil[i*8+4].set_text(str(current.spkr1.speaks[i]))
		dil[i*8+5].set_text(str(current.spkr1.ranks[i]))
		dil[i*8+6].set_text(str(current.spkr2.speaks[i]))
		dil[i*8+7].set_text(str(current.spkr2.ranks[i]))
	
#############################################################################
########      		FUNCTIONS TO EDIT TEAM DETAILS 	 	   ##########
#############################################################################

def beginEditingATeam(button):
	swapTeamDetailEditability(True)



def teamEditingSaveChanges(button):
	
	mainTreeView=builder.get_object("masterTabTreeView")
	selTeam=(mainTreeView.get_cursor()[0].get_indices())[0]
	current=listOfAllTeams[selTeam]


	#MASSIVE ERROR CHECKING
	
	#retrieve a TON of object labels and stores them in our 
	#detailLabels list (dLs)
	
	
	dLs=[]
	checks=[]
	for i in range(0,10):
		labelName= "editATeam_entry"+str(i)
		dLs.append(builder.get_object(labelName))
	for i in range(0,5):
		labelName= "editATeam_checkbutton"+str(i+1)
		checks.append(builder.get_object(labelName))
		
	current.name=dLs[0].get_text()
	current.teamAffiliation=dLs[1].get_text()
	current.wasPullUp=checks[0].get_active()
	current.hitPullUp=checks[1].get_active()
	current.seeded=dLs[5].get_text()
	current.spkr1.name=dLs[6].get_text()
	current.spkr1.affiliation=dLs[7].get_text()
	current.spkr1.novice=checks[3].get_active()
	current.spkr2.name=dLs[8].get_text()
	current.spkr2.affiliation=dLs[9].get_text()
	current.spkr2.novcie=checks[4].get_active()
	
	#Now do the individual rounds
	#retrieve all relevant objects into the detail info list (dil)
	dil=[]
	for i in range(0,80):
		dil.append(builder.get_object("editATeam_entry"+str(i+10)))
	
	#Populate the information for each round
	for i in range(0,roundsSoFar):

		builder.get_object("editATeam_round_vbox"+str(i+1)).show_all()
		
		#Speaker names
		current.judges[i]=dil[i*8].get_text()
		current.opponents[i]=dil[i*8+1].get_text()
		if dil[i*8+2].get_text()=="Opp":
			current.govs[i]=0
		elif dil[i*8+2].get_text()=="Gov":
			current.govs[i]=1
		else:
			print("PROBLEM, ALLOWED A NON GOV/OPP TO GET THROUGH")
		if dil[i*8+3].get_text()=="Loss":
			current.roundWins[i]=0
		elif dil[i*8+3].get_text()=="Win":
			current.roundWins[i]=1
		else:
			print("ERROR, ALLOWED A NON WIN/LOSS TO GET THROUGH")

		current.spkr1.speaks[i]=int(dil[i*8+4].get_text())
		current.spkr1.ranks[i]=int(dil[i*8+5].get_text())
		current.spkr2.speaks[i]=int(dil[i*8+6].get_text())
		current.spkr2.ranks[i]=int(dil[i*8+7].get_text())
	

	swapTeamDetailEditability(False)
	updateTeamList()


def teamEditingCancel(button):

	
	viewTeamDetails("this is a junk variable to pass in, it won't be used")

	swapTeamDetailEditability(False)


def swapTeamDetailEditability(editable):
	if editable:
		builder.get_object("editingTeamDetailsCancel").show_all()
		builder.get_object("editingTeamDetailsSaveChanges").show_all()
		builder.get_object("beginEditingTeamDetails").hide()
	else:
		builder.get_object("editingTeamDetailsCancel").hide()
		builder.get_object("editingTeamDetailsSaveChanges").hide()
		builder.get_object("beginEditingTeamDetails").show_all()


	for i in range(0,90):
		entryObj=builder.get_object("editATeam_entry"+str(i))
		entryObj.set_sensitive(editable)
	for i in range(0,5):
		check=builder.get_object("editATeam_checkbutton"+str(i+1))
		check.set_sensitive(editable)

#############################################################################
########	   	FUNCTIONS TO RUN AT START UP	 	   ##########
#############################################################################

def initialize():
	initialization=builder.get_object("New Tournament Initialization")
	roundSpinButton=builder.get_object("numberOfRounds")
	adj=Gtk.Adjustment(1, 1, 11, 1, 1, 1)
	roundSpinButton.configure(adj, 1, 0)
	roundSpinButton.set_value(5)
	
	#set up the spin buttons that gtk doesn't like, this is happening in
	#preferences box
	for i in range(1,11):
		spinBtn=builder.get_object("seedingPriority_spinbutton"+str(i))
		adj=Gtk.Adjustment(1, 1, 11, 1, 1, 1)
		spinBtn.configure(adj, 1, 0)
		spinBtn.set_value(i)

	
	builder.get_object("editingTeamDetailsCancel").hide()
	builder.get_object("editingTeamDetailsSaveChanges").hide()
	for i in range(0,10):
		builder.get_object("editATeam_round_vbox"+str(i+1)).hide()
	
	treeView=builder.get_object("masterTabTreeView")
	treeView.set_reorderable(True)


	errorBox=builder.get_object("mainErrorBox")
	image=Gtk.Image()
	image.set_from_file("grumpyCatError.png")

	errorBox.set_image(image)

	initialization.show_all()

	

def setInitialization(button):
	
	roundSpinButton=builder.get_object("numberOfRounds")
	
	#sets the TOTAL ROUND NUMBER
	global totalRounds
	totalRounds = roundSpinButton.get_value_as_int()
	print(totalRounds)

	initialization=builder.get_object("New Tournament Initialization")
	initialization.hide()


	setTabs()

def setTabs():
	notebook=builder.get_object("Main Notebook")
	
	for i in range(10,totalRounds,-1):
		
		notebook.remove_page(i)
	


#############################################################################
########		GENERAL ERROR CHECKING FUNCTIONS	   ##########
#############################################################################

def callAnError(errorMessageText):
	builder.get_object("mainErrorBox").set_markup(errorMessageText)
	builder.get_object("mainErrorBox").show_all()

def admitYourMistake(button):
	builder.get_object("mainErrorBox").hide()




#############################################################################
########	FUNCTIONS TO ADD A NEW JUDGE TO THE TOURNAMENT	   ##########
#############################################################################

def openAddAJudgeBox(button):
	builder.get_object("currentJudgeAffils").clear()
	builder.get_object("addAJudgeBox").show_all()
	for i in range(1,11):
		builder.get_object("checkbutton"+str(i)).set_active(True)
	for i in range(totalRounds+1,11):
		builder.get_object("checkbutton"+str(i)).hide()
	spinButton=builder.get_object("judgeRanking_SpinButton")
	adj=Gtk.Adjustment(1, 0, 101, 1, 1, 1)
	spinButton.configure(adj, 1, 0)
	spinButton.set_value(0)



def addAJudgeBoxOkay(button):
	rounds=[]
	for i in range(1,totalRounds+1):
		rounds.append(builder.get_object("checkbutton"+\
		str(i)).get_active())
	
	name=builder.get_object("newJudgeName_entry1").get_text()
	judgeRank=builder.get_object("judgeRanking_SpinButton").get_value()
	
	affils=[]
	for i in range(0,len(builder.get_object("currentJudgeAffils"))):
		affils.append(builder.get_object("currentJudgeAffils")[i][0])

	
	listOfAllJudges.append(Judge(name, affils, rounds, judgeRank))

	updateJudges()

	
	

	builder.get_object("addAJudgeBox").hide()

def addAJudgeBoxClose(button):
	builder.get_object("addAJudgeBox").hide()


def addAJudgeAffiliation(trashVariable, row, columnObject):
	print("We got into the function")
	school=builder.get_object("schoolOptions")[row][0]
	print(school)
	builder.get_object("currentJudgeAffils").append([school])

def updateJudges():
	viewedList=builder.get_object("judgeList")
	viewedList.clear()
	for i in range(0,len(listOfAllJudges)):
		thisJudge=listOfAllJudges[i]
		viewedList.append([thisJudge.name, thisJudge.rank])

#############################################################################
################	FUNCTIONS TO PAIR ROUNDS!!! 	#####################
#############################################################################

def pairARound(button):
	seeds=calculateSeeds()
	seededTeamList=sortSeededTeams(seeds)
	
	#Create the bracket for this round
	theRound=[[],[]]
	tempBracket=[]
	bracket=[[],[]]
	
	#Make the right number of brackets
	for i in range(roundsSoFar, -1, -1):
		 
		bracket.clear()
		tempBracket.clear()
		bracket=[[],[]]
		tempBracket=[]
		size=len(seededTeamList) #dont want to edit 
					 #the list while iterating
		for j in range(0,size):
			if seededTeamList[0].totalWins==i:
				tempBracket.append(seededTeamList.pop(0))

		#Preliminarily pair this round
		size=len(tempBracket)
		for j in range(0,int(size/2)):
			bracket[0].append(tempBracket[j])
			bracket[1].append(tempBracket[size-1-j])
		
		#Pair in a pull-up or a bye
		if len(tempBracket)%2==1:
			print("odd number of teams in the bracket")
			pullUp=getAPullUp(i, seededTeamList, tempBracket)
			tempBracket.append(pullUp)
			bracket[1].append(pullUp)
		
		conflictsExist=True #Assume there are conflicts
		constraints=["pulllup", "school", "hit", "gov/opps"] #Start with using all four criteria
		while conflictsExist:
			#For loop, each team gets one iteration
			if len(bracket[0])==0:
				#no conflicts in an empty bracket
				conflictsExist=False
				break
			for i in range(0,len(bracket[0])):
				conf=checkConflicts(bracket[0][i],bracket[1][i],constraints)
				#If this pairing has a conflict, we start swapping
				j=0 #declare an iterator
				while conf:
					j+=1;
					swapItems(bracket,[1,i],[1,(i+j)%(len(bracket[1]))])
					conf=checkConflicts(bracket[0][i],bracket[1][i],constraints)
					if conf:
						swapItems(bracket,[1,i],[1,(i+j)%(len(bracket[1]))])
					if j==len(bracket[1]):
						#This means we iterated through all possible pairings
						#and nothing worked out. OH NO! Pop a constraint and break
						conf=True
						print("had to squirrel out")
						break
				if conf==True:
					print("WE HAD TO POP A CONSTRAINT! FUCK!!")
					constraints.pop()
					conflictsExist=False
					break
				elif conf==False:
					conflictsExist=False
		
		for k in range(0,len(bracket[0])):
			theRound[0].append(bracket[0][k])
			theRound[1].append(bracket[1][k])
	updateVisualPairings(theRound)

def getAPullUp(bracketNumber, seedOrderedTeamList, tempBracket):
	if bracketNumber==0:
		#Create a BYE. FUCK
		byeTeam=Team("Bye","None","None","None","None","None",False,
				False,"None")
		return byeTeam
	lowerBracket=[]
	for i in range(0, len(seedOrderedTeamList)):
		#get all teams in the bracket below
		if seedOrderedTeamList[i].totalWins==bracketNumber-1:
			lowerBracket.append(seedOrderedTeamList.pop(i))
	
	#Do this if we pull up from the middle. 
	return lowerBracket[int(len(lowerBracket)/2)]
	
		


def updateVisualPairings(currentRound):
	pairingsGovs=builder.get_object("roundPairingsGov"+str(roundsSoFar+1))
	pairingsOpps=builder.get_object("roundPairingsOpp"+str(roundsSoFar+1))
	pairingsJudge=builder.get_object("roundPairingsJudge"+str(roundsSoFar+1))
	pairingsGovs.clear()
	pairingsOpps.clear()
	pairingsJudge.clear()
	for i in range(0,len(currentRound[0])):
		pairingsGovs.append([currentRound[0][i].name])
	for i in range(0,len(currentRound[1])):
		pairingsOpps.append([currentRound[1][i].name])

def swapItems(array, index1, index2):
	temp=array[index1[0]][index1[1]]
	array[index1[0]][index1[1]]=array[index2[0]][index2[1]]
	array[index2[0]][index2[1]]=temp

def checkConflicts(teamA, teamB, constraints):
	if checkForHittingPullUp(teamA, teamB):
		return True
	if checkForSchoolProtection(teamA,teamB):
		return True
	if checkForAlreadyHit(teamA,teamB):
		return True
	if checkForGovOpps(teamA,teamB):
		return True
	return False


def checkForHittingPullUp(teamA,teamB):
	if (teamA.wasPullUp and teamB.hitPullUp):
		return True
	elif (teamA.hitPullUp and teamB.wasPullUp):
		return True
	else:
		return False

def checkForSchoolProtection(teamA,teamB):
	if (teamA.teamAffiliation == teamB.teamAffiliation):
		return True
	else:
		return False

def checkForAlreadyHit(teamA,teamB):
	for i in range(0,len(teamA.opponents)):
		if (teamB==teamA.opponents[i]):
			return True
		if (teamA==teamB.opponents[i]):
			print("TEAM OPPONENTS WERE NOT UPDATED PROPERTLY")
			return True
	return False

def checkForGovOpps(teamA,teamB):
	maxGovs=3 #THIS IS HARDCODED FOR NOW. CHANGE THIS
	
	if (sum(teamA.govs)>=maxGovs and sum(teamB.govs)>=maxGovs):
		return True
	else:
		return False

def sortSeededTeams(seeds):
	#copy the list before sorting
	seededTeamList=[]
	for i in range(0,len(listOfAllTeams)):
		seededTeamList.append(listOfAllTeams[i])
	for i in range(0,len(seeds)-1):
		for j in range(0,len(seeds)-1):
			if seeds[j]<seeds[j+1]:
				temp=seededTeamList[j]
				seededTeamList[j]=seededTeamList[j+1]
				seededTeamList[j+1]=temp
				
				temp=seeds[j]
				seeds[j]=seeds[j+1]
				seeds[j+1]=temp
	print(seeds)
	return seededTeamList


#############################################################################
########	THIS IS THE MAIN FUNCTIONALITY OF THE PROGRAM	   ##########
#############################################################################


#Declare the handlers. Each one should have a corresponding function of the 
#same name (but without underscores)
handlers= {
    "on_Window_Destroy": Gtk.main_quit,  
    "add_A_Team": addATeam,
    "exit_Team_Adder": exitTeamAdder,
    "open_Team_Adder": openTeamAdder,
    "open_File_Box": openFileBox,
    "exit_Open_Box": exitOpenBox,
    "select_A_File": selectAFile,
    "open_A_File": openAFile,
    "toggle_Hybrid_Status": toggleHybridStatus,
    "open_Save_Box": openSaveBox,
    "select_A_Save_File":selectASaveFile,
    "save_To_File":saveToFile,
    "activated_A_Row":activatedARow,
    "set_Initialization":setInitialization,
    "view_Team_Details":viewTeamDetails,
    "add_A_School_Open": addASchoolOpen,
    "add_A_School_Okay": addASchoolOkay,
    "add_A_School_Cancel": addASchoolCancel,
    "open_Add_A_Judge_Box": openAddAJudgeBox,
    "add_A_Judge_Box_Okay": addAJudgeBoxOkay,
    "add_A_Judge_Box_Close": addAJudgeBoxClose,
    "add_A_Judge_Affiliation":addAJudgeAffiliation,
    "begin_Editing_A_Team": beginEditingATeam,
    "team_Editing_Save_Changes": teamEditingSaveChanges,
    "team_Editing_Cancel": teamEditingCancel,
    "admit_Your_Mistake":admitYourMistake,
    "pair_A_Round": pairARound,
    "seeding_Priority_Box_Open": seedingPriorityBoxOpen,
    "seeding_Priority_Cancel": seedingPriorityCancel,
    "seeding_Priority_Okay": seedingPriorityOkay,
}



#Load the gui into the bulder and get the main objects from the builder
builder = Gtk.Builder()
builder.add_from_file("SwatTABgui.glade")
builder.connect_signals(handlers)
window = builder.get_object("window1")
window.show_all()


#Declare a few global variables. These are the grand lists of teams, 
#speakers, rooms, judges, and integers for the rounds that have been paired so
#far and the total numbe of in-rounds. It's unfortunate to have to use these,
#but the main loop for the GUI is auto-called in the Gtk.main() so these 
#global variables are the clearest way to store this information. The 
#alternatives would be to store them somewhere hidden in the GUI and reaccess 
#them everytime, but I think this is clearer.
listOfAllTeams=[]
listOfAllRooms=[]
listOfAllJudges=[]
roundsSoFar=0
totalRounds=5 #initialize to five as the "default" tournament

mainTournament=Tournament(listOfAllTeams,listOfAllJudges)

#run the main loop
initialize()
Gtk.main()


