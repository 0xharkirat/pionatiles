import pyautogui
import time
import keyboard
import win32api, win32con

# 341,796
# 447,817
# 557,832
# 660,847

time.sleep(5)

res = pyautogui.locateCenterOnScreen('start.png')
if res is not None:
    pyautogui.moveTo(res)
    pyautogui.click()


def click(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)

    time.sleep(0.05)

    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0,0)

while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(339,777)[0] == 0:
        click(339,777)
    if pyautogui.pixel(467,777)[0] == 0:
        click(467,777)
    if pyautogui.pixel(555,777)[0] == 0:
        click(555,777)
    if pyautogui.pixel(660,777)[0] == 0:
        click(660,777)
