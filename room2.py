##################################
###                            ###
###          ROOM TWO          ###
###                            ###
##################################

##############################  STATIC VARIABLES  ##############################

#Name
Name = "Cafeteria"

#Description
Description = ("You are in a large room with tables and chairs. In the corner sits a popcorn machine.")

##############################  DYNAMIC VARIABLES  #############################

# Whether or not visited yet
Visited = 0

###################################  ACTIONS  ##################################


#NAVIGATION
# 1 to change room, 0 to stay

def north(item):
	changeroom = 0
	nextroom = ""
	return changeroom, nextroom

def south(item):
        changeroom = 1
        nextroom = "room4"
        return changeroom, nextroom

def east(item):
        changeroom = 0
        nextroom = ""
        return changeroom, nextroom

def west(item):
        changeroom = 1
        nextroom = "room1"
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
