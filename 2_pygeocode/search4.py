#!/usr/bin/env python3
import socket
import ssl
from urllib.parse import quote_plus

request_text = """\
GET /search?q={}&format=json HTTP/1.1\r\n\
Host: nominatim.openstreetmap.org\r\n\
User-Agent: Search4.py\r\n\
Connection: close\r\n\
\r\n\
"""


def geocode(address):
    unencrypted_sock = socket.socket()
    unencrypted_sock.connect(('nominatim.openstreetmap.org', 443))
    sock = ssl.wrap_socket(unencrypted_sock)
    request = request_text.format(quote_plus(address))
    sock.sendall(request.encode('ascii'))
    raw_reply = b''
    while True:
        more = sock.recv(4096)
        if not more:
            break
        raw_reply += more
    print(raw_reply.decode('utf-8'))
    print("Endereço buscado: ", address)
    print("Resultado 1:")
    print("CEP: ",raw_reply.decode('utf-8').split(", ")[-2])
    print(raw_reply.decode('utf-8').split(",")[-14])
    print("Resultado 2:")
    print("CEP: ",raw_reply.decode('utf-8').split(", ")[-2])
    print(raw_reply.decode('utf-8').split(",")[-13])


if __name__ == '__main__':
    geocode('Belarmino Vilela Junqueira, Ituiutaba, MG')