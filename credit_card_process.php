<!-- credit_card_process.php -->
<?php
session_start();

// ログインしているユーザ情報を確認
if (!isset($_COOKIE['userid'])) {
    // ユーザがログインしていない場合はリダイレクトなどの処理を行う
    header("Location: login.php");
    exit;
}

// フォームからの値をそれぞれ変数に代入
$cardnumber = $_POST["card_number"];
$expiration = $_POST["expiration_date"];
$cvv = $_POST["security_code"];

// データベースへの接続情報
$host = 'localhost';
$dbname = 'ShopData';
$username = 'user1';
$password = 'passwordA1!';

$user = $_COOKIE['userid'];

$pdo = new PDO("mysql:host=".$host.";dbname=".$dbname.";charset=utf8", $username, $password);
$sql = "select id from userinfo where userid = :user;";
$stmt = $pdo->prepare($sql);
$stmt->bindParam(':user',$user,PDO::PARAM_STR);
$stmt->execute();
$result = $stmt->fetchAll();

$userid = $result[0][0];

try {
    // クレジットカード情報の登録
    $sql2 = "INSERT INTO credit_cards (userid, card_number, expiration_date, security_code) VALUES (:userid, :cardnumber, :expiration, :cvv)";
    $stmt2 = $pdo->prepare($sql2);
    $stmt2->bindParam(':userid', $userid, PDO::PARAM_INT);
    $stmt2->bindParam(':cardnumber', $cardnumber, PDO::PARAM_STR);
    $stmt2->bindParam(':expiration', $expiration, PDO::PARAM_STR);
    $stmt2->bindParam(':cvv', $cvv, PDO::PARAM_STR);
    $stmt2->execute();
    
    // 成功メッセージを表示
    echo "クレジットカード情報が正常に登録されました。";
    echo '<a href="address_registration.php">住所登録画面へ</a><br><br>';
    echo '<a href="login.php">戻る</a>';

} catch (PDOException $e) {
    // エラーメッセージを表示
    echo "クレジットカード情報の登録中にエラーが発生しました。";
    echo $e->getMessage();
    echo '<a href="credit_card.php">クレジット登録画面に戻る</a><br><br>';
    echo '<a href="touroku.php">住所登録画面へ</a>';
}
?>
