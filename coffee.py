from tkinter import *
from tkinter import ttk

class find_coffee(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        def search():
            print('{} : {}'.format(search_word.get(), combo.get()))

        def next_review():
            pass

        def next_shop():
            pass
        """ウィジェットの作成."""
        self.grid(column=0, row=0)

        Frame1 = ttk.Frame(self)
        Frame1.grid(row=0, column=0)

        Frame2 = ttk.Frame(self)
        Frame2.grid(row=1)

        Frame3 = ttk.Frame(self)
        Frame3.grid(row=3)


        station = ttk.Label(Frame1, text='駅名')
        station.grid(row=0, column=0)

        search_word = StringVar()
        entry = ttk.Entry((Frame1), textvariable = search_word)
        entry.grid(row=0, column=1)

        tobaco = ttk.Label(Frame1, text='たばこ')
        tobaco.grid(row=0, column=2)

        combo = ttk.Combobox(Frame1, state='readonly')
        combo["values"] = ("分煙","禁煙","喫煙可")
        combo.current(0)
        combo.grid(row=0, column=3)

        button = ttk.Button(Frame1, text='検索', command=search)
        button.grid(row=0, column=4)

        response = Message(Frame2, width=500, text="""
        koko----------------------------------------------------------------------------------------------------
        """)
        response.grid(row=0, column=0)

        button = ttk.Button(Frame3, text='次のお店', command=next_shop)
        button.grid(row=0, column=0)

        button = ttk.Button(Frame3, text='次のレビュー', command=next_review)
        button.grid(row=0, column=1)

def main():
    root = Tk()
    root.title('えっち♡')
    root.geometry("510x600+700+200")
    find_coffee(root)
    root.mainloop()

if __name__ == '__main__':
    main()
