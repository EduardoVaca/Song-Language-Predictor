"""
Class to fetch lyrics.
Author: Eduardo Vaca
Using library PyLyrics from:
https://github.com/geekpradd/PyLyrics
"""
import random
from PyLyrics import *


class LyricsFetcher(object):

    def get_lyrics(self, artist, song):
        try:
            lyrics = PyLyrics.getLyrics(artist, song)
            return (True, lyrics)
        except:
            return (False, 'Cant find lyrics')

    def get_random_song_from_artist(self, artist):
        try:
            albums = PyLyrics.getAlbums(singer=artist)
            if not albums:
                return (False, 'No albums')
            songs = random.choice(albums).tracks()
            if not songs:
                return (False, 'No songs')
            return (True, random.choice(songs).name)
        except:
            return (False, 'No artist')

lf = LyricsFetcher()
artist = 'Brainpower'
result = lf.get_random_song_from_artist(artist)
if result[0]:
    print('*************{}*************'.format(result[1]))
    print(lf.get_lyrics(artist, result[1]))