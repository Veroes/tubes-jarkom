# Import socket yang dibutuhkan
from socket import *
import sys # Untuk terminasi program

# Membuat socket TCP
serverSocket = socket(AF_INET, SOCK_STREAM)

# Setting Socket TCP localhost(127.0.0.1)
serverPort = 8001
serverSocket.bind(('', serverPort)) 
serverSocket.listen(1)

while True:
    # Mendirikan Koneksi TCP
    print('Web Server ready to serve clients...')
    connectionSocket, addr = serverSocket.accept()
    print(addr)

    # Mencoba apakah request dari client valid atau tidak
    try:
        # Menerima request file dari client 
        message = connectionSocket.recv(1024).decode()
        fileName = message.split('/')[1].split()[0]
        f = open('./html/{}'.format(fileName))
        outputFile = f.read()

        # Mengirim HTTP Header 
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())

        # Mengirim konten dari yang diminta oleh client
        connectionSocket.sendall(outputFile.encode())
        connectionSocket.send('\r\n'.encode())
        
        # Close client socket
        connectionSocket.close()
        
    except IOError:
        # Mengirim respons apabila file yang diminta tidak ada
        connectionSocket.send('HTTP/1.1 404 Not Found\r\n\r\n'.encode())
        connectionSocket.sendall('./html/nonexist.html\r\n'.encode())

        # Close client socket
        connectionSocket.close()

serverSocket.close()
sys.exit()