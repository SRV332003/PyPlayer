##########____________Credential For Player____________###########
username="Sourav Garg"                        # Your Telegram name
##################### ############################################

import pyautogui as pt
import os
import pyperclip as pyp
from time import sleep
from PIL import Image, ImageFont, ImageDraw
from time import time
from random import randint,shuffle,choice
sleep(1)
screen=pt.size()
words=[]
###########Functions#################

def getresult(wrd):
    font = ImageFont.truetype(r'C:/Windows/Font/Calibri/calibrili.ttf', 14)
    font1 = ImageFont.truetype(r'C:/Windows/Font/Calibri/calibri.ttf', 14)
    wrd= wrd[0:1].upper()+wrd[1:]
    a, b = font.getsize(wrd+" is accepted")
    x, y= font.getsize(wrd)
    print(a)
    print(b)
    img1 = Image.new("RGBA", (a + 20, b + 18), 'white')
    ImageDraw.Draw(img1).text((10, 9), wrd, font=font, fill=(0, 0, 0, 255))
    ImageDraw.Draw(img1).text((x+10, 9), " is accepted.", font=font1, fill=(0, 0, 0, 255))
    img1.save('word.png', quality=50)
    current=time()
    cor = pt.locateCenterOnScreen(img1, confidence=0.6)
    while time() < current+3 and cor is None:
        cor = pt.locateCenterOnScreen(img1, confidence=0.6)
    return cor is not None
f = open("words1.txt", "rt").readlines()
def getWord(letter, num, words):
    num=int(num)
    while True:
        #print(x+" "+str(len(x))+" "+x[0:1])
        x=choice(f)
        if x[0:1] == letter and len(x)-1 >= num and len(x)-1<=num+2 and x not in words:
            return x
 

name=""
############ Check Turn #############
while True:
    if pt.locateOnScreen("selectmsg.png", confidence=0.9):
        pt.hotkey('esc')
    flag=False
    while True:
        turnpt = pt.locateOnScreen("img.png", confidence=0.9)
        var=pt.position()
        if var[1]==0:
            flag=True
            break
        if turnpt is not None and turnpt[1] > int(screen[1]/2):
            break
    if flag:
        break
    #    Check For Name
    pt.moveTo(turnpt[0]+66, turnpt[1]+19)
    pt.click()
    sleep(0.2)
    pt.dragTo(turnpt[0]+300, turnpt[1]+19)
    pt.hotkey('ctrl', 'c')
    string=pyp.paste()
    temp=name
    name = string[6:len(username)+6]
    if temp!=name:
        print("Turn of "+name+": ")
    if name == username:
        # Check for letter and num
        pt.moveTo(turnpt[0]+68, turnpt[1]+37)
        pt.click()
        pt.dragTo(turnpt[0]+410, turnpt[1]+37)
        pt.hotkey('ctrl', 'c')
        #Sample ---> "Your word must start with S and include at least 8 letters."
        string = pyp.paste()
        letter = string[26:27].lower()
        try:    
            num = int(string[49:51].strip())
        except:
            continue
        print(letter, num)
        word = getWord(letter, num, words)
        words+=[word]
        print("The word is "+word)
        while True:
            a=pt.locateCenterOnScreen("write.png",confidence=.8)
            if a is not None:
                break
        pt.click(a[0], a[1])
        pt.typewrite(word)
        '''while getresult(word) is False:
            word = getWord(letter, num, words)
            words+=[word]
            print("The word is "+word)
            while True:
                a=pt.locateCenterOnScreen("write.png",confidence=.8)
                if a is not None:
                    break
            pt.click(a[0], a[1])
            pt.typewrite(word)
        '''