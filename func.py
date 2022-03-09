from pynput.keyboard import Controller as co
from pynput.keyboard import Key
k = co()
def btn0():
    k.press(Key.enter)
    return