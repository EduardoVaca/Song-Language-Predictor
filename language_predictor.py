
import lyrics_fetcher
from sklearn.datasets import load_files
from sklearn.externals import joblib

class LanguagePredictor(object):
    """Class in charge of the prediction module
    """
    
    def __init__(self, dataset_name='Data/sentences', model_name='language_model.sav'):
        self.dataset = load_files(dataset_name)
        self.model = joblib.load(model_name)
        self.lyrics_f = lyrics_fetcher.LyricsFetcher()
        self.target_names = {'en': 'English', 'es': 'Spanish', 'de': 'German', 'it': 'Italian', 'fr': 'French', 'nl': 'Dutch'}

    def best_prediction(self, predictions):
        """Gets best prediction of a list of predictions
        PARAMS:
        - predictions : list of predictions
        RETURNS:
        - most repited prediction
        """
        def most_common(lst):
            """Gets most repeated element from list
            """
            return max(set(lst), key=lst.count)
        return most_common([self.target_names[self.dataset.target_names[p]] for p in predictions])

    def snippets_analyisis(self, predictions, snippets):
        """Gets string describing snippet analyisis
        PARAMS:
        - predictions : list of predictions
        - snippets : list of song snippets
        RETURNS:
        - string of analysis
        """
        return '\n'.join(['{} --> {}'.format(s, self.target_names[self.dataset.target_names[p]]) for s, p in zip(snippets, predictions)])        

    def predict_language(self, artist, song, snippets_n=5):
        """Predicts language of song
        PARAMS:
        - artist : song's artist
        - song : song's title
        - snippets_n : number of snippets to consider (default=5)
        RETURNS:
        - tuple (prediction, analysis, song title) if song found else (None)
        """
        snippets_result = self.lyrics_f.get_snippets(snippets_n, artist) if not song else self.lyrics_f.get_snippets(snippets_n, artist, song)
        if snippets_result[0]:
            predicted = self.model.predict(snippets_result[0])
            return (self.best_prediction(predicted), self.snippets_analyisis(predicted, snippets_result[0]), snippets_result[1])
        else:
            return (None)
