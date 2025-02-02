#!/usr/bin/python3
import cgi
import MySQLdb
import os
from http import cookies
import random, string

cookie = cookies.SimpleCookie(os.environ.get('HTTP_COOKIE',''))

try:

	userid = cookie["userid"].value+"さん"

except KeyError:

	userid = 'please_login'

form = cgi.FieldStorage()
word=form.getfirst("search")

connection = MySQLdb.connect(

    host='localhost',

    user='user1',

    passwd='passwordA1!',

    db='ShopData',

    charset='utf8'

)

cursor = connection.cursor()

cursor.execute("select * from Goods")

rows = cursor.fetchall()
goods_list = str()
goods_name = str()
for row in rows:
    good = "<a href='"+row[3]+"'><img src='./Goods_Photo/"+row[1]+"' width='180'height='150' alt='検索'/></a>"
    if row[2]==word:
        goods_list+=good
        goods_name+=row[2]
len_goodslist=len(goods_list)
connection.close()
print("Content-Type: text/html\n")
if userid == "please_login":
    htmlText = '''
    <!DOCTYPE html>

    <html lang="ja">
    <head>
    <meta charset="utf-8">
    <title>ComBuy</title>
    <link rel="stylesheet" type="text/css" href="goods.css"/>
    <!--
    h1 { color:green }
    strong { color: blue; font-size: large }
    em { font-style: Italic }
    -->
    
    </style>
    
    </head>
    
    <body>
    <!-- ボタンの宛先を指定するjavascript -->
    <script>
    function multipleaction(u){
    var f = document.querySelector("form");
    var a = f.setAttribute("action", u);
    document.querySelector("form").submit();
    }
    </script>

    <form id="mainform">
    <div class="logo"><button type="submit" onclick="multipleaction('./top_page.cgi')" alt="topに戻る"><img src= "./button/ComBuy.png" width="320"height="100"></button></div>
    <h1>%s</h1>
    <input type="search" name="search" placeholder="キーワードを入力">
    <button type="submit" onclick="multipleaction('./top_page.cgi')"><img src="./button/search_button.png" width="50"height="30" alt="検索" /></button> 
    <div class="btn"><button type="button" onclick="multipleaction('./login.php')"><img src="./button/login.png" width="70"height="70" alt="送信" /></button>
    <button type="button" onclick="multipleaction('./register.php')"><img src="./button/sign_up.png" width="70"height="70" alt="新規登録" /></button>
    <button type="button" onclick="multipleaction('./rireki.cgi')"><img src="./button/rireki.png" width="70"height="70" alt="購入履歴" /></button>
    <button type="button" onclick="multipleaction('./Exhibit.cgi')"><img src="./button/syuppin.png" width="70"height="70" alt="出品する" /></button>
    <button type="button" onclick="multipleaction('./cart.cgi')"><img src="./button/cart.png" width="70"height="70" alt="カート" /></button></div>
    </form>
    </body>
    
    </html>
    '''%(userid)
else:
    htmlText = '''
    <!DOCTYPE html>

    <html lang="ja">
    <head>
    <meta charset="utf-8">
    <title>ComBuy</title>
    <link rel="stylesheet" type="text/css" href="goods.css"/>
    <!--
    h1 { color:green }
    strong { color: blue; font-size: large }
    em { font-style: Italic }
    -->
    
    </style>
    </head>
    
    <body>
    <!-- ボタンの宛先を指定するjavascript -->
    <script>
    function multipleaction(u){
    var f = document.querySelector("form");
    var a = f.setAttribute("action", u);
    document.querySelector("form").submit();
    }
    </script>

    <form id="mainform">
    <div class="logo"><button type="submit" onclick="multipleaction('./top_page.cgi')" alt="topに戻る"><img src= "./button/ComBuy.png" width="320"height="100"></button></div>
    <h1>%s</h1>
    <input type="search" name="search" placeholder="キーワードを入力">
    <button type="submit" onclick="multipleaction('./top_page.cgi')"><img src="./button/search_button.png" width="50"height="30" alt="検索" /></button> 
    <div class="btn"><button type="button" onclick="multipleaction('./rireki.cgi')"><img src="./button/rireki.png" width="70"height="70" alt="購入履歴" /></button>
    <button type="button" onclick="multipleaction('./Exhibit.cgi')"><img src="./button/syuppin.png" width="70"height="70" alt="出品する" /></button>
    <button type="button" onclick="multipleaction('./cart.cgi')"><img src="./button/cart.png" width="70"height="70" alt="カート" /></button></div>
    </form>
    </body>
    
    </html>
    '''%(userid)

print(htmlText.encode("utf-8", 'ignore').decode('utf-8'))

form = cgi.FieldStorage()

htmlText = '''
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<title>Python Form</title>
</head>
<body>
%s
%s
</body>
</html>
    '''%(goods_list,goods_name)
print(htmlText.encode("utf-8", 'ignore').decode('utf-8'))
