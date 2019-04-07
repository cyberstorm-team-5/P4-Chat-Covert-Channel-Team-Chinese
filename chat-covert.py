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

from time import time
import socket
import sys
################################################################################

#LANE'S SERVER INFO
#ip = '138.47.136.187'
#port = 5553

#CLAY'S SERVER INFO
IP = "138.47.132.186"
PORT = 5553

#the times that output a 1 or 0 for the covert message, respectively
TIME_ONE = .1
TIME_ZERO = 0.025
#use average time to account for variation
TIME_AVG = (TIME_ONE + TIME_ZERO)/2


################################################################################

#process input as a sequence of 7- or 8-bit ascii code to convert to a readable string
#NOTE: this function is retrieved from ours group's binary decoder (program 1)
def convertASCII(binaryInput, binaryLength, numBits):
	
	finalString = ""
	
	#loop through indexes such that i = the 0th bit in every sequence of numBits
	#(7 or 8) bits in the binaryInput
	for i in range(0, binaryLength-(numBits-1), numBits):

		#get the ASCII number for the bits
		num = int(binaryInput[i:i+numBits], 2)

		#check if the num will produce a backspace (ASCII 8)
		if(num == 8):
			#remove the trailing character from the string
			finalString = finalString[:-1]
		   
		else:
			#convert the 7 or 8 bits into an integer form base 2, then use chr
			#to convert the integer into the equivalent ASCII character
			finalString += chr(num)
		
	print(finalString)
	return


#display the overt message and generate the bits of the covert message based on
#the timing of retrieving the characters (delays between characters
def retrieveMessages(s):

        #hold the binary for the covert message
        covertBin = ""

        #retrieve the first char outside the loop (only care about timing
        #between the characters)
        data = s.recv(4096)

        #continue to loop until an EOF signal is received
        while (data.rstrip("\n") != "EOF"):

                #display the current character being held
                sys.stdout.write(data)
                sys.stdout.flush()

                #time the retrieval of the next character
                start = time()
                data = s.recv(4096)
                end = time()

                #determine what range the time falls into for
                #adding a 1 or 0 to the covert string
                delta = round(end-start, 3)
                #use the average time to account for variations (ex: if time 1 is
                #".1" and the delay was ".09" it should be a binary 1, but if we
                #used "delta >= TIME_ONE", we would get a 0)
                if(delta >= TIME_AVG):
                        covertBin += "1"
                else:
                        covertBin += "0"

		
###############################MAIN#############################################

#setup connection to server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(IP, PORT)

covertBin = retrieveMesssages(s)

#close out of the server and display the converted output
s.close()
print(covertBin)
convertASCII(covertBin, len(covertBin), 8)


