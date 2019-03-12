import socket, math as m

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#bind
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 26210
server.bind((host,port))
print(ip)
#listen
server.listen(5)

while True:
    # init & accept
	dim = 0
	client, addr = server.accept()
	
	# read & create filename
	filename = client.recv(1024)
	filename = filename.decode('utf-8') + "_server"
	fn = open(filename,'wb')
	client.send(b'\x01\x02\x03\x04')	# for synchron

    # read data
	X = 1024
	while True:
		data = client.recv(X)
		dim += len(data)
		fn.write(data)
		if (len(data) < X):
			break	

    #write
	confirm = "Received all " + str(dim) + " bytes"
	tosend = bytearray(confirm,'utf-8')
	client.send(tosend)

	#confirm
	print("Finished receiving from " + str(addr))

    #close
	client.close()
