import sys
sys.path = ['./lib'] + sys.path

from robot_arm import *

arm = robot_arm()

arm.light_on()

#Move arm timed takes a command, and time duration
#                  Command                Time
arm.move_arm_timed(BASE_COUNTERCLOCKWISE, 2)
arm.move_arm_timed(BASE_CLOCKWISE,        2)
            
arm.move_arm_timed(GRIP_CLOSE,            1)
arm.move_arm_timed(WRIST_UP,              1)
arm.move_arm_timed(WRIST_UP,            1)
arm.move_arm_timed(ELBOW_UP,              1)
arm.move_arm_timed(ELBOW_DOWN,            1)
arm.move_arm_timed(BASE_CLOCKWISE,           1)

arm.move_arm(WRIST_UP)
arm.move_arm_timed(STOP)

arm.light_on()
