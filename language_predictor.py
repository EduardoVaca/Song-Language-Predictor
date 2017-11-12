
import lyrics_fetcher
from sklearn.datasets import load_files
from sklearn.externals import joblib

class LanguagePredictor(object):
    
    def __init__(self, dataset_name='Data/sentences', model_name='language_model.sav'):
        self.dataset = load_files(dataset_name)
        self.model = joblib.load(model_name)
        self.lyrics_f = lyrics_fetcher.LyricsFetcher()
        self.target_names = {'en': 'English', 'es': 'Spanish', 'de': 'German', 'it': 'Italian', 'fr': 'French', 'nl': 'Dutch'}

    def best_prediction(self, predictions):
        def most_common(lst):
            return max(set(lst), key=lst.count)
        return most_common([self.target_names[self.dataset.target_names[p]] for p in predictions])

    def snippets_analyisis(self, predictions, snippets):
        return '\n'.join(['{} --> {}'.format(s, self.target_names[self.dataset.target_names[p]]) for s, p in zip(snippets, predictions)])        

    def predict_language(self, artist, song, snippets_n=5):
        snippets = self.lyrics_f.get_snippets(snippets_n, artist) if not song else self.lyrics_f.get_snippets(snippets_n, artist, song)
        if snippets:
            predicted = self.model.predict(snippets)
            return (self.best_prediction(predicted), self.snippets_analyisis(predicted, snippets))
        else:
            return (None, [])
