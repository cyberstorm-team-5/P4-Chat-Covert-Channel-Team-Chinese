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
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = '138.47.136.187'
port = 5550

#hold the binary for the covert message
covertBin = ""
#the times that output a 1 or 0 for the covert message, respectively
TIME_ONE = 1
TIME_ZERO = 0.25


s.connect((ip, port))

#data = s.recv(4096)
while (data.rstrip("\n") != "EOF"):
        start = time()
        data = s.recv(4096)
        end = time()

        delta = round(end-start, 3)
        if(delta >= TIME_ONE):
                covertBin += "1"
        else:
                covertBin += "0"
        
	sys.stdout.write(data)
	sys.stdout.flush()
s.close()

print(covertBin)


