# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import urllib2
import time
import os
import sys
import re

import subprocess
import dbus



def getlyrics(songname):
    error = "Error:  No lyrics Found."
    artist = ""
    song = ""
    url = ""
    if songname.count(" - ") == 1:
        artist, song = songname.rsplit(" - ", 1)
    if songname.count(" - ") == 2:
        artist, song, garbage = songname.rsplit(" - ", 2)
    if " / " in song:
        song, garbage = song.rsplit(" / ", 1)
    song = re.sub(' \(.*?\)', '', song, flags=re.DOTALL)


    
    def lyrics_musixmatch(artist, song):
	    url = ""
	    try:
	        searchurl = "https://www.musixmatch.com/search/%s %s" % (artist, song)

	        searchurl = searchurl.replace(" ","%20")

	        searchresult = urllib2.urlopen(searchurl)
	        soup = BeautifulSoup(searchresult, 'html.parser')
	        li = soup.find('a', {"class": "title"})['href']
	        link = "https://www.musixmatch.com" + li 
	        url = link 
	        lyricspage = urllib2.urlopen(url)

	        soup = BeautifulSoup(lyricspage, 'html.parser')
	        lyrics = soup.text.split('"body":"')[1].split('","language"')[0]
	        lyrics = lyrics.replace("\\n", "\n")
	        lyrics = lyrics.replace("\\", "")
	    
	    except Exception:
	        lyrics = error
	    return lyrics



    lyrics = lyrics_musixmatch(artist, song)

    lyrics = lyrics.replace("&amp;", "&")
    lyrics = lyrics.replace("`", "'")
    lyrics = lyrics.strip()
    return lyrics




def getwindowtitle():
    
    windowname = ''
    session = dbus.SessionBus()
    spotifydbus = session.get_object("org.mpris.MediaPlayer2.spotify", "/org/mpris/MediaPlayer2")
    spotifyinterface = dbus.Interface(spotifydbus, "org.freedesktop.DBus.Properties")
    metadata = spotifyinterface.Get("org.mpris.MediaPlayer2.Player", "Metadata")
    try:
        command = "xwininfo -tree -root"
        windows = subprocess.check_output(["/bin/bash", "-c", command]).decode("utf-8")
        spotify = ''
        for line in windows.splitlines():
            if '("spotify" "Spotify")' in line:
                if " - " in line:
                    spotify = line
                    break
        if spotify == '':
            windowname = 'Spotify'
    except Exception:
        pass
    if windowname != 'Spotify':
        windowname = "%s - %s" %(metadata['xesam:artist'][0], metadata['xesam:title'])


    if "Spotify - " in windowname:
        windowname = windowname.strip("Spotify - ")
    return(windowname)



def main():
    os.system("clear")
 
    oldsongname = ""

    while True:
        songname = getwindowtitle()
        #print songname
        if oldsongname != songname:
            if songname != "Spotify":
                oldsongname = songname
                #os.system("clear")

                print(songname+"\n")
                lyrics = getlyrics(songname)
                print(lyrics+"\n")
                time.sleep(2)
        time.sleep(1)




if __name__ == '__main__':
    main()