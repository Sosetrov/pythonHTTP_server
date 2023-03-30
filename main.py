import socket
import os

WORKING_DIR = os.getcwd()

server = socket.socket()
server.bind(('', 80))

server.listen(1)

while True:
    conn, addr = server.accept()
    print(addr)
    request = conn.recv(10240).decode().split('\n')
    #print(request)

    method,url, protocol = request[0].split(' ')
    url = os.path.join(WORKING_DIR,url[1:])
    print(url)

    response = 'test'
    conn.send(response.encode())
    conn.close()
    print('Connection closed\n')

