import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 5550
s.bind(('138.47.136.187', port))
print ('Socket binded to port 5550')
s.listen(3)
print ('socket is listening')
while (True):
	(clientsocket, address) = s.accept()
	print ('Got connection from ', address)
	output = "This is a message from lane arnold EOF"
	for i in output:
		clientsocket.send(i)
