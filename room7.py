####################################
###                              ###
###          ROOM SEVEN          ###
###                              ###
####################################

##############################  STATIC VARIABLES  ##############################

#Name
Name = "Training Room"

#Description
Description = "You are in a room set up as a classroom, with a large table. It seems to be used for training and teaching new skills."

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
        nextroom = "room6"
        return changeroom, nextroom

def east(item):
        changeroom = 0
       	nextroom = ""
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
