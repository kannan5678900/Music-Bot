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

def cantfind(chat_id, client):
    client.sendSticker(chat_id, 'CAACAgQAAxkBAAIBE2BLNclvKLFHC-grzNdOEXKGl6cLAALzAAMSp2oDSBk1Yo7wCGUeBA')
    client.sendMessage(chat_id, "can't find it")

def cantfindone(chat_id, client):
    client.sendSticker(chat_id, 'CAACAgQAAxkBAAIFSWBF_m3GHUtZJxQzobvD_iWxYVClAAJuAgACh4hSOhXuVi2-7-xQHgQ')
    client.sendMessage(chat_id, "can't download one of them")

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



@Client.on_message(filters.regex(pattern=".*https.* (.*)"))
async def a(client,message):
          msglink = txtfinder(message)
          if msglink[:30]==('https://open.spotify.com/album') :
              downloader(message,chat_id,'AL')

          elif msglink[:30]== ('https://open.spotify.com/track')  :
              try:
                  SONGDOWNLOADER(message, chat_id)
              except:
                  client.sendSticker(chat_id,
                                        'CAACAgQAAxkBAAIFSWBF_m3GHUtZJxQzobvD_iWxYVClAAJuAgACh4hSOhXuVi2-7-xQHgQ')
                  message.reply_text(chat_id, "can't download music")

          elif msglink[:33] == 'https://open.spotify.com/playlist':
                downloader(message,chat_id,'PL')

          elif msglink[:31] == ('https://open.spotify.com/artist'):
                downloader(message,chat_id,'AR')


print('Listening ...')


