# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 11:21:51 2020

@author: frank
"""
t = float(input('How long would you like the object to fall? '))
h = float(input('Enter Height of Tower in meters: '))
g = 9.81 #m/s^2
d = .5*g*t*2 #distance ball has fallen
if h - d < 0:
    print('The ball has already hit the ground')
else:
    print("The height of the ball is ", h-d, "meters above the ground.")
    