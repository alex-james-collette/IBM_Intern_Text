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
# 1 to change room, 0 to stay

def north(item):
	changeroom = 0
	nextroom = ""
	return changeroom, nextroom

def south(item):
        changeroom = 1
        nextroom = "room3"
        return changeroom, nextroom

def east(item):
        changeroom = 1
        nextroom = "room2"
        return changeroom, nextroom

def west(item):
        changeroom = 0
        nextroom = ""
        return changeroom, nextroom

def northeast(item):
        changeroom = 0
        nextroom = ""
        return changeroom, nextroom

def northwest(item):
        changeroom = 0
        nextroom = ""
        return changeroom, nextroom

def southeast(item):
        changeroom = 0
        nextroom = ""
        return changeroom, nextroom

def southwest(item):
        changeroom = 0
        nextroom = ""
        return changeroom, nextroom



#Special Actions
