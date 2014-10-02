import sys
from gi.repository import Gtk
from teamClass import Team
from speakerClass import Speaker

#FUNCTIONS
def messWithLists(list):
	treeiter=list.append(["team","roy","jane",2])
	treeiter2=list.append(["teamb","elisa","john",3])
	treeiter3=list.append(["teamc","sara","isaac",5])
	print( len(list))
	return

def test(button):
	print("test worked!")
	treeiter=team_list.append(["teamx","girl","guy",1])

def addTeam(button):

	teamName=builder.get_object("teamName")
	spkrOne=builder.get_object("spkrOne")
	spkrTwo=builder.get_object("spkrTwo")
	affil=builder.get_object("affil")
	seed=builder.get_object("seed")

	#firstSpeaker=Speaker(spkrOne.get_text())
	#secondSpeaker=Speaker(spkrTwo.get_text())
	
	treeiter=team_list.append([teamName.get_text(), 
			spkrOne.get_text(), spkrTwo.get_text(), 0])
	
def exitTeamAdder(button):
	addTeamBox.hide()

def openTeamAdder(button):
	
	addTeamBox.show_all()
	print("called openTeamAdder")


#Create the handlers. Each handler corresponds to a button or action received
#from the GUI and should call a function in response.
handlers= {
    "on_window_destroy": Gtk.main_quit,  
    "onButtonPressed": test,
    "add_a_Team": addTeam,
    "exit_Team_Adder": exitTeamAdder,
    "open_Team_Adder": openTeamAdder
}

#Load the gui and put objects into the builder
builder = Gtk.Builder()
builder.add_from_file("SwatTABgui.glade")
builder.connect_signals(handlers)
window = builder.get_object("window1")
window.show_all()


testTeam=Team()
print(testTeam.spkr1.name)



#Any objects that require function calls on them (more than in a local setting)
#will be "gotten" here
team_list=builder.get_object("teamList")
addTeamBox=builder.get_object("addTeamBox")

messWithLists(team_list)







#run the program
Gtk.main()


