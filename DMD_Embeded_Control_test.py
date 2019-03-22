import RPi.GPIO as GPIO
import Faster_pycrafter6500
import numpy as np
import time
GPIO.setmode(GPIO.BCM)

mode1=np.load('mode1.npy')
mode2=np.load('mode2.npy')
mode3=np.load('mode3.npy')
mode4=np.load('mode4.npy')
mode5=np.load('mode5.npy')
mode6=np.load('mode6.npy')
modes = [mode1,mode2,mode3,mode4,mode5,mode6, mode1,mode1]

def DMD_Update(mode_number,dlp):
    t = time.clock()
    mode = modes[mode_number]
    dlp.stopsequence()
    dlp.defsequence(mode.tolist(), exposure, trigger_in, dark_time, trigger_out, 0)
    dlp.startsequence()
    t2 = time.clock()
    print('mode',mode_number,'Need',t2-t,'s')

def Calculate_Mode(pin1,pin2,pin3):
    mode_number = 1*pin1 + 2*pin2 + 4*pin3

    return mode_number

dlp = Faster_pycrafter6500.dmd()
dlp.stopsequence()
dlp.changemode(3)
exposure = [1000000] * 30
dark_time = [0] * 30
trigger_in = [False] * 30
trigger_out = [1] * 30
print("Starting DMD")

GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

Default_mode = 0
Last_mode = 0

while True:
    if Default_mode == 0:
        DMD_Update(Default_mode, dlp)
        Default_mode = 1
    else:
        GPIO.wait_for_edge(23, GPIO.RISING)
        mode_number = Calculate_Mode(GPIO.input(22),
                                    GPIO.input(24),
                                    GPIO.input(25))
        if mode_number != Last_mode:
            DMD_Update(mode_number, dlp)
            Last_mode = mode_number