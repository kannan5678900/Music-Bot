from spotify import DOWNLOADMP3 as SONGDOWNLOADER
import telepot
import spotify
import requests
import threading
import os
from pyrogram import Client, filters

def txtfinder(txt):
    a = txt.find("https://open.spotify.com")
    txt = txt[a:]
    return txt

def cantfind(chat.id, client):
    client.sendSticker(chat.id, 'CAACAgQAAxkBAAIBE2BLNclvKLFHC-grzNdOEXKGl6cLAALzAAMSp2oDSBk1Yo7wCGUeBA')
    client.sendMessage(chat.id, "can't find it")

def cantfindone(chat.id, client):
    client.sendSticker(chat.id, 'CAACAgQAAxkBAAIFSWBF_m3GHUtZJxQzobvD_iWxYVClAAJuAgACh4hSOhXuVi2-7-xQHgQ')
    client.sendMessage(chat.id, "can't download one of them")

def downloader(link,chat.id,type):
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
    client.sendMessage(chat.id, MESSAGE)
    for song in ITEMS:
        if PLAYLIST:
            song = song['track']

        try:
            SONGDOWNLOADER(song['href'], chat.id)
        except:
            cantfindone(chat.id)


@Client.on_message(filters.regex(pattern=".*https.* (.*)"))
async def a(client,message):
          msglink = txtfinder(message)
          if msglink[:30]==('https://open.spotify.com/album') :
              downloader(message,chat.id,'AL')

          elif msglink[:30]== ('https://open.spotify.com/track')  :
              try:
                  SONGDOWNLOADER(message, chat.id)
              except:
                  client.sendSticker(chat.id,
                                        'CAACAgQAAxkBAAIFSWBF_m3GHUtZJxQzobvD_iWxYVClAAJuAgACh4hSOhXuVi2-7-xQHgQ')
                  message.reply_text(chat.id, "can't download music")

          elif msglink[:33] == 'https://open.spotify.com/playlist':
                downloader(message,chat.id,'PL')

          elif msglink[:31] == ('https://open.spotify.com/artist'):
                downloader(message,chat.id,'AR')


print()

