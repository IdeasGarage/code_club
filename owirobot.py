"""
   Copyright 2013 Steve Battle

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import usb.core
import usb.util
import time
from Tkinter import *

root = Tk()
dev = usb.core.find(idVendor=0x1267, idProduct=0);

if dev is None:
    raise ValueError('Device not found')

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

def command2(cmd, light):
    c = list(cmd)
    c.append(light)
    dev.ctrl_transfer(0x40,6,0x100,0,c,1000)

def command(cmd, light, duration):
    c = list(cmd)
    c.append(light)
    dev.ctrl_transfer(0x40,6,0x100,0,c,1000)
    time.sleep(duration)
    c = list(STOP)
    c.append(light)
    dev.ctrl_transfer(0x40,6,0x100,0,c,1000)

class Window:
    def __init__(self, parent):
        frame = Frame(parent)
        frame.pack()
        
        Label(frame, text="OWI Robot").grid(row=0, column=1)

        Label(frame, text="Gripper:").grid(row=1)
        self.btn1 = Button(frame, text="close", command=self.grip_close)
        self.btn1.grid(row=1, column=1)

        self.btn2 = Button(frame, text="open", command=self.grip_open)
        self.btn2.grid(row=1, column=2)

        Label(frame, text="Wrist:").grid(row=2)
        self.wristScale = Scale(frame, from_=-1, to=1, orient=HORIZONTAL, command=self.wrist)
        self.wristScale.grid(row=2, column=1)

        Label(frame, text="Elbow:").grid(row=3)
        self.elbowScale = Scale(frame, from_=-1, to=1, orient=HORIZONTAL, command=self.elbow)
        self.elbowScale.grid(row=3, column=1)

        Label(frame, text="Shoulder:").grid(row=4)
        self.shoulderScale = Scale(frame, from_=-1, to=1, orient=HORIZONTAL, command=self.shoulder)
        self.shoulderScale.grid(row=4, column=1)

        Label(frame, text="Base:").grid(row=5)
        self.baseScale = Scale(frame, from_=-1, to=1, orient=HORIZONTAL, command=self.base)
        self.baseScale.grid(row=5, column=1)
        
        self.lightVar = IntVar()
        self.cb = Checkbutton(frame, text="Light", command=self.light, variable=self.lightVar, offvalue=0, onvalue=1)
        self.cb.grid(row=6)


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
            
window = Window(root)
root.mainloop()
