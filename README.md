# Python Desktop Application
## 概要
食べログから東京都内のカフェをスクレイピングします。
格納情報は
```
店名, 詳細url, 評価, 最寄り駅, レビュー, 喫煙禁煙
```
### 必要モジュールのインストールと実行
```bash
$ pip install -r scrape.py
$ python scrape.py
```
実行後、coffeeList.csvが作成されます。
### csvファイルのデータベース化
データベースにsqliteを使用します。

sqliteコンソールに入り
```sqlite
sqlite> .mode csv
sqlite> .import ./coffeeList.csv shop_list.sqlite
```
これで sqlite で使用できる shop_list.sqlite が作成されます。

あとはGUIアプリを起動し、動作させるだけ。
### 起動
粗いですが、動きます。
```bash
$ python coffee.py
```