import socket, time

def ReadFile(fileName):
    dest = ('<broadcast>', 20000)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    rf = open(fileName, 'rb')
    while True:
        time.sleep(0.0001)
        rBuf = rf.read(1024)
        if rBuf != "":
            s.sendto(rBuf, dest)
        else:
            rBuf = "qltxcxbb"
            s.sendto(rBuf, dest)
            break
    print "finish ReadFile"
    rf.close()
    s.close()

os.system("tar -czvf aaa.tar.gz aaa")
os.system("mv aaa.tar.gz a.bin")
ReadFile("a.bin")
