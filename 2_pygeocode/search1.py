#!/usr/bin/env python3

from geopy.geocoders import Nominatim


if __name__ == '__main__':
    address = 'Belarmino Vilela Junqueira, Ituiutaba, MG'
    user_agent = 'Search1'
    location = Nominatim(user_agent=user_agent).geocode(address,exactly_one=False)
    print("Endereço buscado: ", address)
    print("Resultado 1:")
    print(location[0].address.split(", ")[-2])
    print(location[0][1])
    print("Resultado 2:")
    print(location[1].address.split(", ")[-2])
    print(location[1][1])