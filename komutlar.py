import urllib.request
import json
from gtts import gTTS 
from playsound import playsound
import os
import sys
from random import choice
import request
from lxml import html

class Komut():
    def__init__(self,gelenSes):
    self.ses=gelenSes.upper()
    self.sesBloklari=self.ses.split()
    print(self.sesBloklari)
    self.komutlar=["ABONE", "CEVİR","NABER","NASILSIN","KAPAT","HAVA"]

    #KOMUT VE  İSLEMLERİ
 def seslendirme(selfiyazi):
     tts=gTTS(text=yazi,lang='tr')
     tts.save("ses.mp3")
     playsound("ses.mp3")
     os.remove("ses.mp3")
