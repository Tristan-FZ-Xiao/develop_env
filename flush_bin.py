import socket

def ReadFile(fileName):
    dest = ('<broadcast>', 20000)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    rf = open(fileName, 'rb')
    while True:
        rBuf = rf.read(1024)
        if rBuf != "":
            #print rBuf
            s.sendto(rBuf, dest)
        else:
            break
    print "finish ReadFile"
    rf.close()

ReadFile("a.bin")
