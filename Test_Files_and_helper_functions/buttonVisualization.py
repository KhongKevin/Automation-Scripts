import pyautogui
import time
import random

REPEAT_BATTLE_DISPLAY_MON_1 = [(1415, 670), (1720, 670), (1720,795), (1415,795)]
REPLAY_BOUNDS_DISPLAY_MON_1 = [(885, 850), (1150, 850), (1150,925), (885,925)]
SELL_SELECTED1_BOUNDS_DISPLAY_MON_1 = [(1495, 880), (1745, 880), (1745,925), (1495,925)]
SELL_SELECTED2_BOUNDS_DISPLAY_MON_1 = [(1305, 875), (1525, 875), (1525,945), (1305,945)]
YES_SELL_BOUNDS_DISPLAY_MON_1 = [(695, 585), (910, 585), (910,675), (695,675)]
BOX = [(1112,665),(1112+467,665),(1112+467,665-126),(1112,665-126)]
#Box(left=1112, top=665, width=467, height=126)
#Box(left=1112, top=379, width=467, height=126)
time.sleep(5)
left=1112 
top=379 
width=467
height=126
pyautogui.moveTo((left,top), duration = 0.5)
pyautogui.moveTo((left+width,top), duration = 0.5)
pyautogui.moveTo((left+width,top+height), duration = 0.5)
pyautogui.moveTo((left,top+height), duration = 0.5)

# for position in YES_SELL_BOUNDS_DISPLAY_MON_1: 
#     pyautogui.moveTo(position, duration = 1)
