import pyautogui
from pyautogui import *
import time
import keyboard
import numpy as np
import sys
import win32api, win32con, win32gui, win32com.client

time.sleep(2)

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
                time.sleep(1)
                if win32gui.GetForegroundWindow() != hwnd:
                    print("Unable to refocus NBA2K23")
                    sys.exit()
                else:
                    print("Successfully refocused")

            time.sleep(1)
            counter += 1
        else:
            print("Refocused")
        
def click(x, y):
    inFocus()
            
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(np.random.uniform(0.1, 0.3))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def locate(image):
    return pyautogui.locateOnScreen(image, grayscale=True, confidence=0.8)

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

def hold(key):
    inFocus()
    keyboard.press(key)
    time.sleep(np.random.uniform(9, 10))
    keyboard.release(key)

while keyboard.is_pressed('q') == False:
    time.sleep(2)

    if locate('goatlogo.png') != None:
        print("Menu")

        if locate('nextgame.png') != None:
            playnext_point = pyautogui.center(locate('nextgame.png')) 
            click(playnext_point.x, playnext_point.y)
            print("Next game")
            
            time.sleep(np.random.uniform(1, 2))

            #Skip anything that popped up 
            if locate('goatlogo.png') == None:
                print("Message popped up")
                while locate('goatlogo.png') == None:
                    press('2')

            #Confirm play next game
            if locate('nextgame3.png') != None:
                press('2')
            
            time.sleep(np.random.uniform(1, 2))

            #Check to skip team practice
            if locate('gsw_menu.png') == None:
                print("Skip team practice")
                keyboard.press('d')
                time.sleep(np.random.uniform(0.1, 0.2))
                keyboard.release('d')
                time.sleep(np.random.uniform(1, 1.5))

            time.sleep(np.random.uniform(1, 1.5))
            
            #Skip pick uniform
            while locate('yes.png') == None:
                press('2')
                time.sleep(np.random.uniform(0.5, 1))

            #Confirm start game
            yes_point = pyautogui.center(locate('yes.png'))
            click(yes_point.x, yes_point.y)
            print("Confirm start game")

            #Start game when loaded
            print("Loading game")
            while locate('continue.png') == None:
                time.sleep(1)
            press('2')
            print("Started")

            #Open pause menu
            paused = False
            while paused == False:
                if locate('nba_logo.png') == None:
                    press('esc')
                    time.sleep(np.random.uniform(0.5, 1.5))
                else:
                    print("Paused")
                    paused = True

            #Navigate to simcast
            for x in range(8):
                inFocus()
                keyboard.press('d')
                time.sleep(np.random.uniform(0.1, 0.2))
                keyboard.release('d')
                time.sleep(np.random.uniform(0.1, 0.5))

            press('2')

            #Pick user team
            if locate('warriors.png') != None:
                press('2')

            elif locate('warriors2.png') != None:
                press('s')
                press('2')
                
            print("Simcasting")

            #Skip timeout and halftime
            end = False
            while end == False:
                press('2')
                time.sleep(np.random.uniform(1, 1.5))
                if locate('mypoints.png') != None:
                    time.sleep(15)
                    end = True
                    
            print("End")

            time.sleep(np.random.uniform(8, 10))

    else:
        inFocus()

        time.sleep(2)
        if locate('contract.png') != None:

            print("Contract")
            press('2')

            if locate('goatlogo.png') != None:
                print("Returned to menu")

            else:
                time.sleep(1)

                while locate('vc.png') == None:
                    press('2')
                    time.sleep(1)

                if locate('counteroffer.png'):
                    press('2')

                #Max money, 0 incentive + discount
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
                
                time.sleep(np.random.uniform(3, 5))

                while locate('goatlogo.png') == None:
                    press('2')
                    time.sleep(np.random.uniform(3, 5))
        #else:
         #   press('2')
        time.sleep(1)