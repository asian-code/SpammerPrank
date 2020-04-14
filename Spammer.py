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
c=0
keytyper = Controller()
triggerKey=Key.f4
#to do list:
# option 1 spams the whole text file
# option 2 spames only when holding down the trigger button

def textCleanUp(text):
    # remove all \n
    text = text.replace("\n", " ")
    text = text.split(" ")
    return text

def Menu():
    print("---Options--------------------------")
    print(" [0] Spam each word until end of file\n [1] Spam when holding down left 'alt'")
    print("------------------------------------\n")

def selectFile():
    try:
        print("Please select a file")
        root = Tk().withdraw(
        )  # withdraw prevents the tiny window from popping up
        location = filedialog.askopenfilename(initialdir="/~",title="Select file",filetypes=(("text files","*.txt"),("all files", "*.*")))
        if location == "":
            print(red + "[!] No file was selected" + r)
            return False
        print("LOCATION: " + location)
        return location

    except:
        print(red + "[!] Error trying to get file, please try again" + r)
        print(red + "---Error message--------------------" + r)
        raise

def on_press0(key):
    if key == triggerKey:
        print("start signal pressed: ")
    #print('{0} pressed'.format(key))

def on_release0(key):
    #print('{0} released'.format(key))

    # Starting
    if key == triggerKey:
        for i in text:
            keytyper.type(i)
            # Enter button
            keytyper.press(Key.enter)
            keytyper.release(Key.enter)
            # wait a few mili seconds
            time.sleep(seconds)
        return False
    # Stop listener
    if key == Key.esc:
        return False

def on_press1(key):
    global c
    if key == triggerKey:
        keytyper.type(text[c])
        # Enter button
        keytyper.press(Key.enter)
        keytyper.release(Key.enter)
        #counter
        if c < len(text)-1:
            c+=1
        else:
            return False
        
def on_release1(key):
    # Stop listener
    if key == Key.esc:
        return False

def startSpam0():
    print(
        r +
        "---{0}Starting{1}----------------------------------\n{0}[!] PRESS 'f4' button to Start, Press 'esc' to quit{1}\n"
        .format(cyan, r))
    with Listener(on_press=on_press0, on_release=on_release0) as listener:
        listener.join()

def startSpam1():
    print(
        r +
        "---{0}Starting{1}----------------------------------\n{0}[!] HOLD 'f4' button to Start, Press 'esc' to quit{1}\n"
        .format(cyan, r))
    with Listener(on_press=on_press1, on_release=on_release1) as listener:
        listener.join()

def main():
    global text
    location = selectFile()
    if location is False:
        return
    # read text data from file
    file = io.open(location,'r',encoding='utf8')
    text = file.read()
    # print(text)
    file.close()
    text = textCleanUp(text)

    Menu()
    userInput=input("[*] Select option: ")
    userInput=userInput.replace(" ","")

    if userInput=="0":
        startSpam0()
    if userInput=="1":
        startSpam1()
    
    


main()
