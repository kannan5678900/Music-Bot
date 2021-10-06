from spotify import DOWNLOADMP3 as SONGDOWNLOADER
import telepot
import spotify
import requests
import threading
import os
from pyrogram import Client, filters

from bot import BOT_TOKEN

def txtfinder(txt):
    a = txt.find("https://open.spotify.com")
    txt = txt[a:]
    return txt

def cantfind(chat_id):
    bot.sendSticker(chat_id, 'CAACAgQAAxkBAAIBE2BLNclvKLFHC-grzNdOEXKGl6cLAALzAAMSp2oDSBk1Yo7wCGUeBA')
    bot.sendMessage(chat_id, "can't find it")

def cantfindone(chat_id):
    bot.sendSticker(chat_id, 'CAACAgQAAxkBAAIFSWBF_m3GHUtZJxQzobvD_iWxYVClAAJuAgACh4hSOhXuVi2-7-xQHgQ')
    bot.sendMessage(chat_id, "can't download one of them")

def downloader(link,chat_id,type):
    PLAYLIST = False
    if type=='AL':
        ITEMS = spotify.album(link)
    elif type == 'AR':
        ITEMS = spotify.artist(link)
    elif type == 'PL':
        ITEMS = spotify.playlist(link)
        PLAYLIST = True
    else:
        ITEMS = []

    MESSAGE = ""
    COUNT = 0
    for song in ITEMS:
        if PLAYLIST:
            song = song['track']
        COUNT+=1
        MESSAGE += f"{COUNT}. {song['name']}\n"
    bot.sendMessage(chat_id, MESSAGE)
    for song in ITEMS:
        if PLAYLIST:
            song = song['track']

        try:
            SONGDOWNLOADER(song['href'], chat_id)
        except:
            cantfindone(chat_id)



@Client.on_message(filters.private & filters.regex("http|https"))
async def download(client,message)
        msglink = txtfinder(msg)
        if msglink[:30]==('https://open.spotify.com/album') :
        downloader(msg,chat_id,'AL')

    elif msglink[:30]== ('https://open.spotify.com/track')  :
        try:
            SONGDOWNLOADER(msg, chat_id)
        except:
            message.sendSticker(chat_id,
                            'CAACAgQAAxkBAAIFSWBF_m3GHUtZJxQzobvD_iWxYVClAAJuAgACh4hSOhXuVi2-7-xQHgQ')
            message.reply_text(chat_id, "can't download music")

    elif msg[:33] == 'https://open.spotify.com/playlist':
        downloader(msg,chat_id,'PL')

    elif msglink[:31] == ('https://open.spotify.com/artist'):
            downloader(msg,chat_id,'AR')


print('Listening ...')


tokenurl = f'https://api.telegram.org/bot{BOT_TOKEN}'
Update = tokenurl+"/getUpdates"


def UPDATE():
    MESSAGES = requests.get(Update).json()
    return MESSAGES['result']


while 1:
    if threading.activeCount()-1 < 15:
        try:
            for message in UPDATE():
                offset = message['update_id']+1
                offset = Update+f"?offset={offset}"
                offset = requests.post(offset)
                msg = message['message']['text']
                chat_id = message['message']['from']['id']
                thread = threading.Thread(target=START,args=(msg,chat_id))
                thread.start()
        except:
            pass
