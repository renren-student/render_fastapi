from typing import Optional

from fastapi import FastAPI

import random  # randomライブラリを追加

from fastapi.responses import HTMLResponse #インポート

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/omikuji")
def omikuji():
    omikuji_list = [
        "大吉",
        "中吉",
        "小吉",
        "吉",
        "半吉",
        "末吉",
        "末小吉",
        "凶",
        "小凶",
        "大凶"
    ]

    return omikuji_list[random.randrange(10)]

@app.get("/index")
def index():
    html_content = """
    <html lang="ja">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>埋め込みCSSとJSのサンプルサイト</title>

        <style>
            /* ページ全体のスタイル */
            body {
                font-family: 'Helvetica Neue', Arial, sans-serif;
                line-height: 1.6;
                background-color: #f0f2f5;
                color: #333;
                text-align: center;
                padding: 20px;
            }

            /* コンテンツを囲むコンテナのスタイル */
            .container {
                max-width: 600px;
                margin: 40px auto;
                padding: 30px;
                background-color: #ffffff;
                border-radius: 12px;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            }

            /* 見出しのスタイル */
            h1 {
                color: #1a73e8;
                margin-bottom: 20px;
            }

            /* ボタンのスタイル */
            button {
                background-color: #1a73e8;
                color: white;
                border: none;
                padding: 12px 24px;
                border-radius: 8px;
                cursor: pointer;
                font-size: 16px;
                transition: background-color 0.3s ease;
            }

            /* ボタンにマウスを乗せたときのスタイル */
            button:hover {
                background-color: #1558b8;
            }

            /* メッセージ表示部分のスタイル */
            #message {
                margin-top: 25px;
                font-size: 18px;
                font-weight: bold;
                color: #d93025;
                min-height: 25px; /* メッセージが変わってもレイアウトが崩れないように高さを確保 */
            }
        </style>
        </head>
    <body>

        <div class="container">
            <h1>こんにちは！👋</h1>
            <p>下のボタンを押してみてください。</p>
            
            <button id="myButton">ここをクリック</button>
            
            <p id="message"></p>
        </div>

        <script>
            // DOM（HTML要素）の読み込みが終わってからスクリプトを実行
            document.addEventListener('DOMContentLoaded', () => {

                // IDを使ってHTML要素を取得
                const myButton = document.getElementById('myButton');
                const messageArea = document.getElementById('message');

                // ボタンがクリックされたときの処理を定義
                myButton.addEventListener('click', () => {
                    // 配列からランダムにメッセージを選ぶ
                    const messages = [
                        "ようこそ！",
                        "ボタンが押されました！🎉",
                        "良い一日を！😊",
                        "これはJavaScriptからのメッセージです。",
                        "また押してね！"
                    ];
                    const randomIndex = Math.floor(Math.random() * messages.length);
                    
                    // メッセージ表示エリアのテキストを変更
                    messageArea.textContent = messages[randomIndex];
                });

            });
        </script>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.post("/present")
async def give_present(present):
    return {"response": f"サーバです。メリークリスマス！ {present}ありがとう。お返しはキャンディーです。"}  # f文字列というPythonの機能を使っている