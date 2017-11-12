import time
import tkinter as tk
import language_predictor
from sklearn.datasets import load_files
from sklearn.externals import joblib

BG_COLOR = 'black'
FONT_COLOR = 'white'
HEIGHT = 700
WIDTH = 600
ROOT = tk.Tk()
LANGUAGE_LB = tk.Label(ROOT, text='Language is:', fg=FONT_COLOR, bg=BG_COLOR, font='Avenir 14')
PREDICTION_LB = tk.Label(ROOT, text='', fg=FONT_COLOR, bg=BG_COLOR, font='Avenir 22 bold')
ANALYSIS_LB = tk.Message(ROOT, text='', fg=FONT_COLOR, bg=BG_COLOR, font='Avenir 14', width=WIDTH-20)
# Predictor constant
LANG_PREDICTOR = language_predictor.LanguagePredictor()
LANG_COLORS = {
    'English': 'red1',
    'Dutch': 'DarkOrange1',
    'French': 'deepskyblue',
    'Italian': 'SpringGreen2',
    'Spanish': 'darkorchid1',
    'German': 'yellow'
}

def configure_root():
    """Configures UI Root
    """
    ROOT.title('Ich connais esa lied, I credo')
    ROOT.geometry('{}x{}'.format(WIDTH, HEIGHT))
    ROOT.resizable(0, 0)
    ROOT.configure(background=BG_COLOR)

def create_ui_elements(): 
    """Creates UI elements
    """
    # Labels
    tk.Label(ROOT, text='Ich connais esa lied, I credo', fg=FONT_COLOR, bg=BG_COLOR, font='Avenir 20 bold').pack()
    author = tk.Message(ROOT, text='by Eduardo Vaca')
    author.config(fg=FONT_COLOR, bg=BG_COLOR, font='Avenir 10', width=200)
    author.pack()
    intro = tk.Message(ROOT, text='\nThis project allows you to predict the language of a song based on a Logistic Regression model. Enter the artist and song info below, if you leave the song entry empty then a random song will be selected for the artist and then be predicted.')
    intro.config(fg=FONT_COLOR, bg=BG_COLOR, font='Avenir 14', width=WIDTH-20)
    intro.pack()
    # Entries
    tk.Label(ROOT, text='Artist', fg=FONT_COLOR, bg=BG_COLOR).pack()
    artist_entry = tk.Entry(ROOT, bd=0)
    artist_entry.pack()
    tk.Label(ROOT, text='Song', fg=FONT_COLOR, bg=BG_COLOR).pack()
    song_entry = tk.Entry(ROOT, bd=0)
    song_entry.pack()
    # Checkbox
    tk.Label(ROOT, text='\n', fg=FONT_COLOR, bg=BG_COLOR).pack()
    show_analyisis = tk.IntVar()
    tk.Checkbutton(ROOT, text="Show snippets", variable=show_analyisis).pack()
    # Predict button
    tk.Label(ROOT, text='\n', fg=FONT_COLOR, bg=BG_COLOR).pack()
    tk.Button(ROOT, text='Predict', command=lambda: predict_song(artist_entry.get(), song_entry.get(), song_entry, show_analyisis.get()), font='Avenir 18 bold', width=10).pack()
    tk.Label(ROOT, text='\n', fg=FONT_COLOR, bg=BG_COLOR).pack()
    LANGUAGE_LB.pack()
    PREDICTION_LB.pack()
    ANALYSIS_LB.pack()

def predict_song(artist, song, song_entry, show_snippets):
    """Using LanguagePredictor, predicts a song and update UI
    PARAMS:
    - artist : song's artist
    - song : song's title
    - song_entry : entry for song
    - show_snippets : bool for showing snippets
    """
    LANGUAGE_LB.config(text='Searching song...')
    result = LANG_PREDICTOR.predict_language(artist, song)
    if result:
        LANGUAGE_LB.config(text='Language is:')
        PREDICTION_LB.config(text=result[0], fg=LANG_COLORS.get(result[0], FONT_COLOR))
        ANALYSIS_LB.config(text=result[1] if show_snippets else '')
        if not song:
            song_entry.insert(0, result[2])
    else:
        LANGUAGE_LB.config(text='No song found...')
        PREDICTION_LB.config(text='')
        ANALYSIS_LB.config(text='')

def main():
    """Main program
    """
    configure_root()
    create_ui_elements()
    tk.mainloop()

if __name__ == '__main__':
    main()
