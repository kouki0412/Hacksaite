<!-- credit_card.php -->
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>クレジットカード登録</title>
    <h1><img src= "./button/ComBuy.png" width="320"height="100"></h1>
    <style>
        body {
            background:linear-gradient(180deg, #000000 0%, #000000 24.5%, #fffaf0 24.5%, #fffaf0 100%);
            background-repeat:no-repeat;
            font-family: Arial, sans-serif;
            background-color:#fffaf0;
        }

        .container {
            max-width: 400px;
            margin: 0 auto;
            padding: 40px;
            background-color: #fff;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }

        h1 {
            text-align: center;
            color: #333;
            margin-top: 0;
        }

        .form-group {
            margin-bottom: 20px;
        }

        .form-group label {
            display: block;
            margin-bottom: 5px;
            color: #555;
        }

        .form-group input[type="text"],
        .form-group input[type="number"] {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }

        .form-group input[type="submit"] {
            width: 100%;
            padding: 10px;
            background-color: #4CAF50;
            border: none;
            color: white;
            border-radius: 5px;
            cursor: pointer;
        }

        .back-link {
            display: block;
            text-align: center;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>住所登録</h1>
        <form action="address_process.php" method="post">
            <input type="hidden" name="userid" value="<?php echo $_COOKIE['userid']; ?>">
            <div class="form-group">
                <label for="yuubinbangou">郵便番号</label>
                <input type="text" id="yuubinbangou" name="yuubinbangou" required>
            </div>
            <div class="form-group">
                <label for="todouhuken">都道府県名</label>
                <input type="text" id="todouhuken" name="todouhuken" required>
            </div>
            <div class="form-group">
                <label for="sikutyouson">市区町村</label>
                <input type="text" id="sikutyouson" name="sikutyouson" required>
	    </div>
            <div class="form-group">
                <label for="banchi">番地</label>
                <input type="text" id="banchi" name="banchi" required>
            </div>
            <input type="submit" value="登録">
        </form>
        <a class="back-link" href="top_page.cgi">トップへ戻る</a>
    </div>
</body>
</html>
