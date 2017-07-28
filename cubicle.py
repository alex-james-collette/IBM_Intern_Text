##################################
###             		       ###
### 	     CUBICLE	       ###
###                            ###
##################################

##############################  STATIC VARIABLES  ##############################

#Name
Name = "Cubicle"

###########################  DESCRIPTION FUNCTIONS  ###########################

#Description
Desctext = """You are standing in a partially filled parking lot.
A sign is in front of you. A sidewalk leads to the entrance of a building."""

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
#MUST LIST GOLD
items = {
	"gold" : 0	
}

cabinet - {
    "gold" : 0
    "popcorn": 0,
    "backpack" : [],
    "tropheys" : []
}

###################################  ACTIONS  ##################################

# NAVIGATION
directions = {
	"south" : "room3",
	"east" : "room2"
}

#Special Actions
specials = []
