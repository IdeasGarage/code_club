# Pygame init
import sys, pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))

# Arm init
sys.path = ['./lib'] + sys.path
from robot_arm import *

arm = robot_arm()

#Main event loop
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
        # Base
            if event.key == pygame.K_LEFT:
                arm.move_arm(BASE_COUNTERCLOCKWISE)

            if event.key == pygame.K_RIGHT:
                arm.move_arm(BASE_CLOCKWISE)

        # Shoulder
            if event.key == pygame.K_UP:
                arm.move_arm(SHOULDER_UP)

            if event.key == pygame.K_DOWN:
                arm.move_arm(SHOULDER_DOWN)

        # Elbow
            if event.key == pygame.K_y:
                arm.move_arm(ELBOW_UP)

            if event.key == pygame.K_u:
                arm.move_arm(ELBOW_DOWN)

        # Wrist
            if event.key == pygame.K_h:
                arm.move_arm(WRIST_UP)

            if event.key == pygame.K_j:
                arm.move_arm(WRIST_DOWN)

        # Grip
            if event.key == pygame.K_n:
                arm.move_arm(GRIP_OPEN)

            if event.key == pygame.K_m:
                arm.move_arm(GRIP_CLOSE)

        if event.type == pygame.KEYUP:
            arm.stop()

        
        pygame.display.flip()


