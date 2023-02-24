import pyautogui
import time
import random

necroTime1 = 848
necroTime2 = 900
repeatTimes = 5

faimonTime1 = 300
faimonTime2 = 310
REPEAT_BATTLE_DISPLAY_MON_1 = [(1415, 670), (1720, 670), (1720,795), (1415,795)]
REPLAY_BOUNDS_DISPLAY_MON_1 = [(885, 850), (1150, 850), (1150,925), (885,925)]
SELL_SELECTED1_BOUNDS_DISPLAY_MON_1 = [(1495, 880), (1745, 880), (1745,925), (1495,925)]
SELL_SELECTED2_BOUNDS_DISPLAY_MON_1 = [(1305, 875), (1525, 875), (1525,945), (1305,945)]
YES_SELL_BOUNDS_DISPLAY_MON_1 = [(695, 585), (910, 585), (910,675), (695,675)]


def randomPointWithinRect(rect):
    # Define the corners of the rectangle
    top_left = rect[0]
    top_right = rect[1]
    bottom_right = rect[2]
    bottom_left = rect[3]

    # Get the x and y limits of the rectangle
    x_min, y_min = top_left
    x_max, y_max = bottom_right

    # Generate random coordinates within the rectangle
    x = random.uniform(x_min, x_max)
    y = random.uniform(y_min, y_max)
    return (x,y)

def tap(position):
    print("tap!")

    # Move the mouse to the starting position of the object to be dragged
    pyautogui.moveTo(position)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    print("clickDuration: instant")
    print("clickLocation: ", position)
def dragClick(position):
    print("dragClick!")
    xTranslate = random.randint(-15,15)
    yTranslate = random.randint(-15,15)
    durationRandom = random.uniform(0.1,0.4)
    pyautogui.moveTo(position[0]+xTranslate, position[1]+yTranslate)
    pyautogui.mouseDown()
    pyautogui.dragTo(position, duration=durationRandom)
    pyautogui.mouseUp()
    print("clickDuration: ", durationRandom)
    print("clickLocation: ", position)

def dragClick2(position):
    print("dragClick2!")
    xTranslate = random.randint(-15,15)
    yTranslate = random.randint(-15,15)
    xTranslate2 = random.randint(-10,10)
    yTranslate2 = random.randint(-10,10)
    durationRandom = random.uniform(0.1,0.3)
    pyautogui.moveTo(position[0]+xTranslate, position[1]+yTranslate)
    pyautogui.mouseDown()
    pyautogui.dragTo(position, duration=durationRandom)
    durationRandom = random.uniform(0.1,0.3)
    pyautogui.moveTo(position[0]+xTranslate2, position[1]+yTranslate2)
    pyautogui.dragTo(position, duration=durationRandom)
    pyautogui.mouseUp()
    print("clickDuration: ", durationRandom)
    print("clickLocation: ", position)

def holdClick(position):
    print("holdClick!")
    durationRandom = random.uniform(0.2,0.6)
    pyautogui.moveTo(position)
    pyautogui.mouseDown()
    time.sleep(durationRandom)
    pyautogui.mouseUp()
    print("clickDuration: ", durationRandom)
    print("clickLocation: ", position)


# Create a list of functions
clickTypes = [tap, dragClick, holdClick]


time.sleep(4)
for i in range(repeatTimes):
    print("iteration ", i)
    print("repeat press")
    randomClickType = random.choice(clickTypes)
    randomClickType(randomPointWithinRect(REPEAT_BATTLE_DISPLAY_MON_1))
    time.sleep(random.uniform(faimonTime1, faimonTime2))
    print("sell 1 press")
    randomClickType = random.choice(clickTypes)
    randomClickType(randomPointWithinRect(SELL_SELECTED1_BOUNDS_DISPLAY_MON_1))
    time.sleep(random.uniform(5, 10))
    print("sell 2 press")
    randomClickType = random.choice(clickTypes)
    randomClickType(randomPointWithinRect(SELL_SELECTED2_BOUNDS_DISPLAY_MON_1))
    time.sleep(random.uniform(8, 10))
    print("yes press")
    randomClickType = random.choice(clickTypes)
    randomClickType(randomPointWithinRect(YES_SELL_BOUNDS_DISPLAY_MON_1))
    time.sleep(random.uniform(3, 10))
    print("replay press")
    randomClickType = random.choice(clickTypes)
    randomClickType(randomPointWithinRect(REPLAY_BOUNDS_DISPLAY_MON_1))
    time.sleep(random.uniform(3, 10))



