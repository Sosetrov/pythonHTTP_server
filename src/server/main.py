import socket
from load_page import load_page_from_get_request

def start_my_server():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('', 8000))
        server.listen(1)
        while True:
            print('Working...')
            client_socket, address = server.accept()
            data = client_socket.recv(1024).decode('utf-8')
            content = load_page_from_get_request(data)
            client_socket.send(content)
            client_socket.shutdown(socket.SHUT_WR)

    except KeyboardInterrupt:
        server.close()
        print('shutdown this shift...')



if __name__ == '__main__':
    start_my_server()

