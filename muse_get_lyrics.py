import urllib2 as ul

# gets lyrics from online source
# @param song_name      string: name of the song to get the lyrics of
# @param artist         string: name of the artist performing the song
def get_lyrics(song_name, artist):
    song = ul.urlopen("http://www.azlyrics.com/lyrics/" + artist.replace(" ", "").lower() + "/" + song_name.replace(" ", "").lower() + ".html")
    lyrics = song.read()
    start_index = lyrics.find("<!-- start of lyrics -->") + len("<!-- start of lyrics -->")
    end_index = lyrics.find("<!-- end of lyrics -->")
    lyrics = lyrics[start_index:end_index].replace("<br />", "").replace('"', '')#.replace("\n"," ")
    while (lyrics.find("<i>") != -1):
        st = lyrics.find("<i>")
        end = lyrics.find("</i>")+len("</i>")
        lyrics = lyrics[:st] + lyrics[end:]
    return lyrics
    
#print get_lyrics("Demons", "Imagine Dragons")

