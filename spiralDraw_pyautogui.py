# open paint 
# after starting the program bring the pointer into to paint program and watch the magic

import pyautogui as p
import time

time.sleep(5) # 5 second delay so that after running the program you have time to bring the pointer to paint program
p.click()
distance = 200
while distance > 0:
    p.dragRel(distance,0,duration=0.2)  # move right
    distance = distance -5
    p.dragRel(0,distance,duration=0.2)  # move down
    p.dragRel(-distance,0,duration=0.2) # move left
    distance = distance - 5
    p.dragRel(0,-distance,duration=0.2) # move up