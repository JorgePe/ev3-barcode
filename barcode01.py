#! /usr/bin/env python3

# if you are running from ssh session invoke this script with 'brickrun'
from ev3dev2 .sound import Sound

sound = Sound()

while True:
    ucc = input('Scan a UCC: ')
    ucc = ucc.lower().strip().replace('\t','').replace('\n','')
    sound.speak(ucc)
