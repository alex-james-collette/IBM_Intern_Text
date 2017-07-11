###################################
###                             ###
###          ROOM FIVE          ###
###                             ###
###################################

##############################  STATIC VARIABLES  ##############################

#Name
Name = "Pod 2"

#Description
Description = """You are in a pod of cubicles. Several people are sitting here working.
You think one of them is your new boss."""

##############################  DYNAMIC VARIABLES  #############################

# Whether or not visited yet
Visited = 0

###################################  ACTIONS  ##################################

# NAVIGATION
directions = {
	"west" : "room4",
	"east" : "room6"
}

#Special Actions
specials = []
