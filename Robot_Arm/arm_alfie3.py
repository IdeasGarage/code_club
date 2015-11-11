import sys
sys.path = [ './lib' ] + sys.path

from robot_arm import  *

arm = robot_arm ( )

arm.move_arm_timed(BASE_COUNTERCLOCKWISE,4)
arm.move_arm_timed(SHOULDER_DOWN,3)                                                              
arm.move_arm_timed(BASE_CLOCKWISE,8)
arm.move_arm_timed(SHOULDER_UP,3)
arm.move_arm_timed(BASE_COUNTERCLOCKWISE,4)