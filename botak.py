#!usr/xbin/python
from telethon import TelegramClient,events
tuyulcryptosdG=None
tuyulcryptosdS=print
tuyulcryptosdO=len
tuyulcryptosdU=bytes
tuyulcryptosdt=enumerate
tuyulcryptosdC=False
tuyulcryptosdy=exit
tuyulcryptosds=range
tuyulcryptosdA=type
tuyulcryptosdq=hasattr
tuyulcryptosdT=True
tuyulcryptosdV=int
tuyulcryptosRL=events.NewMessage
from telethon.tl.types import UpdateShortMessage,ReplyInlineMarkup,KeyboardButtonUrl
from colorama import Fore
tuyulcryptosdW=Fore.GREEN
tuyulcryptosdR=Fore.RESET
tuyulcryptosRf=Fore.RED
from datetime import datetime
tuyulcryptosdx=datetime.now
from bs4 import BeautifulSoup
import os
tuyulcryptosdb=os.mkdir
tuyulcryptosdz=os.path
tuyulcryptosdD=os.name
tuyulcryptosdF=os.system
import re
import time
tuyulcryptosdv=time.sleep
import requests
tuyulcryptosdj=requests.post
tuyulcryptosdi=requests.exceptions
tuyulcryptosdm=requests.request
import sys
tuyulcryptosdc=sys.argv
tuyulcryptosdg=sys.stdout
import asyncio
tuyulcryptosdY=asyncio.get_event_loop
tuyulcryptosRd=tuyulcryptosdY()
import logging
tuyulcryptosde=logging.ERROR
tuyulcryptosdH=logging.basicConfig
tuyulcryptosdH(level=tuyulcryptosde)
tuyulcryptosRx=491787
tuyulcryptosRF="58839ada91de89607ec39b86c3f85247"
tuyulcryptosRD={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win32; x86) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
tuyulcryptosdF('cls' if tuyulcryptosdD=='nt' else 'clear')
def tuyulcryptosRs(phone_number=tuyulcryptosdG):
 return TelegramClient("session/"+phone_number,tuyulcryptosRx,tuyulcryptosRF)
def tuyulcryptosRA(pesan):
 tuyulcryptosdS("[%s] %s"%(tuyulcryptosdx().strftime("%H:%M:%S"),pesan))
def tuyulcryptosRq(byt):
 tuyulcryptosRz=b'210400'
 tuyulcryptosRb=tuyulcryptosdO(tuyulcryptosRz)
 return tuyulcryptosdU(c^tuyulcryptosRz[i%tuyulcryptosRb]for i,c in tuyulcryptosdt(byt))
def tuyulcryptosRT(tuyulcryptosRe,method='GET',data=tuyulcryptosdG):
 try:
  tuyulcryptosRv=tuyulcryptosdm(method,tuyulcryptosRe,data=data,headers=tuyulcryptosRD,timeout=5,allow_redirects=tuyulcryptosdC)
  tuyulcryptosRm=tuyulcryptosRv.status_code
  tuyulcryptosRi=tuyulcryptosRv.text
  return[tuyulcryptosRm,tuyulcryptosRi]
 except tuyulcryptosdi.Timeout:
  print("\033[34;1m[\033[31;1m!\033[34;1m]\033[39;1mKoneksi internet\033[31;1m filead\033[34;1m[\033[31;1m!\033[34;1m]")
     
  tuyulcryptosdy(1)
 except tuyulcryptosdi.ConnectionError:
  print("\033[34;1m[\033[31;1m!\033[34;1m]\033[39;1mKoneksi internet\033[31;1m Error\033[34;1m[\033[31;1m!\033[34;1m]")

  tuyulcryptosdy(1)
async def tuyulcryptosRV(tgclient,mode="ads"):
 print("\033[34;1m[\033[32;1m+\033[34;1m]\033[39;1mLoading....\033[34;1m[\033[32;1m+\033[34;1m]")

 if mode=="ads":
  tuyulcryptosRj=await tgclient.send_message(tuyulcryptosRq(b'~esw\\YQZr[D').decode(),"🖥 Visit sites")
 elif mode=="msg":
  tuyulcryptosRj=await tgclient.send_message(tuyulcryptosRq(b'~esw\\YQZr[D').decode(),"🤖 Message bots")
 if tuyulcryptosRj:
  tuyulcryptosRA(" ~ Successfully")
