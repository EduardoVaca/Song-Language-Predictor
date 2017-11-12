"""
Class to fetch lyrics.
Author: Eduardo Vaca
Using library PyLyrics from:
https://github.com/geekpradd/PyLyrics
"""
import random
from PyLyrics import *


class LyricsFetcher(object):
    """Class that is responsible of fetching lyrics
    Manages all the logic in case no lyrics are found
    """

    def get_lyrics(self, artist, song):
        """Gets the lyrics of a song
        PARAMS:
        - artist : artist of the song
        - song : song title
        RETURNS:
        - tuple, (True of lyrics found, lyrics)
        """
        try:
            lyrics = PyLyrics.getLyrics(artist, song)
            return (True, lyrics)
        except:
            return (False, 'Cant find lyrics')

    def get_random_song_from_artist(self, artist):
        """Gets a random song title from an artis
        PARAMS:
        - artist : artist to get the random song of
        RETURNS:
        - tuple, (True if song found, song title)
        """
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

    def get_snippets(self, n_snippets, artist, song=None):
        """Gets n snippets from the song lyrics
        PARAMS:
        - artist : artist of the song
        - song : song title
        - n_snippets : number of snippets to get
        RETURNS:
        - tuple, (list of snippets, song title)
        """
        if not song:
            song = self.get_random_song_from_artist(artist)[1]
        result = self.get_lyrics(artist, song)
        return (self.song_snippets(result[1], n_snippets) if result[0] else [], song)

    def song_snippets(self, lyrics, n_snippets):
        """Gets snippets from the song
        PARAMS:
        - lyrics : lyrics of song
        - n_snippets: number of snippets to get
        RETURNS:
        - list of n snippets
        """
        snippets = [s for s in lyrics.split('\n') if s != '']
        random.shuffle(snippets)
        return snippets[:n_snippets]
