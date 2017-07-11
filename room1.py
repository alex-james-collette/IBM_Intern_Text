##################################
###         		       ###
### 	     ROOM ONE	       ###
###                            ###
##################################

##############################  STATIC VARIABLES  ##############################

#Name
Name = "Front Parking Lot"

#Description
Description = """You are standing in a partially filled parking lot.
A sign is in front of you. A sidewalk leads to the entrance of a building."""

##############################  DYNAMIC VARIABLES  #############################

# Whether or not visited yet
Visited = 0

###################################  ACTIONS  ##################################

# NAVIGATION
directions = {
	"south" : "room3",
	"east" : "room2"
}

#Special Actions
specials = []
