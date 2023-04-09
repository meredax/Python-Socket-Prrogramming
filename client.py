from socket import *
import sys
serverName = sys.argv[1]
serverPort = int(sys.argv[2])
fileName = sys.argv[3]
request = "GET "+str(fileName)+" HTTP/1.1"

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
clientSocket.send(request.encode())
returnFromServer = clientSocket.recv(1024)

while(len(returnFromServer)>0):
    print(returnFromServer.decode())
    returnFromServer = clientSocket.recv(1024)
clientSocket.close()