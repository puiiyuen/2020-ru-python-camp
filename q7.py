# Author: Patrick
# Date: 2020/12/21

# Task/Requirement: A robot moves in a plane starting from the original point (0,0). The robot can move toward
# UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following: UP 5
# DOWN 3 LEFT 3 RIGHT 2. The numbers after the direction are steps. Write a program to compute the distance
# from current position after a sequence of movement and original point. If the distance is a float, then just print
# the nearest integer.

import math

def main():
    x = 0
    y = 0
    op = 'UP'
    step_size = 0
    while (op == 'UP' or op == 'DOWN' or op == 'LEFT' or op == 'RIGHT'):
        op = input(
            'Input the direction(UP,DOWN,LEFT,RIGHT,other words for ending the operation): ')
        if op == 'UP':
            step_size = int(input("Input the size of the step: "))
            y += step_size
        elif op == 'DOWN':
            step_size = int(input("Input the size of the step: "))
            y -= step_size
        elif op == 'LEFT':
            step_size = int(input("Input the size of the step: "))
            x -= step_size
        elif op == 'RIGHT':
            step_size = int(input("Input the size of the step: "))
            x += step_size
        else:
            break
    distance = math.ceil(math.sqrt(x**x+y**y))
    print ("The distance is ", distance)


if __name__ == "__main__":
    main()


# OUTPUT:
# Input the direction(UP,DOWN,LEFT,RIGHT,other words for ending the operation): UP
# Input the size of the step: 5
# Input the direction(UP,DOWN,LEFT,RIGHT,other words for ending the operation): DOWN
# Input the size of the step: 3
# Input the direction(UP,DOWN,LEFT,RIGHT,other words for ending the operation): LEFT
# Input the size of the step: 3
# Input the direction(UP,DOWN,LEFT,RIGHT,other words for ending the operation): RIGHT
# Input the size of the step: 2
# Input the direction(UP,DOWN,LEFT,RIGHT,other words for ending the operation): E
# The distance is  2