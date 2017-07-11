###################################
###                             ###
###          ROOM FOUR          ###
###                             ###
###################################

##############################  STATIC VARIABLES  ##############################

#Name
Name = "Empty Pod"

#Description
Description = """You are in an area of empty cubicles, desolate spare for a pile of telephones. 
Nobody works here."""

##############################  DYNAMIC VARIABLES  #############################

# Whether or not visited yet
Visited = 0

###################################  ACTIONS  ##################################

# NAVIGATION
directions = {
	"west" : "room3",
	"north" : "room2",
	"east" : "room5"
}

#Special Actions
specials = []
