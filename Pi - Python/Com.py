import time, RPi.GPIO as GPIO
def toBinary(n):
    return ''.join(str(1 & int(n) >> i) for i in range(64)[::-1])
LEDon = False
# Python Codes
# The Innit() must be ran first to Allert Mindstorms
# Frequency = Change this to calabrate (in Seconds)
f = 1
#
def On():
    print "LED on"
    GPIO.output(4, GPIO.HIGH)
def Off():
    print "LED off"
    GPIO.output(4, GPIO.LOW)
def Init():
    On()
    time.sleep(f)
    Off()
    time.sleep(f)
def Binary(Data):
    Off()
    print "IN BIN"
    LEDon = False
    for Digit in Data:
        if Digit == "1":
            print " Dig 1"
            if not LEDon:
                LEDon = True
                print "ON"
                On()
        if Digit == "0":
            print " Dig 0"
            if LEDon:
                print "OFF"
                LEDon = False
                Off()
        print " -- "
        time.sleep(f)
    Off()
def Numeral(Data):
    zeros = True
    binary = []
    num = 0
    b = toBinary(Data)
    for char in b:
        num = num+1
        if char != "0":
            zeros = False
        if zeros == False:
            binary.append(char)
    Binary(binary)

"""
def Hexadecimal(Data):
    print "Hex"
def ASCII(Data):
    print "ASCII"
"""
Numeral("12")
