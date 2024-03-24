## 始め方
立ち上げ

```
uvicorn create_article:app --reload
```

apiを叩いて記事を生成

```
curl -X POST http://127.0.0.1:8000/generate-news -H "Content-Type: application/json" -d '{"key": "あああ"}'
```