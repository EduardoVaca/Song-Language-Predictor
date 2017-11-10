import tkinter as tk

BG_COLOR = 'black'
ROOT = tk.Tk()

def configure_root():
    ROOT.title('Ich connais esa lied, I credo')
    ROOT.geometry('500x500')
    ROOT.resizable(0, 0)
    ROOT.configure(background=BG_COLOR)

def create_ui_elements():    
    tk.Label(ROOT, text='Ich connais esa lied, I credo', fg = 'white', bg=BG_COLOR, font = "Helvetica 20 bold").pack()

def run():
    ROOT.mainloop()

def main():
    """Main program
    """
    configure_root()
    create_ui_elements()
    run()

if __name__ == '__main__':
    main()