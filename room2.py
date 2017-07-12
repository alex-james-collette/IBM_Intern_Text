##################################
###                            ###
###          ROOM TWO          ###
###                            ###
##################################
from __future__ import division
import time
import os
##############################  STATIC VARIABLES  ##############################

#Name
Name = "Cafeteria"

############################  DESCRIPTION FUNCTIONS  ##########################

#Description
Desctext = """You are in a large room with tables and chairs. In the corner sits a 
popcorn machine."""

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
items = {
	"gold" : 0
}

###################################  ACTIONS  ##################################

#NAVIGATION
directions = {
	"west" : "room1",
	"south" : "room4"
}

#Special Actions
specials = {
}
