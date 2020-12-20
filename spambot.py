from pynput.keyboard import Key, Controller
import time
 
message = "spambot by sasank "
keyboard = Controller()
 
time.sleep(5)
 
for num in range(100):
    for letter in message:
        keyboard.press(letter)
        keyboard.release(letter)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1)
 
