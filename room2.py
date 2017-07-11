##################################
###                            ###
###          ROOM TWO          ###
###                            ###
##################################
from __future__ import division
import time
import os
import sys
##############################  STATIC VARIABLES  ##############################

#Name
Name = "Cafeteria"

#Description
Description = """You are in a large room with tables and chairs. In the corner sits a 
popcorn machine."""

##############################  DYNAMIC VARIABLES  #############################

# Whether or not visited yet
Visited = 0

###################################  ACTIONS  ##################################

#NAVIGATION
directions = {
	"west" : "room1",
	"south" : "room4"
}

#Special Actions
specials = {
	"make" : "popcorn"
}

def popcorn():
	counter = 11
	print "popping..."
	original = counter
	while counter > 0:
		length = original - counter
                progressbar = ("=" * 4) * length

                numofwhite = counter - 1 
                white_space = (" " * 4) * numofwhite
		
		percent_done = (length / (original - 1)) * 100
		percent_done = round(percent_done)

		print progressbar, white_space, percent_done, "%              \r",
		sys.stdout.flush()

		time.sleep( .25 )
		counter -= 1
	else:
		print
		print "100 popcorn added to bin!"
		print	
