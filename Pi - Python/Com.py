import time, RPi.GPIO as GPIO
LEDon = False
# Python Codes
# The Innit() must be ran first to Allert Mindstorms
# Frequency = Change this to calabrate (in Seconds)
f = 1
#
"""
def decimal_to_binary(x):
    x = float(x)
    test_str = str(x)
    dec_at = test_str.find('.')
    p=0
    binary_equivalent = [0]
    c=0
    for m in range(0,100):
        if 2**m <= int(test_str[0:dec_at]):
            c += 1
        else:
            break

    for i in range(c, -1, -1):
        if 2**i + p <= (int(test_str[0:dec_at])):
            binary_equivalent.append(1)
            p = p + 2**i
        else:
            binary_equivalent.append(0)
    return binary_equivalent
"""
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
