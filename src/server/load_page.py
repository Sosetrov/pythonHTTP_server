def load_page_from_get_request(request_data):
    HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
    HDRS_404 = 'HTTP/1.1 404 OK\r\nContent-Type: text/html; charset = utf-8\r\n\r\n'

    try:
        if request_data == '':
            print('Oh, no. Request_data is empty')
            return (HDRS_404 + 'Sorry, bro! No PAge...').encode('utf-8')

        path = request_data.split(' ')[1]
        if path == '/':
            with open('views/index.html', 'rb') as file:
                response = file.read()
        else:
            with open('views' + path, 'rb') as file:
                response = file.read()

        return HDRS.encode('utf-8') + response
    except FileNotFoundError:
        print('Not found: ' + path)
        return (HDRS_404 + 'Sorry, bro! No PAge...').encode('utf-8')