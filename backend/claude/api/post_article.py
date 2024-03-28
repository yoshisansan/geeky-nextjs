import os
import requests
import json
from dotenv import load_dotenv

# .env ファイルから環境変数を読み込む
load_dotenv()
# APIキー設定
SUPABASE_ANNON_KEY = os.getenv("SUPABASE_ANNON_KEY")


async def post_article(json_article_data):
    try:
        # リクエストヘッダーを設定
        headers = {
            "Authorization": f"Bearer {SUPABASE_ANNON_KEY}",
            "Content-Type": "application/json"
        }

        # POSTリクエストを送信
        response = requests.post(
            'https://ajytzagixhcjqcrfunjt.supabase.co/functions/v1/post-article',
            headers=headers,
            json=json_article_data, # JSONファイルのデータを使用
            timeout=100
        )
        
        print('記事をDBへレコード追加しました')

        # レスポンスを返す
        return response.text

    except Exception as e:
        # エラー処理をここに書く
        print(f"エラーが発生しました: {e}")

# # JSONファイルからデータを読み込む
# with open(json_file_path, 'r') as file:
#     data = json.load(file)

# 使用例
# print(post_article('../outputs/article/tetsuro.json'))

# https://oaidalleapiprodscus.blob.core.windows.net/private/org-vM99ZyYJ4JkUT8b1YqNcy5zi/user-kResN0pbcYgnfVadSIxRmAeY/img-RQfmune8TR6Whhn0Q9mamfHl.png?st=2024-03-25T11%3A53%3A57Z&se=2024-03-25T13%3A53%3A57Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-03-24T21%3A30%3A51Z&ske=2024-03-25T21%3A30%3A51Z&sks=b&skv=2021-08-06&sig=XMecS7YL1BhfyCUXoYeJ5TyMjaj8543i9NdLOh06Ru4%3D