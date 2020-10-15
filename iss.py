#!/usr/bin/env python

__author__ = 'Meagan Ramey'

import requests


def astronauts():
    r = requests.get('http://api.open-notify.org/astros.json')
    r = r.json()
    astronaut_list = r['people']
    for astronaut in astronaut_list:
        for k, v in astronaut.items():
            if k == 'name':
                print(f'{v} is on the ', end='')
            else:
                print(f'{v}')
    print(f'There are a total of {len(astronaut_list)} in space.')


def iss_location():
    r = requests.get('http://api.open-notify.org/iss-now.json')
    r = r.json()
    coords = r['iss_position']
    time = r['timestamp']
    return time, coords


def main():
    astronauts_on_ISS = astronauts()
    time, coords = iss_location()
    print(time)
    print(coords)


if __name__ == '__main__':
    main()
