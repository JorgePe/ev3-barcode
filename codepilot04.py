#! /usr/bin/env python3

# thanks to ROBOTMAK3RS Lee Magpili and Daniel Walton for inspiration

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveSteering
from ev3dev2.sound import Sound
from ev3dev2.button import Button

from time import sleep
from random import randint

#using getpass to prevent echoing the code... not really needed, 'input' works fine
from getpass import getpass

# sugestions:
# timing 1 | 2 | 3 | 4 | 5 | random
# speed 20 | 40 | 60
# sounds
# notes: C, C#, D, D#, E, F, F#, G, G#, A, A#, B

timing = 1.0
speedpct = 40

note_duration = 0.2
note_volume = 100
note_play_type = 0

DELAY = 1.0
LONGDELAY = 3.0
DEBOUNCE = 0.2

codedict = {
    1: {
        "barcode" : "5600000000014",
        "command" : "Forward",
        "function" : "drive.on_for_seconds(0, SpeedPercent(speedpct), timing)"
    },

    2: {
        "barcode" : "5600000000021",
        "command" : "Backward",
        "function" : "drive.on_for_seconds(0, SpeedPercent(-speedpct), timing)"
    },

    3 : {
        "barcode" : "5600000000038",
        "command" : "Left",
        "function" : "drive.on_for_seconds(-100, SpeedPercent(speedpct), timing)"
    },

    4 : {
        "barcode" : "5600000000045",
        "command" : "Right",
        "function" : "drive.on_for_seconds(100, SpeedPercent(speedpct), timing)"
    },

    5 : {
        "barcode" : "5600000000052",
        "command" : "Do it",
        "function" : "sound.speak('Dude, do what?')"
    },
    
    6 : {
        "barcode" : "5600000000069",
        "command" : "Timing 1 second",
        "function" : "timing = 1.0"
    },
    
    7 : {
        "barcode" : "5600000000076",
        "command" : "Timing 2 seconds",
        "function" : "timing = 2.0"
    },
    
    8 : {
        "barcode" : "5600000000083",
        "command" : "Timing 3 seconds",
        "function" : "timing = 3.0"
    },
    
    9 : {
        "barcode" : "5600000000090",
        "command" : "Timing 4 seconds",
        "function" : "timing = 4.0"
    },
    
    10 : {
        "barcode" : "5600000000106",
        "command" : "Timing 5 seconds",
        "function" : "timing = 5.0"
    },
    
    11 : {
        "barcode" : "5600000000113",
        "command" : "Timing Random",
        "function" : "timing = float(randint(1,5)); sound.speak('Timing is now ' + str(timing) + 'seconds')"
    },

    12 : {
        "barcode" : "5600000000120",
        "command" : "Speed 20 per cent",
        "function" : "speedpct = 20"
    },
    
    13 : {
        "barcode" : "5600000000137",
        "command" : "Speed 40 per cent",
        "function" : "speedpct = 40"
    },
    
    14 : {
        "barcode" : "5600000000144",
        "command" : "Speed 60 per cent",
        "function" : "speedpct = 60"
    },
    
    15 : {
        "barcode" : "5600000000151",
        "command" : "Speed 80 per cent",
        "function" : "speedpct = 80"
    },
    
    16 : {
        "barcode" : "5600000000168",
        "command" : "Speed 100 per cent",
        "function" : "speedpct = 100"
    },
    

    17 : {
        "barcode" : "5600000000175",
        "command" : "DO",
        "function" : "Sound.play_note("C4", note_duration, note_volume, note_play_type=0)"
    },
    

    18 : {
        "barcode" : "5600000000182",
        "command" : "RE",
        "function" : "Sound.play_note("D4", note_duration, note_volume, note_play_type=0)"
    },
    

    19 : {
        "barcode" : "5600000000199",
        "command" : "MI",
        "function" : "Sound.play_note("E4", note_duration, note_volume, note_play_type=0)"
    },
    

    20 : {
        "barcode" : "5600000000205",
        "command" : "FA",
        "function" : "Sound.play_note("F4", note_duration, note_volume, note_play_type=0)"
    },
    

    21 : {
        "barcode" : "5600000000212",
        "command" : "SOL",
        "function" : "Sound.play_note("G4", note_duration, note_volume, note_play_type=0)"
    },
    

    22 : {
        "barcode" : "5600000000229",
        "command" : "LA",
        "function" : "Sound.play_note("A4", note_duration, note_volume, note_play_type=0)"
    },
    

    23 : {
        "barcode" : "5600000000236",
        "command" : "SI",
        "function" : "Sound.play_note("B4", note_duration, note_volume, note_play_type=0)"
    },
    

    24 : {
        "barcode" : "5600000000243",
        "command" : "null",
        "function" : "pass"
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
    sleep(DEBOUNCE)  # debouncing delay, not sure if needed but doesn't hurt

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
    sleep(DELAY)

    for step in sequence:
        exec(step)
        sleep(DELAY)

    print("Done!")
    sound.speak("Done!")
    sleep(LONGDELAY)

    # clear the sequence before starting again
    sequence.clear()
