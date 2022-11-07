#!/usr/bin/env python3
import http.client
import json
from urllib.parse import quote_plus

base = '/search'


def geocode(address):
    path = '{}?q={}&format=json'.format(base, quote_plus(address))
    user_agent = b'Search3.py'
    headers = {b'User-Agent': user_agent}
    connection = http.client.HTTPSConnection('nominatim.openstreetmap.org')
    connection.request('GET', path, None, headers)
    rawreply = connection.getresponse().read()
    reply = json.loads(rawreply.decode('utf-8'))
    print("Endereço buscado: ", address)
    print("Resultado 1:")
    print("CEP: ", reply[0]['display_name'].split(", ")[-2])
    print(reply[0]['lat'], reply[0]['lon'])
    print("Resultado 2:")
    print("CEP: ", reply[1]['display_name'].split(", ")[-2])
    print(reply[1]['lat'], reply[1]['lon'])


if __name__ == '__main__':
    geocode('Belarmino Vilela Junqueira, Ituiutaba, MG')