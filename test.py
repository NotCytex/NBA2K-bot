import pyautogui
from pyautogui import *
import time
import keyboard
import numpy as np
import sys
import win32api, win32con, win32gui, win32com.client


def locate(image):
    return pyautogui.locateOnScreen(image, grayscale=True, confidence=0.8)

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def press(key):
    inFocus()
    keyboard.press(key)
    time.sleep(np.random.uniform(0.1, 0.3))
    keyboard.release(key)

def shortPress(key):
    inFocus()
    keyboard.press(key)
    time.sleep(0.1)
    keyboard.release(key)

def inFocus():
    window_name = "NBA 2K23"
    hwnd = win32gui.FindWindow(None, window_name)

    if win32gui.GetForegroundWindow() != hwnd:
        print("NBA2K23 not in focus\nWill attempt to refocus NBA2K23 in 10 seconds")
        counter = 0
        while win32gui.GetForegroundWindow() != hwnd:
            if counter > 10:
                shell = win32com.client.Dispatch("WScript.Shell")
                shell.SendKeys('%')
                win32gui.SetForegroundWindow(hwnd) 
                time.sleep(5)
                if win32gui.GetForegroundWindow() != hwnd:
                    print("Unable to refocus NBA2K23")
                    sys.exit()
                else:
                    print("Successfully refocused")
            time.sleep(1)
            counter += 1

def hold(key):
    inFocus()
    keyboard.press(key)
    time.sleep(np.random.uniform(10, 12))
    keyboard.release(key)

time.sleep(2)

hold('d')
time.sleep(np.random.uniform(0.5, 1))
shortPress('s')
time.sleep(np.random.uniform(0.5, 1))
hold('a')
time.sleep(np.random.uniform(0.5, 1))
shortPress('s')
time.sleep(np.random.uniform(0.5, 1))
hold('a')
time.sleep(np.random.uniform(0.5, 1))

while locate('goatlogo.png') == None:
    press('2')
    time.sleep(np.random.uniform(0.5, 1))
