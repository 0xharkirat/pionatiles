# (93, 430, 844-90 , 530 )

import pyautogui
import time
import keyboard
import win32api, win32con

print('starting script in 2 seconds...')

time.sleep(2)
print('now playing')


def click(x, y):
    win32api.SetCursorPos((x,y))
    
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)



    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0,0)


while keyboard.is_pressed('q') == False:

    pic = pyautogui.screenshot(region=(93, 430, 754 , 530))
    
    width, height = pic.size

    for x in range(0,width,5):
        for y in range(0,height,5):

            r,g,b = pic.getpixel(xy=(x,y))

            if b == 195:
                click(x+93, y+430)
                time.sleep(0.05)
                break





# (225, 219, 195)
