import pyautogui as ag
import random
import time
import cv2
import keyboard
from photoarchivelib import *

MAX_RANDOM_TIME = 0.5
CONFIDENCE_INTERVAL = 0.8

def randomsleep():
    time.sleep(MAX_RANDOM_TIME*random.random())

def presskey(key):
    randomsleep()
    ag.keyDown(key)
    randomsleep()
    ag.keyUp(key)

def click(box):
    if box is None:
        return
    randompointx = box.left+random.random()*box.width
    randompointy = box.top+random.random()*box.height
    randomsleep()
    ag.click(randompointx, randompointy)


def locate(image):
    return ag.locateOnScreen(image, grayscale = False, confidence=CONFIDENCE_INTERVAL)

def start():
    input("Enter any key to start...\n")
    print("Starting in 5")
    time.sleep(1)
    print("Starting in 4")
    time.sleep(1)
    print("Starting in 3")
    time.sleep(1)
    print("Starting in 2")
    time.sleep(1)
    print("Starting in 1")
    time.sleep(1)

def scan():
    for photo in photolib:
        location = locate(photo)
        if location is not None:
            return photo
    return None

def dothething(photo):
    if photo is None:
        return
    if photo in clickable:
        click(locate(photo))
    if photo in finished_quest:
        time.sleep(2)
        presskey('tab')
    elif photo in pressable.keys():
        presskey(pressable[photo])

def main():
    start()
    start_time = time.time()
    while keyboard.is_pressed('q') is False:
        found = None
        while found is None and keyboard.is_pressed('q') is False:
            found = scan()
            end_time = time.time()
            elapsed_time = end_time - start_time
            if elapsed_time > 300:
                presskey("tab")
        if keyboard.is_pressed('q') is True:
            break
        dothething(found)

main()

