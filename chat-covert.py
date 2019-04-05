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



import socket
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = 'jeangourd.com'
port = 31337

s.connect((ip, port))

data = s.recv(4096)
while (data.rstrip("\n") != "EOF"):
	sys.stdout.write(data)
	sys.stdout.flush()
s.close
