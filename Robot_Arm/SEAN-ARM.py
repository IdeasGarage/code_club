import sys
sys.path = [ './lib' ] + sys.path

from robot_arm import  *

arm = robot_arm ( )

arm.move_arm_timed(BASE_COUNTERCLOCKWISE, 10)
arm.move_arm_timed(ELBOW_UP,4)
arm.move_arm_timed(GRIP_OPEN,2)                                                              
arm.move_arm_timed(BASE_CLOCKWISE,1)
arm.move_arm_timed(SHOULDER_DOWN,3)
arm.move_arm_timed(WRIST_UP,1)