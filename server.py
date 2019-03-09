import socket

s = socket.socket()

#bind
host = socket.gethostname()
port = 12345
s.bind((host,port))

#listen
s.listen(5)

while True:
    # accept
    c, addr = s.accept()


    #read

    #write

    #close
