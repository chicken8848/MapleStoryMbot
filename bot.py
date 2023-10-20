import pyautogui as ag
import random
import time
import cv2

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
    randompointx = box.left+random.random()*box.width
    randompointy = box.top+random.random()*box.height
    randomsleep()
    ag.click(randompointx, randompointy)


def locate(image):
    return ag.locateOnScreen(image, confidence=CONFIDENCE_INTERVAL)

def start():
    input("Press any key to start...")
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
    pass
start()
res = ag.locateOnScreen("photoarchive/newquest.png", confidence=0.8)
print(res)
if res != None:
    ag.press("tab")
