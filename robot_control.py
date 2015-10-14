#Import Python USB`
import usb.core
import usb.util
import time
from Tkinter import *

#######################################################################
# Arm Control Codes
#######################################################################
STOP = [0,0]

GRIP_CLOSE   = [1,0]
GRIP_OPEN    = [2,0]
WRIST_UP     = [4,0]
WRIST_DOWN   = [8,0]
ELBOW_UP     = [16,0]
ELBOW_DOWN   = [32,0]
SHOULDER_UP  = [64,0]
SHOULDER_DOWN= [128,0]

BASE_COUNTERCLOCKWISE = [0,1]
BASE_CLOCKWISE = [0,2]

duration = 1



#######################################################################
# Find The Robot Arm
#######################################################################
def find_arm():
	dev = usb.core.find(idVendor=0x1267, idProduct=0);

	if dev is None:
	    raise ValueError('Device not found')


#######################################################################
# Send Command
#######################################################################
def command2(cmd, light):
    c = list(cmd)
    c.append(light)
    dev.ctrl_transfer(0x40,6,0x100,0,c,1000)

#######################################################################
# Send Command
#######################################################################
def command(cmd, light, duration):
    c = list(cmd)
    c.append(light)
    dev.ctrl_transfer(0x40,6,0x100,0,c,1000)
    time.sleep(duration)
    c = list(STOP)
    c.append(light)
    dev.ctrl_transfer(0x40,6,0x100,0,c,1000)

class Window:
    def __init__(self):
        self.lightVar = IntVar()

    def grip_close(self):
        command(GRIP_CLOSE,self.lightVar.get(),duration)

    def grip_open(self):
        command(GRIP_OPEN,self.lightVar.get(),duration)

    def light(self):
        command2(STOP,self.lightVar.get())

    def wrist(self, value):
        self.elbowScale.set(0)
        self.shoulderScale.set(0)
        self.baseScale.set(0)
        if int(value)<0:
            command2(WRIST_DOWN,self.lightVar.get())
        elif int(value)>0:
            command2(WRIST_UP, self.lightVar.get())
        else:
            command2(STOP, self.lightVar.get())

    def elbow(self, value):
        self.wristScale.set(0)
        self.shoulderScale.set(0)
        self.baseScale.set(0)
        if int(value)<0:
            command2(ELBOW_DOWN,self.lightVar.get())
        elif int(value)>0:
            command2(ELBOW_UP, self.lightVar.get())
        else:
            command2(STOP, self.lightVar.get())       

    def shoulder(self, value):
        self.wristScale.set(0)
        self.elbowScale.set(0)
        self.baseScale.set(0)
        if int(value)<0:
            command2(SHOULDER_DOWN,self.lightVar.get())
        elif int(value)>0:
            command2(SHOULDER_UP, self.lightVar.get())
        else:
            command2(STOP, self.lightVar.get())

    def base(self, value):
        self.wristScale.set(0)
        self.elbowScale.set(0)
        self.shoulderScale.set(0)
        if int(value)>0:
            command2(BASE_COUNTERCLOCKWISE,self.lightVar.get())
        elif int(value)<0:
            command2(BASE_CLOCKWISE, self.lightVar.get())
        else:
            command2(STOP, self.lightVar.get())

find_arm()

Control = Window()
Control.grip_close()
