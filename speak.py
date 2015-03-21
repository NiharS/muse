import urllib2 as ul
import urllib
from urllib import urlretrieve as ur
import pyttsx
import time
from muse_get_lrc import *
from pygame import mixer


def get_time_diff(start, end):
    s = int(start[0:2])*60 + int(start[2:4]) + float(start[4:])/100
    e = int(end[0:2])*60 + int(end[2:4]) + float(end[4:])/100
    return e-s
    
def get_time_diff_unedited(start, end):
    return get_time_diff(start[0:2]+start[3:5]+start[6:8], end[0:2]+end[3:5]+end[6:8])

def sing_song(song_name, artist):
    engine = pyttsx.init()
    engine.setProperty('rate', engine.getProperty('rate')-100)

    lyric_list = get_lrc(song_name, artist)
    for i in xrange(len(lyric_list) - 1):
        length = get_time_diff(lyric_list[i].begin, lyric_list[i].end)
        diff = get_time_diff(lyric_list[i].begin, lyric_list[i+1].begin)
        start = time.time()
        print "length:", length
        print "diff:", diff
        words = lyric_list[i].lyrics
        
        engine.setProperty('rate', int(len(words.split())*60/length))
        engine.say(words)
        engine.runAndWait()
        td = time.time() - start
        if length < diff:
            pass #time.sleep(diff-length)
    engine.say(lyric_list[-1].lyrics)
    engine.runAndWait()

#sing_song("Battlefield", "Jordin Sparks")

def sing_translated(song_name, artist, language):
    print "start"
    engine = pyttsx.init()
    lyrics, times = get_translated_lrc(song_name, artist, language)
    lyrics = lyrics.split("\r\n")
    #text = lyrics.replace("\r\n", " ")
    raw_input()
    text = "yo soy una persona".replace(" ", "%20")
    #outfile = open("C:/Users/Nihar/Documents/yelp_dataset_challenge_academic_dataset/test.mp3", "w")
    asdf=0
    for text in lyrics:
        outfile = open("C:/Users/Nihar/Documents/yelp_dataset_challenge_academic_dataset/muse_music/test" + str(asdf) + ".mp3", "w")
        asdf += 1
        text = text.replace(" ", "%20")
        url = "http://translate.google.com/translate_tts?ie=UTF-8&q=" + text + "&tl=" + language
        #testfile = urllib.URLopener()
        #testfile.retrieve("http://translate.google.com/translate_tts?ie=UTF-8&q=" + text + "&tl=es", "song.mp3")
        req = ul.Request(url, headers={'User-Agent' : "Magic Browser"}) 
        con = ul.urlopen( req )
    
        #mpeg = ul.urlopen("http://translate.google.com/translate_tts?ie=UTF-8&q="+ text +"&tl="+language)
        data = con.read()
        con.close()

        outfile.write(data)
        outfile.close()
    return
    if mixer.get_init():
        mixer.quit()
    mixer.init(channels=1, buffer=2048)
    mixer.music.load("C:/Users/Nihar/Documents/yelp_dataset_challenge_academic_dataset/test.mp3")
    mixer.music.play()
    time.sleep(40)
    mixer.quit()
    '''lyrics = lyrics.split("\n")
    #lyrics = get_translated_lrc(song_name, artist, language).split("\n")
    for i in range(len(lyrics)-1):
        print lyrics[i]
        length = get_time_diff_unedited(times[i][0], times[i][1])
        diff = get_time_diff_unedited(times[i][0], times[i][1])
        start = time.time()
        words = lyrics[i]
        engine.setProperty('rate', int(len(words.split())*60/length))
        engine.say(words)
        engine.runAndWait()
    engine.say(lyrics[-1])
    engine.runAndWait()'''
    
sing_translated("Love Story", "Taylor Swift", "es")