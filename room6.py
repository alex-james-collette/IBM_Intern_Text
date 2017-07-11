##################################
###                            ###
###          ROOM SIX          ###
###                            ###
##################################

##############################  STATIC VARIABLES  ##############################

#Name
Name = "East-West Hallway"

#Description
Description = """Hallway leading from cubicles to game room. There is a door to the North that 
leads to a training room."""

##############################  DYNAMIC VARIABLES  #############################

# Whether or not visited yet
Visited = 0

###################################  ACTIONS  ##################################

# NAVIGATION
directions = {
	"west" : "room5",
	"north" : "room7",
	"east" : "room8"
}

#Special Actions
specials = []
