#!/usr/bin/env python3
import requests


def geocode(address):
    base = 'https://nominatim.openstreetmap.org/search'
    parameters = {'q': address, 'format': 'json'}
    user_agent = 'Search2.py'
    headers = {'User-Agent': user_agent}
    response = requests.get(base, params=parameters, headers=headers)
    reply = response.json()
    print("Endereço buscado: ", address)
    print("Resultado 1:")
    print("CEP: ",reply[0]['display_name'].split(", ")[-2])
    print(reply[0]['lat'], reply[0]['lon'])
    print("Resultado 2:")
    print("CEP: ",reply[1]['display_name'].split(", ")[-2])
    print(reply[1]['lat'], reply[1]['lon'])


if __name__ == '__main__':
    geocode('Belarmino Vilela Junqueira, Ituiutaba, MG')