import pyautogui as pya

def greetUser():
   
    pya.PAUSE = 1
    pya.FAILSAFE = True
    pya.confirm('You will not be able to use your device while the robot is running.\n\nYou may abort the process by moving your cursor to the top left corner of your main monitor.\n\nBe patient and enjoy the time being saved!')