from tkinter import *
from tkinter import ttk
import sqlite3

class target_shop:
    def __init__(self):
        pass
    shopname = ''
    url = ''
    rate = ''
    station = ''
    comment = ''
    smoke = ''

class find_coffee(ttk.Frame):
    index_num = 1
    display_messages = []

    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        def show_info():
            self.display_messages = list()
            search()
            if len(self.display_messages) <= 0:
                print("Nothing to show")
            response = Message(Frame2, width=500, text=self.display_messages[self.index_num])
            response.grid(row=0, column=0)
            print("This is show_info message")
            print(self.display_messages[self.index_num])

        def search():
            keyword = search_word.get()
            smoking = combo.get()
            if keyword not in '駅':
                keyword = keyword + "駅"
            print("{} : {}".format(keyword, smoking))

            con = sqlite3.connect('./shop_list.sqlite')
            cur = con.cursor()
            sql = '''
            select shop_name, rate, rocation, comment, url
            from shop_list
            where rocation like {0} and smoking like {1}'''.format('"%' + keyword +'%"', '"%' + smoking +'%"')
            cur.execute(sql)
            hits = cur.fetchall()
            for row in hits:
                hit = target_shop()
                hit.shopname = row[0]
                hit.rate = row[1]
                hit.station = row[2]
                hit.comment = row[3]
                hit.url = row[4]
                self.display_messages.append("""
                    店名 : {}
                    評価 : {}
                    場所 : {}

                    {}

                    URL : {}
                """.format(hit.shopname, hit.rate, hit.station, "コメントなし" if hit.comment=="" else hit.comment, hit.url))
                print("""------------------------------------------------------
                    店名 : {}
                    評価 : {}
                    場所 : {}

                    {}

                    URL : {}
                """.format( hit.shopname, hit.rate, hit.station, "コメントなし" if hit.comment=="" else hit.comment, hit.url))
            # print("length + "+str(len(self.display_messages)))
            con.close()

        def next_shop():
            self.index_num+= 1
            if self.index_num < len(self.display_messages)-1 :
                self.index_num = 1
            show_info()

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

        button = ttk.Button(Frame3, text='次のお店', command=next_shop)
        button.grid(row=0, column=0)

def main():
    root = Tk()
    root.title('17FI008')
    root.geometry("510x600+700+200")
    find_coffee(root)
    root.mainloop()

if __name__ == '__main__':
    main()
