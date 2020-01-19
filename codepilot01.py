#! /usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveSteering
from ev3dev2 .sound import Sound
from time import sleep

#using 'getpass' to prevent echoing the code... not really needed, 'input' is enough
from getpass import getpass

###

codedict = {
    1: {
        "barcode" : "5600000000014",
        "command" : "Forward",
        "value" : 1
    },

    2: {
        "barcode" : "5600000000021",
        "command" : "Backward",
        "value" : 2
    },

    3 : {
        "barcode" : "5600000000038",
        "command" : "Left",
        "value" : 3
    },

    4 : {
        "barcode" : "5600000000045",
        "command" : "Right",
        "value" : 4
    },

    5 : {
        "barcode" : "5600000000052",
        "command" : "Do it",
        "value" : 5
    }
}

drive = MoveSteering(OUTPUT_A, OUTPUT_B)

sound = Sound()
print("Running")
sound.beep()

while True:
    ucc = getpass('Scan a UCC: ')
    ucc = ucc.lower().strip().replace('\t','').replace('\n','')

    command=""
    for codeid, codedata in codedict.items():
        barcode = codedata["barcode"]
        if barcode == ucc:
            command=codedata["command"]

    if command == "":
        sound.speak("oopsy!")
    else:
#        print(command)
        sound.speak(command)

    if command == "Forward":
        drive.on_for_seconds(0, SpeedPercent(50), 1.5)
    elif command == "Backward":
        drive.on_for_seconds(0, SpeedPercent(-50), 1.5)
    elif command == "Left":
        drive.on_for_seconds(-100, SpeedPercent(50), 0.5)
    elif command == "Right":
        drive.on_for_seconds(100, SpeedPercent(50), 0.5)
    elif command == "Do it":
        sound.speak("Dude, do what?")
