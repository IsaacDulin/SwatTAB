import sys
from gi.repository import Gtk
from teamClass import Team
from speakerClass import Speaker

#############################################################################
#############  METHOD FUNCTIONS TO "DO STUFF" TO THE TEAM LIST  #############

def updateMasterTabView():
	for i in len(listOfAllTeams):
		team_list.clear()
		uselessVariable=team_list.append([listOfAllTeams[i].name, \
				listOfAllTeams[i].spkr1.name, \
				listOfAllTeams[i].spkr2.name, \
				listOfAllTeams[i].wins])

#############################################################################
#############  FUNCTIONS TO MANAGE THE "ADD TEAM" DIALOG BOX   ##############
#############################################################################

def addATeam(button):
	teamName=builder.get_object("teamName").get_text()
	spkrOne=builder.get_object("spkrOne").get_text()
	spkrTwo=builder.get_object("spkrTwo").get_text()
	
	teamAffil=builder.get_object("affil").get_text()
	spkrOneSchool=builder.get_object("Spkr1Affil").get_text()
	spkrTwoSchool=builder.get_object("Spkr2Affil").get_text()
	
	spkrOneNovice=builder.get_object("NoviceStatus1").get_active()
	spkrTwoNovice=builder.get_object("NoviceStatus2").get_active()

	seed=builder.get_object("seed").get_text()
	
	#puts all our data into a new team in the main LIST OF ALL TEAMS
	listOfAllTeams.append(Team(teamName,spkrOne,spkrTwo,teamAffil,\
			spkrOneSchool, spkrTwoSchool, spkrOneNovice, \
			spkrTwoNovice, seed))

	#call the update to bring everything into the main speaker tab then clean up
	#your mess.
	updateTeamList()
	clearAddATeamBox()
	addTeamBox.hide()


def clearAddATeamBox():
	teamName=builder.get_object("teamName").set_text("")
	spkrOne=builder.get_object("spkrOne").set_text("")
	spkrTwo=builder.get_object("spkrTwo").set_text("")
	
	teamAffil=builder.get_object("affil").set_text("")
	spkrOneSchool=builder.get_object("Spkr1Affil").set_text("")
	spkrTwoSchool=builder.get_object("Spkr2Affil").set_text("")
	
	spkrOneNovice=builder.get_object("NoviceStatus1").set_active(False)
	spkrTwoNovice=builder.get_object("NoviceStatus2").set_active(False)

	builder.get_object("seed").set_text("")

def updateTeamList():
	
	team_list.clear()

	for i in range(0,len(listOfAllTeams)):
		t=team_list.append([listOfAllTeams[i].name, \
				    listOfAllTeams[i].spkr1.name, \
				    listOfAllTeams[i].spkr2.name, \
				    listOfAllTeams[i].totalSpeaks, \
				    listOfAllTeams[i].totalRanks, \
				    listOfAllTeams[i].totalWins])
		

def exitTeamAdder(button):
	clearAddATeamBox()
	addTeamBox.hide()

def openTeamAdder(button):
	addTeamBox.show_all()
	toggleHybridStatus(button)


def toggleHybridStatus(button):
	hybridButton=builder.get_object("HybridStatus")
	hybridStatus=hybridButton.get_active()
	
	firstSpeakerSchoolAffil=builder.get_object("School Affiliation1")
	firstSpeakerSchoolAffilEntry=builder.get_object("Spkr1Affil")
	secondSpeakerSchoolAffil=builder.get_object("School Affiliation2")
	secondSpeakerSchoolAffilEntry=builder.get_object("Spkr2Affil")
	if hybridStatus==True:
		
		firstSpeakerSchoolAffil.show_all()
		secondSpeakerSchoolAffil.show_all()
		firstSpeakerSchoolAffilEntry.show_all()
		secondSpeakerSchoolAffilEntry.show_all()
	elif hybridStatus==False:
		firstSpeakerSchoolAffil.hide()
		secondSpeakerSchoolAffil.hide()
		firstSpeakerSchoolAffilEntry.set_text("")
		secondSpeakerSchoolAffilEntry.set_text("")
		firstSpeakerSchoolAffilEntry.hide()
		secondSpeakerSchoolAffilEntry.hide()


#############################################################################
########          THESE FUNCTIONS DEAL WITH OPENING FILES         ###########
#############################################################################

def openFileBox(button):	
	openBox.show_all()

def exitOpenBox(button):
	filePreview=builder.get_object("filePreview")
	filePreview.set_text("")
	openBox.hide()

def selectAFile(selection):
	print(openBox.get_preview_filename())
	filePreview=builder.get_object("filePreview")
	filePreview.set_text(openBox.get_preview_filename())

def openAFile(button):
	print("We opened a file")
	filePreview=builder.get_object("filePreview")
	fileName=filePreview.get_text()
	actualFile=open(fileName)
	print(actualFile.read())



	filePreview.set_text("")
	openBox.hide()




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
}

#Load the gui into the bulder and get the main objects from the builder
builder = Gtk.Builder()
builder.add_from_file("SwatTABgui.glade")
builder.connect_signals(handlers)
window = builder.get_object("window1")
window.show_all()


#Any objects that require function calls on them (more than in a local setting)
#will be "gotten" here. These are effectively global variables.
team_list=builder.get_object("teamList")
addTeamBox=builder.get_object("addTeamBox")
openBox=builder.get_object("openBox")


#Define any actual global variables. These are the grand lisst of teams, 
#speakers, rooms, and judges.
listOfAllTeams=[]
listOfAllRooms=[]
listOfAllSpeakers=[]
listOfAllJudges=[]


#run the main loop
Gtk.main()


