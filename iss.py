#!/usr/bin/env python

__author__ = 'Meagan Ramey'

import requests
import turtle
import time


def astronauts():
    '''Obtains and returns a list of astronauts, the spacecraft they are
        aboard, and the total number of astronausts in space using
        NASA's API.'''
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
    '''Obtains the current timestamp and coordinates of the ISS.'''
    r = requests.get('http://api.open-notify.org/iss-now.json')
    r = r.json()
    coords = r['iss_position']
    time = r['timestamp']
    return time, coords


def over_indy():
    '''Obtains and returns the next date, to the seconds, the ISS will be over
        Indianapolis, IN'''
    r = requests.get(
        """
        http://api.open-notify.org/iss/v1/?lat=40.027435&lon=-86.158068&alt=1650&n=1
        """
        )
    r = r.json()
    date = r['response'][0]['risetime']
    seconds = r['response'][0]['duration']
    overhead_date = time.ctime(date)
    indy_date = [overhead_date, seconds]
    return indy_date


def iss_display(time, coords, indy):
    '''Using turtle, displays the world map with an ISS icon. Moves the ISS
        icon to the current ISS coordinates, and adds a yellow dot and next
        passover time to Indianapolis, IN.'''
    disp = turtle.Screen()
    disp.setup(width=720, height=360)
    disp.bgpic('map.gif')
    disp.setworldcoordinates(-180, -90, 180, 90)
    disp.register_shape('iss.gif')
    iss = turtle.Turtle()
    iss.penup()
    iss.goto(float(coords['longitude']), float(coords['latitude']))
    iss.shape('iss.gif')
    indianapolis = turtle.Turtle()
    indianapolis.penup()
    indianapolis.goto(-88.158068, 39.768403)
    indianapolis.shape('circle')
    indianapolis.color('yellow')
    indianapolis.turtlesize(0.2)
    overhead = turtle.Turtle()
    overhead.penup()
    overhead.color('white')
    overhead.goto(-80.158068, 39.768403)
    overhead.write(f"""
    ISS will pass over Indianapolis on: {indy[0]} for a duration of
    {indy[1]} seconds""")
    turtle.done()


def main():
    astronauts()
    time, coords = iss_location()
    indy = over_indy()
    iss_display(time, coords, indy)


if __name__ == '__main__':
    main()
