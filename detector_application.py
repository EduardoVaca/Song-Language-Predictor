import tkinter as tk

BG_COLOR = 'black'
FONT_COLOR = 'white'
HEIGHT = 500
WIDTH = 500
ROOT = tk.Tk()

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
    tk.Button(ROOT, text='Predict', command=predict_song, font='Avenir 18 bold', width=10).pack()
    tk.Label(ROOT, text='\n', fg=FONT_COLOR, bg=BG_COLOR).pack()
    tk.Button(ROOT, text='Reset', command=predict_song, font='Avenir 12').pack()

    tk.mainloop( )

def predict_song():
    pass

def reset():
    pass

def main():
    """Main program
    """
    configure_root()
    create_ui_elements()

if __name__ == '__main__':
    main()