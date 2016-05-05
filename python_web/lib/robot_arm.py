
#######################################################################
# Library for controlling Maplin Robot arm
#######################################################################

#Import Python USB and Time
import usb.core, usb.util, time

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


class robot_arm:
    __arm_usb_device = None
    __light = 0
    __active_command = STOP

#######################################################################
# Constructor, connect to robot arm
#######################################################################
    def __init__(self):
        self.__arm_usb_device = usb.core.find(idVendor=0x1267, idProduct=0);

        if self.__arm_usb_device is None:
            raise ValueError('Device not found')

#######################################################################
# Abstract USB command send
#######################################################################
    def __usb_send(self, command):
        if self.__arm_usb_device is None:
            raise ValueError('Device not found. lost USB connection')

        self.__arm_usb_device.ctrl_transfer(0x40,6,0x100,0,command,1000)


#######################################################################
# Send movement command to arm
#######################################################################
    def move_arm(self, cmd):
        __active_command = cmd

        self.__usb_send(list(cmd) + [self.__light])


#######################################################################
# Send movement command to arm stopping after duration (in seconds)
#######################################################################
    def move_arm_timed(self, cmd, time_duration):
        self.move_arm(cmd)
        time.sleep(time_duration)
        self.stop()

#######################################################################
# Stop any active movement
#######################################################################
    def stop(self):
        self.__usb_send(STOP + [self.__light])


#######################################################################
# Turn Light On
#######################################################################
    def light_on(self):
        self.__light = 1
        self.__usb_send(self.__active_command + [self.__light])


#######################################################################
# Turn Light Off
#######################################################################
    def light_off(self):
        self.__light = 0
        self.__usb_send(self.__active_command + [self.__light])

