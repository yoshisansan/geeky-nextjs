## 概要
Google Crowd FunctionとしてCRONで定期的に呼び出すためのファイル。このファイルをアップロードしている。

## 始め方
1. 立ち上げ

```
pip install -r requirements.txt
```
2. 各種envファイルにキーを設定

3. 記事を生成

python main.py
```


## メモ旧
playgroundのcreate_article_backup.pyあたりのやつ
```
curl -X POST http://127.0.0.1:8000/generate-news -H "Content-Type: application/json" -d '{"key": "あああ"}'
```