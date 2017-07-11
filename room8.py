####################################
###                              ###
###          ROOM EIGHT          ###
###                              ###
####################################

##############################  STATIC VARIABLES  ##############################

#Name
Name = "Game Room"

#Description
Description = "You are standing in a large, well lit room with several games, including Ping-Pong, ShuffleBoard, and a putting green."

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
        changeroom = 0
        nextroom = ""
        return changeroom, nextroom

def east(item):
        changeroom = 0
       	nextroom = ""
        return changeroom, nextroom

def west(item):
        changeroom = 1
        nextroom = "room6"
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
