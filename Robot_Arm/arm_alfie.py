import sys
sys.path = [ ‘ . /lib’ ] + sys.path

from robot_arm import  *

arm = robot_arm ( )

arm.move_arm_timed(WRIST_DOWN,4)
arm.move_arm_timed(GRIP_CLOSE,2)                                                              
arm.move_arm_timed(ELBOW_DOWN,3)
arm.move_arm_timed(SHOULDER_UP,1)
arm.move_arm_timed(BASE_COUNTERCLOCKWISE,2)
arm.move_arm_timed(BASE_CLOCKWISE,2)
                   