####################################
###                              ###
###          ROOM THREE          ###
###                              ###
####################################

##############################  STATIC VARIABLES  ##############################

#Name
Name = "Entry Hall"

############################# DESCRIPTION FUNCTIONS ############################

#Description
Desctext = """You are standing in a entry way made of glass. to the East are doors 
with access card scanners. A security gaurd sits nearby, reading a magazine."""

def Description():
	if items['gold'] > 0:
		Final = Desctext + """ There is some gold in the corner."""
	else:
		Final = Desctext
	return Final

##############################  DYNAMIC VARIABLES  #############################

# Whether or not visited yet
Visited = 0

#Items in room
#MUST LIST GOLD, PUT 0 IF NONE
items = {
	"gold" : 10
}

###################################  ACTIONS  ##################################

# NAVIGATION
directions = {
	"north" : "room1",
	"east" : "room8"
}

#Special Actions
specials = []
