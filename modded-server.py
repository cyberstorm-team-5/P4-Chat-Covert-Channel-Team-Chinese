
import socket
import sys
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 5553
s.bind(('138.47.132.186', port))
print ('Socket binded to port ', port)
s.listen(3)
print ('socket is listening')
message = [0,1,1,0,1,0,0,0,0,1,1,0,0,1,0,1,0,1,1,0,1,1,0,0,0,1,1,0,1,1,0,0,0,1,1,0,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,0,1,1,1,1,0,1,1,1,0,0,1,0,0,1,1,0,1,1,0,0,0,1,1,0,0,1,0,0] 
while (True):
	(clientsocket, address) = s.accept()
	print ('Got connection from ', address)
	output = "iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii"
	x = 1
	c = 0
	for i in output:
		clientsocket.send(i)
		x = message[c]
		if x == 1:
			time.sleep(.1)
			x = 0
		else:
			time.sleep(.025)
			x = 1	
		c += 1
		
	clientsocket.send("EOF")
	clientsocket.close()
