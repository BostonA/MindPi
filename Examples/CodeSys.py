import RPi.GPIO as GPIO
import time, Com
restTime = .5
flashPattern = [12, 3, 8, 3]
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
def flashLEDon ():
    print "LED on"
    GPIO.output(4, GPIO.HIGH)
def flashLEDoff ():
    print "LED off"
    GPIO.output(4, GPIO.LOW)
flashLEDoff()
while True:
    Code = []
    Expanded_Line =[]
    reading_file=open('newfile.txt', 'r')

    lines=reading_file.readlines()
    GoodLine = lines[len(lines) - 1]
    OldGood = GoodLine
    oldLinesGood = lines
    while True:
        time.sleep(1)
        # Change the location Not sure where
        reading_file=open('newfile.txt', 'r')
        lines=reading_file.readlines()
        print lines
        GoodLine = lines[len(lines) - 1]
        if len(GoodLine)==4 and len(lines) > len(oldLinesGood):
            break
        OldGood = GoodLine
        oldLinesGood = lines
    for x in GoodLine:
        Expanded_Line.append(x)
        #print Expanded_Line
    Com.Init()
    if Expanded_Line[0] + Expanded_Line[1] == "00":
        DegB = "00"
        print "90 Degrees"
    elif Expanded_Line[0] + Expanded_Line[1] == "01":
        DegB = "01"
        print "180 Degrees"
    elif Expanded_Line[0] + Expanded_Line[1] == "10":
        DegB = "10"
        print "270 Degrees"
    elif Expanded_Line[0] + Expanded_Line[1]  == "11":
        DegB = "11"
        print "360 Degrees"
    else:
        Code.append(0)
        print "Empty"
        
    if Expanded_Line[3] == "L":
        L = True
        print "Rotate: Left"
    elif Expanded_Line[3] == "R":
        L = False
        print "Rotate: Right"
    else:
        print "Error: php formating incorrect"
    
    print Code
    if DegB == "00" and L == True:
        Info = "001"
    elif DegB == "00" and L == False:
        Info = "000"
    elif DegB == "01" and L == True:
        Info = "011"
    elif DegB == "01" and L == False:
        Info = "010"
    elif DegB == "10" and L == True:
        Info = "101"
    elif DegB == "10" and L == False:
        Info = "100"
    elif DegB == "11" and L == True:
        Info = "111"
    elif DegB == "11" and L == False:
        Info = "110"
        
    Com.Binary(Info)
    flashLEDoff()
    time.sleep(4)
    flashLEDon()
    time.sleep(4)
    flashLEDoff()
    
"""
    for x in Code:
        print x
        flashLEDon ()
        if x == 3:
            time.sleep(1)
            print "on for 1 sec"
        elif x == 8:
            time.sleep(2)
            print "on for 2 sec"
        elif x == 12:
            time.sleep(3)
            print "on for 3 sec"
        elif x == 24:
            time.sleep(4)
            print "on for 4 sec"
        elif x == 0:
            time.sleep(5)
            print "on for 5 sec"
        else:
            print "error"
        flashLEDoff()
        time.sleep(1)
    flashLEDon()
    if Free:
        time.sleep(2)
        print "on for 2 sec"
    else:
        time.sleep(1)
        print "on for 1 sec"
    flashLEDoff()
"""
