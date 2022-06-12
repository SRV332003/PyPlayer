from PIL import ImageFont, Image, ImageDraw
from time import time
from time import sleep
import pyautogui as pt
from randomiser import randint
sleep(2)
def getresult(wrd):
    font = ImageFont.truetype(r'C:/Windows/Font/Calibri/calibrii.ttf', 14)
    font1 = ImageFont.truetype(r'C:/Windows/Font/Calibri/calibri.ttf', 14)
    wrd= wrd[0:1].upper()+wrd[1:]
    a, b = font.getsize(wrd+" is accepted")
    x, y= font.getsize(wrd)
    print(wrd)
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
def getWord(letter, num, words=[]):
    num=int(num)
    f = open("words1.txt", "rt").readlines()
    for x in f[randint(0,256):]:
        #print(x+" "+str(len(x))+" "+x[0:1])
        if x[0:1] == letter and len(x)-1 >= num and x not in words:
            #print(words)
            return x
 
words=[]
for _ in range(10):
    for x in "abcdefghuvwxyz":
        y= randint(4,9)
        l,n=x,y #map(str,input().split())
        wrd=getWord(l,n)
        print(wrd[:-1],end=" ")
        words+=[wrd]
    print()