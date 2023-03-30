import pyautogui
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

def main(flag):
    while flag[0]:
        random_sleep('extra_long')

        if locate('images/mc.png') != None:
                print("Return to menu")
                wait_for_image('images/goatlogo.png', action=lambda: press('3'))
        
        if locate('images/goatlogo.png') != None:
            print("Menu")

            if wait_for_image('images/nextgame.png') != None:
                playnext_point = pyautogui.center(locate('images/nextgame.png')) 
                click(playnext_point.x, playnext_point.y)
                print("Next game")
                
                random_sleep('long')

                #Skip anything that popped up 
                if locate('images/goatlogo.png') == None:
                    print("Message popped up")
                    wait_for_image('images/goatlogo.png', timeout=10)
                    press('2')

                #Confirm play next game
                if locate('images/nextgame3.png') != None:
                    press('2')
                
                random_sleep('long')

                #Check to skip team practice
                if locate('images/gsw_menu.png') == None:
                    print("Skip team practice")
                    press('d', sleep_duration='extra_short')
                    random_sleep('long')

                random_sleep('long')
                
                #Skip pick uniform
                wait_for_image('images/yes.png', action=lambda: press('2'))

                #Confirm start game
                yes_point = pyautogui.center(locate('images/yes.png'))
                click(yes_point.x, yes_point.y)
                print("Confirm start game")

                #Start game when loaded
                print("Loading game")
                wait_for_image('images/continue.png')
                press('2')
                print("Started")

                #Open pause menu
                wait_for_image('images/nba_logo.png', action=lambda: press('esc'))

                #Navigate to simcast
                for _ in range(8):
                    press('d', sleep_duration='tap')
                    random_sleep('medium')

                press('2')

                #Pick user team
                if locate('images/warriors.png') != None:
                    press('2')

                elif locate('images/warriors2.png') != None:
                    press('s')
                    press('2')
                    
                print("Simcasting")

                #Skip timeout and halftime
                wait_for_image('images/mypoints.png', action=lambda: press('2'))                 
                print("End")

        else:
            if locate('images/contract.png') != None:
                print("Contract")
                press('2')

                if wait_for_image('images/goatlogo.png', timeout=3) != None:
                    print("Returned to menu")

                else:
                    random_sleep('long') 

                    wait_for_image('images/vc.png', action=lambda: press('2'))
                    
                    wait_for_image('images/counteroffer.png')
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
                    random_sleep('medium')

                    wait_for_image('images/goatlogo.png', action=lambda: press('2'))