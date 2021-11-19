import time
import pyautogui

# Prevents pyautogui.FailSafeException to be raised if the
# mouse is in one of the screen corners during move(),
# see https://pyautogui.readthedocs.io/en/latest/#fail-safes
pyautogui.FAILSAFE = False

SECONDS_BETWEEN_MOVEMENTS = 60 * 3


def move():
    pyautogui.move(+1, +1)  # 1 pixel down and to the right
    pyautogui.move(-1, -1)  # 1 pixel up and to the left
    print("Last mouse movement occured on " + time.ctime())


while(True):
    move()
    time.sleep(SECONDS_BETWEEN_MOVEMENTS)
