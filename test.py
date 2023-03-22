import pyautogui
from pyautogui import *
import time
import keyboard
import numpy as np
import sys
import win32api, win32con, win32gui, win32com.client

CONFIG = {
    'tap': (0.1, 0.1),
    'extra_short': (0.1, 0.2),
    'short': (0.1, 0.3),
    'medium': (0.5, 1),
    'long': (1, 2),
    'extra_long': (3, 5),
    'hold': (9, 10)
}

WINDOW_NAME = "NBA 2K23"

def random_sleep(duration):
    time.sleep(np.random.uniform(*CONFIG[duration]))

def in_focus():
    hwnd = win32gui.FindWindow(None, WINDOW_NAME)
    return win32gui.GetForegroundWindow() == hwnd

def refocus():
    hwnd = win32gui.FindWindow(None, WINDOW_NAME)
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(hwnd)

def ensure_focus():
    if not in_focus():
        print(f"{WINDOW_NAME} not in focus\nWill attempt to refocus {WINDOW_NAME} in 10 seconds")
        for _ in range(10):
            time.sleep(1)
            if in_focus():
                print("Refocused")
                break
        else:
            refocus()
            time.sleep(1)
            if in_focus():
                print("Successfully refocused")
            else:
                print("Unable to refocus")
                sys.exit()

def click(x, y):
    ensure_focus()
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    random_sleep('short')
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def press(key, sleep_duration='short'):
    ensure_focus()
    keyboard.press(key)
    random_sleep(sleep_duration)
    keyboard.release(key)

def locate(image):
    return pyautogui.locateOnScreen(image, grayscale=True, confidence=0.8)

def wait_for_image(image, timeout=None, action=None):
    start_time = time.time()
    while True:
        location = locate(image)
        if location != None:
            return location

        if timeout and time.time() - start_time > timeout:
            return None
        
        if action:
            action()

        time.sleep(1)

time.sleep(2)

#wait_for_image('vc.png', action=lambda: press('2'))

""" wait_for_image('counteroffer.png')         
press('2')


#Max money, 0 incentive + discount
press('d', sleep_duration='hold')
random_sleep('medium')
press('s', sleep_duration='tap')
random_sleep('medium')
press('a', sleep_duration='hold')
random_sleep('medium')
press('s', sleep_duration='tap')
random_sleep('medium')
press('a', sleep_duration='hold')
random_sleep('medium')  """

wait_for_image('goatlogo.png', action=lambda: press('2'))
print("found")
