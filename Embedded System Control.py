import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

def DMD_Start():
    print("Starting DMD")


def DMD_Update(mode_number):
    modes = ['mode1','mode2','mode3','mode4','mode5','mode6','mode7','mode8']

    print(modes[mode_number])

def Calculate_Mode(pin1,pin2,pin3):
    mode_number = 1*pin1 + 2*pin2 + 4*pin3

    return mode_number

DMD_Start()

GPIO.setup("P9_11", GPIO.IN)
GPIO.setup("P9_13", GPIO.IN)
GPIO.setup("P9_15", GPIO.IN)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

Default_mode = 0
Last_mode = 0

while True:
    if Default_mode == 0:
        DMD_Update(Default_mode)
        Default_mode = 1
    else:
        GPIO.wait_for_edge(23, GPIO.RISING)
        mode_number = Calculate_Mode(GPIO.input("P9_11"),
                                    GPIO.input("P9_13"),
                                    GPIO.input("P9_15"))
        if mode_number != Last_mode:
            DMD_Update(mode_number)
            Last_mode = mode_number


