﻿# MindPi - You Raspberry Pi to Mindstorm Connection

Hello, I'm Boston the Creator Of MindPi

Basic Explanation:
With this you can communicate between a Mindstorms Brick and a Raspberry Pi Easly.

How it works:

You have some information you want to transmit, but in this current version it will only accept binary inputs, so unfortunately you will need to convert your info to binary. So then you input the series of ones and zeros you want to transfer to the “Com.Binary()” python function on your Raspberry Pi the Led will flash in this pattern. I chose to use python because it is preinstalled on the Raspberry Pi and I already have a basic knowledge of how it works!. This flashing can be read by a Ev3 Color Sensor controlled by a  “My Block” called BinaryTransfer (what Ev3-G, the Lego Mindstorms Programing language, calls a function) waiting for these flashes on the Mindstorms Brick. When the message has reached the length specified by the numerical input to the My Block it stops recording and returns the binary that it recorded. This would conclude the transfer of data from one system to another.

How To Guide: {{{THIS IS NOT DONE YET}}}

  Step 1:
  Download the Zip File with the latest version on your pc/mac (not your pi yet)

  Currently "Version .02 ZIPPED!.zip"

  Step 2:

  Do nothing

  Step 3:

  Use the PDF instructions to build the LED holder.

  Step 4:

  Connect the color sensor to the #3 port on the Mindstorms Brick.

  Step 5:
  Attach the LED as to the middle hole on the 5 long liftarm/

  Step 6:
  Follow the circuit diagram to attach the LED to the Raspberry Pi.

  Step 7:
  Plug in the power supply, keyboard and mouse to the Pi/

  Step 8:

  Boot up the pi.

  Step 9:

  Get the Python archive onto the pi, there are many ways to do this, you could use the git pull command or a USB.

  Step 10:
  Open Mindpi/Pi - Python/Com.py

  Step 11: {IN PROGRESS}

  Open the Command Line

    cd ... {Location of Com.py}
    sudo mv

  Step 12:

  Open Mindpi/Examples/SimpleCommand/CommandLine.py in python 2

  Run > Run Module

  Type in 1's and 0's and watch the LED flash if it does not work Check Troubleshooting

  Step 7:
  Open the Mindstorms EV3 program file located in the "Mindstorms" folder.

  Step 6:

Troubleshooting:
