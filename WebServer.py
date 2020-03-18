import socket
import sys
import base64

bind_ip = "127.0.0.1"
bind_port = int(sys.argv[1])

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.settimeout(None)
server.listen(5)

print("[*] Listening on %s:%d" %(bind_ip, bind_port))

def to_bytes(_string):
    return _string.encode(encoding='UTF-8')


def ico():
    return base64.decodestring(b"iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAIAAAD8GO2jAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAABmJLR0QA/wD/AP+gvaeTAAAAB3RJTUUH5AMSBSEMf1ON0wAABH9JREFUSMe1lk2IlVUYx//Pc97zvvfOjON8KmqDieWiQkg0a6ELTY2kD8OvaqDaRCiEFLhrE1QUCRWC0K6FYRIYRVIJRikkGCoZRjqLDD9GR50Z79y5977ve55/i5ttnHv1Gp7t4ZzfOc///3wISdzNpf/nMM1odhcAJEKgUVQhYtYsBi0CSIQMIJyDonz0+MnX3xofOg2ADTDR7V5tBhJO4XyeViYOHrr0+Z5Lv/xUS9N5W5+vwwG5I4AZAKoC4LWrY/u/v7Z3d3by9xAQdxZdwUvTMDQFkCAhApHs779qX3ybfrWvcv5c5FW6elNYe5aVM1MCUz7+lgCSolo5dWzis91y4DCvXGb7tKS7Q8GMlguNuevqi2f2A4BIywARGf945/VPd7E2ESe92ttHCwy5CJw6IHGXRmYODrqePgSD01YAZlA98v6OgZ07p83oC74tNwsWBBCnIsJqGWOVnvWbet7cFoBIpeErb85kkiIyNnz+k+WrFkr6WKHHiwYEQx5o0cQkCPfgfHn5penPbHKRkiYijVSY6gdmcG74j1McHz2f+B/zy/Ojjp4kLipcoc0/ujxZ/0Rh2QotFM1yEiItuqju53Riwlut4Kdp4LBNljTvUPbMvWfmxo2FZYs1LrKuEgzQBjnQVGQfFVUdVCMw8S5W9eKzM2fHtrxa7Z/hH34kXrU4XrVai92gNakIU2lgJqojZ4b2rF4z3ck0p53OdUK74GIfJwrLa34yr1mmixf1f7QjmjMg9XSZak1BFlUa+++/b9GLg9WRUcfUq8aqCZhYgJFxbN3tvq/bHTlafve9HAhsxUU3hLAsq53cuWt477724dHutNKbeF8ohkihUBogACMfdXyzz88a0AafkMYNx0iKuOr4lYlfT1QO/lz87US4eFFSC04k5BQo4YDpX+71CxbUU+e2QvTflkCZ54XO3r4Vj89+521ufe184q5UK5MENErgTVQp2rAONXURAJASRXm1XP1u/8ier68dO16x/AKyaqkce5kRd9wbFUO7sLsbuINaZAbVyqHD5Q8/sFNDkUpbDASpma+ZjmbZkJTGR64ufXaN6++DEdoSwAyqkwd+KG3Zpg5xZ5dDhlABmEIzFxt85dLo5TlzCm9sFzTJsylFJiESSlcurFvnz13zxQ6xAGWqLJHjk+nYRHW8zXetXLlk+/bOeXONJqKt9AMSIvnJ03p2RNqLyFNEjpFjNhmXyr6nZ+C5pxdt3ty9cKEQbHp7YwAQxq77mmlHJC5jpczMZMHA9Fee6t+woW32LEBoNABa9yZbqab/7jioVcoV0Wr80AMd6zYla9e6ri4StByAaHTjymZjS0OAVKuS1wpPLiu+MNi2ZJkmMWkMmaiD3vYs0kTk9NSfLJWSpYsBwIhgUELdTX6vH2+5Ft0wdn2w0DufMBvXIrLePAkQFIiAJhSKUih1VUXkFoCpOhpJ0oIZLZjlFjILIc0YskxyR+fFR7FEUeI0ETEVcVGkettThYjQ6u8nyLoAwcxyozCICVLkTiVyShKUZj76B0yYXzjR8R3xAAAAJXRFWHRkYXRlOmNyZWF0ZQAyMDIwLTAzLTE4VDA1OjMzOjEyLTA3OjAwJD4QVQAAACV0RVh0ZGF0ZTptb2RpZnkAMjAyMC0wMy0xOFQwNTozMzoxMi0wNzowMFVjqOkAAAAASUVORK5CYII=")

def open_file(filename):
    if filename == '/favicon.ico':
        return ico()
    try:
        fileData = open(filename[1:], "rb").read()

    except FileNotFoundError:
        print("[*] File '%s' not found." % filename)
        return False

    return fileData

def header(filename = None):

    success_string = "HTTP/1.1 200 OK\r\nConnection: Keep-Alive\r\n"
    notfound_string = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n<html><head></head><body><h1>404 Not Found</h1></body></html>"

    if not filename:
        return to_bytes(notfound_string)

    splitted = filename.split(".")

    if splitted[-1] == 'html':
        success_string += "Content-Type: text/html\r\n\r\n"
    elif splitted[-1] == 'png' or splitted[-1] == 'PNG':
        success_string += "Content-Type: image/png\r\n\r\n"
    elif splitted[-1] == "ico":
        success_string += "Content-Type: image/x-icon\r\n\r\n"
    elif splitted[-1] == 'jpg' or splitted[-1] == 'jpeg' or splitted[-1] == 'JPG':
        success_string += "Content-Type: image/jpeg\r\n\r\n"
    elif splitted[-1] == "pdf":
        success_string += 'Content-Type: application/pdf\r\n\r\n'

    return to_bytes(success_string)


def handle_client(client_socket):
    
    # print out what the client sends
    request = client_socket.recv(1024)
    request = request.decode("utf-8")
    splitted = request.split('\r\n')

    print("[*] Received:")
    for i in splitted:
        print("|   ", i)
    print("[*] == End ==\n")

    if splitted[0]:
        details = splitted[0].split()
        if details[0] == 'GET':
            fname = details[1]

            #default path
            if fname == '/':
                fname = '/index.html'

            data = open_file(fname)

            if data:
                HTTPString =  header(fname) + data
                client_socket.send(HTTPString)
            else:
                HTTPString = header()
                client_socket.send(HTTPString)

    
    client_socket.close()
    
while True:
    try:
        conn, addr = server.accept()
        print("[*] Accepted connection from: %s:%d" % (addr[0], addr[1]))

        handle_client(conn)

    except KeyboardInterrupt:
        try:
            if conn:
                conn.close()
        except:
            pass
            
        break