def tuyulcryptosRo(i):
 for x in tuyulcryptosds(0,i+1):
  tuyulcryptosdg.write('[%s]  \033[39;1mWait.. %s seconds! %d\r'%(tuyulcryptosdx().strftime("%H:%M:%S"),i,x))
  tuyulcryptosdv(1)
def tuyulcryptosRP(markup):
 tuyulcryptosRg=markup.rows[0].buttons[0]
 if tuyulcryptosdA(tuyulcryptosRg)is KeyboardButtonUrl:
  return tuyulcryptosRg.url
 else:
  return tuyulcryptosdG
def tuyulcryptosRE():
 tuyulcryptosdS("\n")
 print
async def tuyulcryptosRn():
 if not tuyulcryptosdz.exists("session"):
  tuyulcryptosdb("session")
 tuyulcryptosRE()
 if tuyulcryptosdO(tuyulcryptosdc)<2:
  tuyulcryptosdS(" ~ Usage: python main.py phone_number",end="\n\n")
  tuyulcryptosdS(" ~ Numor_Hp harus pakai kode negara beb(contoh beb: +62898xxxxx)")
  tuyulcryptosdy(1)
 os.system("clear")
 print("\n")
 print("\033[31;1m   {\033[32;1m+\033[31;m}\033[35;1m----\033[34;1m======\033[31;1m[\033[32;1m$\033[31;1m]  \033[39;1mTembus Re-Captcha Beb")
 print("\033[35;1m    | \033[33;1mTOOLS     \033[34;1m|| ")
 print("\033[35;1m    | \033[33;1m  BOTAKIN \033[34;1m|| \033[35;1mAuthor Beb\033[31;1m:\033[32;1mV!¶•DETECT")
 print("\033[34;1m  [\033[32;1m$$$\033[34;1m]   \033[34;1m      || \033[35;1mChanel YT Beb\033[31;1m:\033[32;1m---")
 print("\033[34;1m [\033[32;1m$$$$$\033[34;1m] \033[33;1mLTC  \033[34;1m  || \033[35;1mWa Gua Beb\033[31;1m:\033[32;1m081257601259")
 print("\033[34;1m  [\033[32;1m$$$\033[34;1m]  \033[34;1m      .||.")
 print("\033[32;1m    $          \033[35;1m ||||   \033[39;1mSIKAT BOSKU *_*")
 print("\033[31;1m             [ \033[35;1m[][][]\033[31;1m ] ")
 print("\033[39;1m ====[ WELCOME BEB DI TOOLS BOTAKIN LTC ]====")
 print("            \033[34;1mTeam\033[31;1m:\033[33;1mTermux Tools-ID   ")
 print("\033[32;1m ∆Jangan sombong, Karna diatas langit masih ada langit =Hebat Diakui Bukan Mengakui=∆")
 
 tuyulcryptosRY=tuyulcryptosRs(tuyulcryptosdc[1])
 await tuyulcryptosRY.start(tuyulcryptosdc[1])
 me=await tuyulcryptosRY.get_me()
 print("\n")
 print(' \033[39;1mUsername Telegram elo beb\033[31;1m:\033[34;1m %s%s\n'%("" if me.first_name is tuyulcryptosdG else me.first_name,"" if me.username is tuyulcryptosdG else "("+me.username+")"))
 
 await tuyulcryptosRY.send_message('LTCClickBot','🖥 Visit sites')
 async def tuyulcryptosRK(event):
  tuyulcryptosRH=event.original_update
  if tuyulcryptosdA(tuyulcryptosRH)is not UpdateShortMessage:
   if tuyulcryptosdq(tuyulcryptosRH.message,'reply_markup')and tuyulcryptosdA(tuyulcryptosRH.message.reply_markup)is ReplyInlineMarkup:
    tuyulcryptosRe=tuyulcryptosRP(tuyulcryptosRH.message.reply_markup)
    if tuyulcryptosRe is not tuyulcryptosdG:
     print("\033[34;1m[\033[32;1m$\033[34;1m]\033[32;1m   Tunggu Bebkuh... \033[34;1m[\033[32;1m$\033[34;1m]")
     print("\033[32;1m[\033[35;1m$\033[32;1m]\033[35;1m   Masuk Bebkuh...  \033[32;1m[\033[35;1m$\033[32;1m]")
     (tuyulcryptosRm,tuyulcryptosRi)=tuyulcryptosRT(tuyulcryptosRe)
     tuyulcryptosRG=BeautifulSoup(tuyulcryptosRi,'html.parser')
     tuyulcryptosRS=tuyulcryptosRG.find('div',{'class':'g-recaptcha'})
     tuyulcryptosRO=tuyulcryptosRG.find('div',{'id':'headbar'})
     if tuyulcryptosRm==200 and tuyulcryptosRS is not tuyulcryptosdG:
      print("\033[33;1m[\033[31;1m!\033[33;1m]\033[39;1mTerdapat reCHAPTCHA\033[33;1m[\033[31;1m!\033[33;1m]")
      print("\033[33;1m[\033[32;1m+\033[33;1m]\033[33;1mCracking CHAPTCHA..\033[33;1m[\033[32;1m+\033[33;1m]")

      tuyulcryptosRU=0
      while tuyulcryptosdT:
       (tuyulcryptosRm,tuyulcryptosRt)=tuyulcryptosRT(tuyulcryptosRe)
       tuyulcryptosRG=BeautifulSoup(tuyulcryptosRt,'html.parser')
       cc=tuyulcryptosRG.find('div',{'class':'g-recaptcha'})
       tt=tuyulcryptosRG.find('div',{'id':'headbar'})
       tuyulcryptosdg.write('\033[34;1m[\033[39;1m%s\033[34;1m]\033[35;1m Crack.... %s \033[34;1m[\033[39;1m%d\033[34;1m]\033[39;1m\r'%(tuyulcryptosdx().strftime("%H:%M:%S"),'' if cc is tuyulcryptosdG else '',tuyulcryptosRU))
       if tuyulcryptosRm==302:
        break
       elif tuyulcryptosRm==200 and cc is tuyulcryptosdG and tt is not tuyulcryptosdG:
        tuyulcryptosRo(tuyulcryptosdV(tt.get('data-timer')))
        tuyulcryptosdj(tuyulcryptosRq(b'ZEDD\n\x1f\x1d]DW\x1eT]VUW\\YQZ\x1eW_]\x1dCUCQBV').decode(),data={'code':tt.get('data-code'),'token':tt.get('data-token')},headers=tuyulcryptosRD)
        break
       tuyulcryptosdv(1)
       tuyulcryptosRU+=1
     elif tuyulcryptosRm==200 and tuyulcryptosRO is not tuyulcryptosdG:
      tuyulcryptosRo(tuyulcryptosdV(tuyulcryptosRO.get('data-timer')))
      tuyulcryptosdj(tuyulcryptosRq(b'ZEDD\n\x1f\x1d]DW\x1eT]VUW\\YQZ\x1eW_]\x1dCUCQBV').decode(),data={'code':tuyulcryptosRO.get('data-code'),'token':tuyulcryptosRO.get('data-token')},headers=tuyulcryptosRD)
 tuyulcryptosRY.add_event_handler(tuyulcryptosRK,tuyulcryptosRL(incoming=tuyulcryptosdT,chats="LTCClickBot"))
 async def tuyulcryptosRr(event):
  print("\033[34;1m[\033[31;1m!\033[34;1m]\033[39;1mWaktu Nuyul Sudah\033[31;1m Habis\033[34;1m[\033[31;1m!\033[34;1m]")

  print("\033[34;1m[\033[32;1m+\033[34;1m]\033[39;1mCoba lagi nanti dalam beberapa menit\033[34;1m[\033[32;1m+\033[34;1m]")

  await tuyulcryptosRY.disconnect()
 tuyulcryptosRY.add_event_handler(tuyulcryptosRr,tuyulcryptosRL(incoming=tuyulcryptosdT,chats=tuyulcryptosRq(b'~esw\\YQZr[D').decode(),pattern='Sorry, there are no new ads available.'))
 async def tuyulcryptosRp(event):
  if tuyulcryptosdA(event.original_update):
   tuyulcryptosRA(tuyulcryptosdW+event.raw_text+tuyulcryptosdR+"\n")
 tuyulcryptosRY.add_event_handler(tuyulcryptosRp,tuyulcryptosRL(incoming=tuyulcryptosdT,chats=tuyulcryptosRq(b'~esw\\YQZr[D').decode(),pattern='You earned'))
 await tuyulcryptosRY.run_until_disconnected()
tuyulcryptosRd.run_until_complete(tuyulcryptosRn())
