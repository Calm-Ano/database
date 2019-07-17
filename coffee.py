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
        店名 : ブリコラージュ ブレッド アンド カンパニー ベーカリー

まずはﾊﾟﾝ屋さんとしてﾃｲｽﾃｨﾝｸﾞする予定だったのに、昨日に比べ過ごしやすい気温でかつﾃﾗｽが空いてるように見えたので、ついｶﾌｪの方へ…入店時点でお一人様には肩身の狭いﾎﾟﾘｼｰかどうか判別できたのに着席してから「やっぱり止めます」は大人げないと、ｶｳﾝﾀｰでｶﾞﾏﾝしたのが失敗2。そしてﾀﾞﾒ押しが、雑誌で見かけた時にｵｰﾌﾟﾝｻﾝﾄﾞは死ぬほど食べづらそうだと思ったのに「ｱｽﾊﾟﾗ」の文字に惹かれてうっかり。案の定、ようやく出てきたｵｰﾌﾟﾝｻﾝﾄﾞは、ｶﾝﾊﾟの上にｱｽﾊﾟﾗがｺﾞﾛｺﾞﾛ…もちろんｿﾃｰしたｷﾉｺやてっぺんに鎮座したﾌﾗｲﾄﾞｴｯｸﾞとは一緒に頬張れない。でもｺｺまでは、ある意味わたしの好みではない、というだけで万人と異なる可能性もあるのだが、肝心のｷﾉｺのｿﾃｰやﾌﾗｲﾄﾞｴｯｸﾞになんら味付けが施されていないように感じたのは残念。ｸﾘｰﾑﾁｰｽﾞだろうか、ｶﾝﾊﾟの下に塗られていた酸味を感じるｸﾘｰﾑ、またｱｽﾊﾟﾗは“素材の”旨味を感じられた、以上。ただ最も残念なのがｻｰﾋﾞｽで、一人なのでｶｳﾝﾀｰ、これは仕方がないとしても、誰もいないｶｳﾝﾀｰに一人着席したので隣にﾊﾞｯｸﾞを置いたら、後から来た女子ｸﾞﾙｰﾌﾟのためにｶｳﾝﾀｰ下のﾌｯｸに吊るすよう言われ、その直後、女子ｸﾞﾙｰﾌﾟはﾃｰﾌﾞﾙ席に案内し直したにも拘らずｴｸｽｷｭｰｽﾞなし。飲み物のｺｰﾋｰが最初に来てしまいｻﾗﾀﾞを食べる頃には冷めてしまったことも残念。そしてｸﾘｰﾑのｻｰﾋﾞｽもなし。念のためﾊﾟﾝを購入してみると悪くない。ただ同じくｻｰﾋﾞｽは残念。他のお店も同様かも知れないが、ｱﾀﾞﾙﾄには肩身が狭く共感もできない品質のお店が多くてﾂﾏﾗﾅｲ。
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
