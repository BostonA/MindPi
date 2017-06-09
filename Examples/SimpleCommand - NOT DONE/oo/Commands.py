import Com
print "Write the bianry you want to send!"
while True:
    propperCommand = True
    binary = raw_input(">>> ")
    for x in binary:
        if x == "1" or x == "0":
            pass
        
        else:
            print "Please Only Type Bianary!"
            propperCommand = False
            break
    if propperCommand and binary != "":
        Com.Init()
        Com.Binary(binary)
        print "Sent Data"
