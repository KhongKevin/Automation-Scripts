import swmacros as sw
import pyautogui
import time
import random
import win32gui
import win32con
import Test_Files_and_helper_functions.detection as detection
import os
import Test_Files_and_helper_functions.picToCornerCoords as picToCornerCoords

sw.changeWindows("Summoners War - Mumu Player")
time.sleep(2)
sw.dragClick(sw.randomPointWithinRect(picToCornerCoords.picToCornerCoordsMediumRes("images\9x10repeat_battleNEW.png") ))