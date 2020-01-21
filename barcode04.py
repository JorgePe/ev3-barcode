#! /usr/bin/env python3

# thanks to ROBOTMAK3RS Lee Magpili and Daniel Walton for inspiration

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveSteering
from ev3dev2.sound import Sound
from ev3dev2.button import Button

from time import sleep

#using getpass to prevent echoing the code... not really needed, 'input' works fine
from getpass import getpass

# sugestions:
# timing 1 | 2 | 3 | 4 | 5 | random
# speed 20 | 40 | 60
# sounds
# notes: C, C#, D, D#, E, F, F#, G, G#, A, A#, B

codedict = {
    1: {
        "barcode" : "5600000000014",
        "command" : "Forward",
        "function" : "drive.on_for_seconds(0, SpeedPercent(50), 1.5)"
    },

    2: {
        "barcode" : "5600000000021",
        "command" : "Backward",
        "function" : "drive.on_for_seconds(0, SpeedPercent(-50), 1.5)"
    },

    3 : {
        "barcode" : "5600000000038",
        "command" : "Left",
        "function" : "drive.on_for_seconds(-100, SpeedPercent(50), 0.5)"
    },

    4 : {
        "barcode" : "5600000000045",
        "command" : "Right",
        "function" : "drive.on_for_seconds(100, SpeedPercent(50), 0.5)"
    },

    5 : {
        "barcode" : "5600000000052",
        "command" : "Do it",
        "function" : "sound.speak('Dude, do what?')"
    }
}

drive = MoveSteering(OUTPUT_A, OUTPUT_B)

sound = Sound()
print("Running")
sound.speak("Running")

btn=Button()

# initialize the sequence as an empty list
sequence = []

while True:
    # wait for [Enter] button to start recording a new sequence
    sound.speak("Please insert the scanner and press ENTER to create a program")
    while not btn.enter:
        pass    
    sleep(0.2)  # debounce, not sure if needed but doesn't hurt

    # keep adding steps to the sequence until [Enter] is pressed again    
    while True:
        ucc = getpass('Scan a UCC: ')
        ucc = ucc.lower().strip().replace('\t','').replace('\n','')

        command=""
        function=""
        for codeid, codedata in codedict.items():
            barcode = codedata["barcode"]
            if barcode == ucc:
                command=codedata["command"]
                function=codedata["function"]

        # when using sound.speak sometimes pressing [ENTER] got a "oopsy!"
        # a worakround was using long presses but its better to prevent it
        # perhaps using other key than would be better

        if btn.enter:
            break

        if command == "":
            print("oopsy!")
            sound.speak("oopsy!")
        else:
            print(command)
            sound.speak(command)
            sequence.append(function)

    # stats
    size = len(sequence)
    print(size)
    sound.speak("Your program has " + str(size) + " steps" )
    sound.speak("Please remove the scanner and press ENTER to execute it")

    while not btn.enter:
        pass
    sleep(0.5)

    for step in sequence:
        exec(step)
        sleep(1.0)

    print("Done!")
    sound.speak("Done!")
    sleep(2)

    # clear the sequence before starting again
    sequence.clear()
