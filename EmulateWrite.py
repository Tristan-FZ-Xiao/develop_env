import socket

def emulateWriteFile(fileName):
    dest = ('', 20000)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('', 20000))
    wf = open(fileName, 'wb')
    flag = 0 
    while True:
        rBuf = s.recv(1024)
        if rBuf != "":
            wf.write(rBuf) 
            flag = 1
        elif flag == 1:
            break
    print "finish writeFile"
    s.close()
    wf.close()

emulateWriteFile("b.bin")
