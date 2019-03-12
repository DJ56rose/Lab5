import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#bind
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 12346
server.bind((host,port))
print(host)
#listen
server.listen(5)

while True:
    # accept
	client, addr = server.accept()
	
	# read & create filename
	filename = client.recv(1024)
	filename = filename.decode('utf-8') + "_server"
	fn = open(filename,'wb')
	#print("Just opened stuff...")	
    # read data
	X = 1024
	while True:
		data = client.recv(X)
		fn.write(data)
		print(len(data))
		if (len(data) < 1024):
			
			X = len(data)
			print("Breaking...")
			break

    #write
	confirm = "Received all " + str(len(data)) + " bytes"
	tosend = bytearray(confirm,'utf-8')
	client.send(tosend)
    #close
	client.close()
