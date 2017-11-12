import tkinter as tk
import language_predictor
from sklearn.datasets import load_files
from sklearn.externals import joblib

BG_COLOR = 'black'
FONT_COLOR = 'white'
HEIGHT = 500
WIDTH = 500
ROOT = tk.Tk()
LANGUAGE_LB = tk.Label(ROOT, text='Language is:', fg=FONT_COLOR, bg=BG_COLOR, font='Avenir 14')
PREDICTION_LB = tk.Label(ROOT, text='', fg=FONT_COLOR, bg=BG_COLOR, font='Avenir 16 bold')

lang_predictor = language_predictor.LanguagePredictor()

def configure_root():
    ROOT.title('Ich connais esa lied, I credo')
    ROOT.geometry('{}x{}'.format(WIDTH, HEIGHT))
    ROOT.resizable(0, 0)
    ROOT.configure(background=BG_COLOR)

def create_ui_elements():    
    tk.Label(ROOT, text='Ich connais esa lied, I credo', fg=FONT_COLOR, bg=BG_COLOR, font='Avenir 20 bold').pack()
    author = tk.Message(ROOT, text='by Eduardo Vaca')
    author.config(fg=FONT_COLOR, bg=BG_COLOR, font='Avenir 10', width=200)
    author.pack()
    intro = tk.Message(ROOT, text='\nThis project allows you to predict the language of a song based on a Logistic Regression model')
    intro.config(fg=FONT_COLOR, bg=BG_COLOR, font='Avenir 14', width=WIDTH-20)
    intro.pack()

    tk.Label(ROOT, text='Artist', fg=FONT_COLOR, bg=BG_COLOR).pack()
    artist_entry = tk.Entry(ROOT, bd=0)
    artist_entry.pack()
    tk.Label(ROOT, text='Song', fg=FONT_COLOR, bg=BG_COLOR).pack()
    song_entry = tk.Entry(ROOT, bd=0)    
    song_entry.pack()

    tk.Label(ROOT, text='\n', fg=FONT_COLOR, bg=BG_COLOR).pack()
    tk.Button(ROOT, text='Predict', command=lambda: predict_song(artist_entry.get(), song_entry.get()), font='Avenir 18 bold', width=10).pack()    
    tk.Label(ROOT, text='\n', fg=FONT_COLOR, bg=BG_COLOR).pack()
    LANGUAGE_LB.pack()
    PREDICTION_LB.pack()

def predict_song(artist, song):
    LANGUAGE_LB.config(text='Searching song...')
    result = lang_predictor.predict_language(artist, song)
    if result[0]:        
        LANGUAGE_LB.config(text='Language is:')
        PREDICTION_LB.config(text='{}'.format(result[0]))
        print(result[1])
    else:
        LANGUAGE_LB.config(text='No song found...')
    print('A: {}, s: {}'.format(artist, song))     

def main():
    """Main program
    """
    configure_root()
    create_ui_elements()
    tk.mainloop()

if __name__ == '__main__':
    main()