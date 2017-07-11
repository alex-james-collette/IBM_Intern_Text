##################################
###                            ###
###          ROOM SIX          ###
###                            ###
##################################

##############################  STATIC VARIABLES  ##############################

#Name
Name = "East-West Hallway"

#Description
Description = "Hallway leading from cubicles to game room. There is a door to the North that leads to a training room."

##############################  DYNAMIC VARIABLES  #############################

# Whether or not visited yet
Visited = 0

###################################  ACTIONS  ##################################

# NAVIGATION
# 1 to change room, 0 to stay

def north(item):
        changeroom = 1
        nextroom = "room7"
        return changeroom, nextroom

def south(item):
        changeroom = 0
        nextroom = ""
        return changeroom, nextroom

def east(item):
        changeroom = 1
        nextroom = "room8"
        return changeroom, nextroom

def west(item):
        changeroom = 1
        nextroom = "room5"
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
