import os
import requests
import json
from dotenv import load_dotenv

# .env ファイルから環境変数を読み込む
load_dotenv()
# APIキー設定
SUPABASE_ANNON_KEY = os.getenv("SUPABASE_ANNON_KEY")


async def post_image_storage(image_url, article_id):
    try:
        # リクエストヘッダーを設定
        headers = {
            "Authorization": f"Bearer {SUPABASE_ANNON_KEY}",
            "Content-Type": "application/json"
        }

        # image_urlをsupabase storageへ保存
        response = requests.post(
            'https://ajytzagixhcjqcrfunjt.supabase.co/functions/v1/post-image-storage',
            headers=headers,
            json={"image_url": image_url, "article_id": article_id},  # JSONファイルのデータを使用
            timeout=100
        )

        print("画像をストレージへ保存しました")

        # レスポンスを返す
        return response.text

    except Exception as e:
        # エラー処理をここに書く
        print(f"エラーが発生しました: {e}")
