from pynput.keyboard import Key, Controller, Listener
import time
from tkinter import filedialog
from tkinter import *
import io
cyan = '\033[36m'
red = '\033[31m'
r = '\033[0m'  # reset
green = '\033[32m'
text = []
seconds = .1
c=0 # option 0 counter
keytyper = Controller()
triggerKey=Key.f4
times=0 # option 2 

def textCleanUp(text):
    # remove all \n
    text = text.replace("\n", " ")
    text = text.split(" ")
    return text

def logo():
    print('''{}  ____                                            
 / ___| _ __   __ _ _ __ ___  _ __ ___   ___ _ __ 
 \___ \| '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ | '__|
  ___) | |_) | (_| | | | | | | | | | | |  __| |   
 |____/| .__/ \__,_|_| |_| |_|_|_|_| |_|\___|_|   
       |_|{}_ __  _ __ __ _ _ __ | | __             
         | '_ \| '__/ _` | '_ \| |/ /             
         | |_) | | | (_| | | | |   <              
         | .__/|_|  \__,_|_| |_|_|\_\             
         |_| {}Made by Asian-code{}\n\n'''.format(red,cyan,green,r))

def Menu():
    print("---{0}File Options{1}--------------------------".format(cyan,r))
    print(" [{0}0{1}] Spam when holding down 'f4' key. (Controlled)\n [{0}1{1}] Spam each word in a file. (Uncontrolled)".format(cyan,r))
    print("\n---{}Other Options{}-------------------------".format(cyan,r))
    print(" [{0}2{1}] Spam a word/phrase a number of times\n".format(cyan,r))
    print("-----------------------------------------\n")

def on_press0(key):
    # Starting
    if key == triggerKey:
        for i in text:
            keytyper.type(i)
            # Enter button
            keytyper.press(Key.enter)
            keytyper.release(Key.enter)
            # wait a few mili seconds
            time.sleep(seconds)
        print(cyan+"[+] Reached end of file"+r)
        return False

def on_release(key):
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
            print(cyan+"[+] Reached end of file"+r)
            return False

def on_press2(key):
    if key == triggerKey:
        for i in range(times):
            keytyper.type(text)
            # Enter button
            keytyper.press(Key.enter)
            keytyper.release(Key.enter)
            time.sleep(seconds)
        return False

def StartSpam(onPress,onRelease,message):
    print(r +"---{0}Starting{1}----------------------------------\n{0}{2}{1}\n"
        .format(cyan, r,message))
    with Listener(on_press=onPress, on_release=onRelease) as listener:
        listener.join()

def main():
    global text,times
    logo()
    Menu()
    userInput=input("[*] Select option: "+cyan)
    userInput=userInput.replace(" ","")
    print(r)# resets color

    # checks if input is valid
    valid=["0","1","2"]
    if userInput not in valid:
        userInput="0"# default 

    if userInput=="2":
        text=input(r+"[*] Enter Text: "+cyan)
        times=int(input(r+"[*] # of times: "+cyan))
        StartSpam(on_press2,on_release,"[!] PRESS 'f4' button to Start, Press 'esc' to quit")
        return 

    # prompt user to select a Folder
    try:
        print("Please select a file")
        root = Tk()
        # withdraw prevents the tiny window from popping up
        location = filedialog.askopenfilename(initialdir="/~",title="Select file",filetypes=(("text files","*.txt"),("all files", "*.*")))
        if location == "":
            print(red + "[!] No file was selected" + r)
            return
        print("LOCATION: " + location)

    except:
        print(red + "[!] Error trying to get file, please try again" + r)
        print(red + "---Error message--------------------" + r)
        raise 

    # read text data from file
    file = io.open(location,'r',encoding='utf8')
    text = file.read()
    file.close()

    text = textCleanUp(text)    
    if userInput=="1":
        StartSpam(on_press0,on_release,"[!] PRESS 'f4' button to Start, Press 'esc' to quit")
    if userInput=="0":
        StartSpam(on_press1,on_release,"[!] HOLD 'f4' button to Start, Press 'esc' to quit")
    
main()
