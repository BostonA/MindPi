import time, RPi.GPIO as GPIO
LEDon = False
# Python Codes
# The Innit() must be ran first to Alert Mindstorms
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
    binary = []
    print "Numeral"
    for Digit in Data:
        if Digit == "0":
            binary.append("0")
            binary.append("0")
            binary.append("0")
            binary.append("0")
        elif Digit == "1":
            binary.append("0")
            binary.append("0")
            binary.append("0")
            binary.append("1")
        elif Digit == "2":
            binary.append("0")
            binary.append("0")
            binary.append("1")
            binary.append("0")
        elif Digit == "3":
            binary.append("0")
            binary.append("0")
            binary.append("1")
            binary.append("1")
        elif Digit == "4":
            binary.append("0")
            binary.append("1")
            binary.append("0")
            binary.append("0")
        elif Digit == "5":
            binary.append("0")
            binary.append("1")
            binary.append("0")
            binary.append("1")
        elif Digit == "6":
            binary.append("0")
            binary.append("1")
            binary.append("1")
            binary.append("0")
        elif Digit == "7":
            binary.append("0")
            binary.append("1")
            binary.append("1")
            binary.append("1")
        elif Digit == "8":
            binary.append("1")
            binary.append("0")
            binary.append("0")
            binary.append("0")
        elif Digit == "9":
            binary.append("1")
            binary.append("0")
            binary.append("0")
            binary.append("1")
    Binary(binary)
"""
def Hexadecimal(Data):
    print "Hex"
def ASCII(Data):
    print "ASCII"
"""
#Numeral("123456789")
