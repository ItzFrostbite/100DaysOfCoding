import webbrowser
import keyboard
import random
import win32api
import win32con
from pyautogui import press, typewrite, hotkey
from time import sleep
from pynput.keyboard import Key, Controller

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

key = Controller()

rand = int(random.randint(1,200))

def repeat_func(times, f):
    for i in range(times): f()

def pageDown():
    press('pagedown')

webbrowser.open("https://twitter.com")

print("Starting In 5")
sleep(1)
print("4")
sleep(1)
print("3")
sleep(1)
print("2")
sleep(1)
print("1")
sleep(1)
print("GOOOOO!!!")
print("Random Number Is:", rand)


repeat_func(rand, pageDown)
sleep(0.5)
click(700,400)
