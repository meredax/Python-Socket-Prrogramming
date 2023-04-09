#import socket module 
from socket import *
import sys # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start
server_port = 41159
serverSocket.bind(("10.0.2.15",server_port))
print('listening on port:', serverSocket.getsockname()[1])

#Listen to at most one connection at a time
serverSocket.listen(1)

#Fill in end
while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()   #Fill in start #Fill in end
    try:
        #receive message from the client
        message = connectionSocket.recv(1024)#Fill in start #Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read() #get the entire data
        #Fill in start #Fill in end
        #Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
        #Fill in start
        #Fill in end
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())    
        
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        #Fill in start
        #Fill in end
        #Close client socket
        #Fill in start
        #Fill in end
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())

        connectionSocket.close()
  
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data

