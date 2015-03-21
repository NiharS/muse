import urllib2 as ul
import goslate

class song_lyric(object):
    def __init__(self):
        self.begin = 0
        self.end = 0
        self.lyrics = ""
    def __str__(self):
        return "starts at " + self.begin + ", ends at " + self.end +", " + self.lyrics

def get_lrc(song_name, artist):
    song = ul.urlopen("http://lrc.awardspace.us/lrc/" + artist.replace(" ", "_") + "-" + song_name.replace(" ", "_") + ".lrc")
    for i in range(4):
        song.readline()
    mod = 0
    lyric_list = []
    for i in song.readlines():
        if (mod == 0):
            mod = 1
            s = song_lyric()
            s.begin = i[:10].replace("[","").replace("]","").replace(":","").replace(".","")
            s.lyrics = i[10:]
            lyric_list.append(s)
        else:
            mod = 0
            lyric_list[-1].end = i[:10].replace("[","").replace("]","").replace(":","").replace(".","")
    return lyric_list
'''   
ll = get_lrc("Battlefield", "Jordin Sparks")
for i in ll:
    print i
'''

def get_lyrics_and_times(song_name, artist):
    lrc = ul.urlopen("http://lrc.awardspace.us/lrc/" + artist.replace(" ", "_") + "-" + song_name.replace(" ", "_") + ".lrc")
    has_lyric = True
    lyrics = ''
    time_intervals = []

    for line in lrc.readlines():
        if line == "\r\n":
            continue
        elif line[1:3] in ["ti","ar","la"]:
            continue
        if has_lyric:
            lyrics += line[10:]
            time_intervals.append([line[:10].replace("[","").replace("]","")])
        else:
            time_intervals[-1].append(line[:10].replace("[","").replace("]",""))
        has_lyric = not has_lyric

    return lyrics, time_intervals

def get_translated_lrc(song_name, artist, language):
    lyrics, time_intervals = get_lyrics_and_times(song_name, artist)
    print "got lyrics"
    gs = goslate.Goslate()
    print "initialized gs"
    return gs.translate(lyrics, language).encode('latin-1'), time_intervals

#print get_lyrics_and_times("Love Story", "Taylor Swift")
#print get_translated_lrc("Love Story", "Taylor Swift", "es")
