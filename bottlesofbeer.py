#!/usr/bin/env python3

#code to display a given number of bottles of beer on the wall

#Prompt the user for input

import time

import crayons 
 
number=99



for i in range(number):
    print(f"{number} bottles of beer on the wall! {number} bottles of beer! You take one down, pass it around\n) {number-1} bottles of beer on the wall!")
    number= number-1
    time.sleep(2)
#time.sleep(2)