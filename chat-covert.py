################################################################################
# Authors: Team Chinese (Lane Arnold, Christopher Boquet,
# 	   Christopher Bouton, Darrell Durousseaux, Clay Fonseca,
#	   Rebecca Grantham, Andrew Maurice)
# Class: CSC 442
# Date: 4-26-2019
# Github Repo: https://github.com/cyberstorm-team-5/P4-Chat-Covert-Channel-Team-Chinese
# Description: Program 4: Chat (Timing) Covert Channel
#              The Python code will extract a covert message based on delays
#              between characters of a chat server's transmitted message. It
#              outputs the overt message as it is received and automatically
#              disconnects from the server once it is complete, displaying the
#              covert message in stdout as well.
################################################################################

import ftplib
################################################################################

#global var to select mode (0 (7-bit) or 1 (10-bit))
METHOD = 0
#global var for the string of the FTP server to connect to
SERVER = 'www.jeangourd.com'
#global var for directory within server to retrieve file permissions info from
DIR = '7'

#data retrieved from server is stored here
data = []

################################################################################


########NOTE: THE BELOW CODE IS FROM PROGRAM 3, LEFT HERE BECAUSE IT MAY HELP FOR
#####THIS ONE, BUT IF NOT WE CAN DELETE IT FROM HERE


#append all permissions data in the DIR directory in the server to the data array
def retrieveData():
	server.dir(DIR, data.append)

	#loop through each line of data retrieved (1 line/index of the data array)
	for i in range(len(data)):
		#remove all but the first 10 characters of each line (only want
		#the permissions info)
		data[i] = data[i][0:10]
		i=i+1



#####################################MAIN#######################################

#setup connection to server
server = ftplib.FTP()
server.connect(SERVER)
server.login('anonymous')

#retrieve the permissions data from server
retrieveData()
#generate the binary string and print the 7-bit ASCII version
genString()



