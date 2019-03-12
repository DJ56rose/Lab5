import socket, sys, os

# accept server IP, file
if (len(sys.argv) != 3):
	print("ERROR: wrong number of arguments")
	exit()
IP = sys.argv[1]
filename = sys.argv[2]

# error check
try: fn = open(filename,"rb")
except:
    print("ERROR: invalid filename")
    exit()
IPnums = IP.split('.')
if len(IPnums) != 4:
    print("ERROR: Incorrect IP format")
    exit()

# initialize socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = 12346
host = socket.gethostname()
print(host)
#connect
s.connect((host,port))
filesize = os.path.getsize(filename)
print("FROM CLIENT: sending "+str(filesize)+" bytes")

# send filename
filename = bytearray(filename,'utf-8')
s.sendall(filename)

# === loop through file ===
X = 1024
info = fn.read(X)
data = info	#for tracking
while info:
	# send over link
	s.sendall(info)	
	# read again
	info = fn.read(X)
	data += info

# receive confirmation
msg = "FROM SERVER: " + str(s.recv(1024))
print(msg)
s.close()
#print(data)
