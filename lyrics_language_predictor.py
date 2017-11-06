"""
Lyrics Language Predictor
Author: Eduardo Vaca
"""

import lyrics_fetcher
from sklearn.datasets import load_files
from sklearn.externals import joblib

dataset = load_files('Data/sentences')
loaded_model = joblib.load('language_model.sav')
while(True):
    artist = input('Artist: ')
    song = input('Song: ')
    lf = lyrics_fetcher.LyricsFetcher()
    snippets = lf.get_snippets(5, artist) if not song else lf.get_snippets(5, artist, song)
    if snippets:
        predicted = loaded_model.predict(snippets)

        for s, p in zip(snippets, predicted):
            print('The language of \"{}\" is {}'.format(s, dataset.target_names[p]))

