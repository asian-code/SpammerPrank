from pynput.keyboard import Key, Controller, Listener
import time
from tkinter import filedialog
from tkinter import *
import io
cyan = '\033[36m'
red = '\033[31m'
r = '\033[0m'  # reset
text = []
seconds = .1
#to do list:
# option 1 spams the whole text file
# option 2 spames only when holding down the trigger button

def textCleanUp(text):
    # remove all \n
    text = text.replace("\n", " ")
    text = text.split(" ")
    return text


def on_press(key):
    if key == Key.alt_l:
        print("start signal pressed: left Alt")
    #print('{0} pressed'.format(key))


def on_release(key):
    #print('{0} released'.format(key))

    # Starting
    if key == Key.alt_l:
        keytyper = Controller()
        for i in text:
            keytyper.type(i)
            # Enter button
            keytyper.press(Key.enter)
            keytyper.release(Key.enter)
            # wait a few mili seconds
            time.sleep(seconds)
    # Stop listener
    if key == Key.esc:
        return False


def main():
    global text
    location = ""
    print("Please select a file")
    time.sleep(.5)
    try:
        root = Tk().withdraw(
        )  # withdraw prevents the tiny window from popping up
        location = filedialog.askopenfilename(initialdir="/",title="Select file",filetypes=(("text files","*.txt"),("all files", "*.*")))
        if location == "":
            print(red + "[!] No file was selected" + r)
            return
        print("LOCATION: " + location)
        #root.destroy()
        # read text data from file
        file = io.open(location,'r',encoding='utf8')
        text = file.read()
        # print(text)
        file.close()
        text = textCleanUp(text)

    except:
        print(red + "[!] Error trying to get file, please try again" + r)
        print(red + "---Error message--------------------" + r)
        raise

    print(
        r +
        "---{0}Starting{1}----------------------------------\n{0}[!] Press left 'alt' button to Start, Press 'esc' to quit{1}\n\n"
        .format(cyan, r))
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


main()
