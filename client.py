import socket, sys

# accept server IP, file

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

# === loop through file ===
X = 1024
data = ""
info = fn.read(X)
while info:
    # send over link
    
    # read again
    info = fn.read(X)
    print(info)
    #print(info)
print(data)
