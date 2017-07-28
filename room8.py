####################################
###                              ###
###          ROOM EIGHT          ###
###                              ###
####################################

##############################  STATIC VARIABLES  ##############################

#Name
Name = "Game Room"

############################# DESCRIPTION FUNCTIONS ############################

#Description
Desctext = """You are standing in a large, well lit room with several games, including 
Ping-Pong, ShuffleBoard, and a putting green."""

def Description():
	if True:
		Final = Desctext
	else:
		Final = Desctext
	return Final

##############################  DYNAMIC VARIABLES  #############################

# Whether or not visited yet
Visited = 0

#Items in room
#MUST LIST GOLD, PUT 0 IF NONE
items = {
        "gold" : 0
}

###################################  ACTIONS  ##################################

# NAVIGATION
directions = {
	"west" : "room3"
}

#Special Actions
specials = []
