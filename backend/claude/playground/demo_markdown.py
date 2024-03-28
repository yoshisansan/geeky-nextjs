'''インポート関連'''
import os
import string
import random

class ContentBlock:
    def __init__(self, text, type):
        self.text = text
        self.type = type

def generate_md_file(response_content):
    # ContentBlock形式のデータからテキストを取得
    content = response_content[0].text

    # タイトル、日付、画像パス、カテゴリーを抽出
    title = content.split('\n')[1].split('"')[1]  # タイトルの抽出方法を修正
    date = content.split('\n')[2].split(' ')[1]  # 日付の抽出方法を修正
    image_path = f"/images/post/{''.join(random.choices(string.ascii_letters + string.digits, k=12))}.png"
    categories = content.split('\n')[4].replace('categories: ["', '').replace('"]', '').split('", "')  # カテゴリーの抽出方法を修正
    text = content.split('---\n\n', 1)[1]
    # mdファイルの内容を作成
    md_content = f"""---
title: "{title}"
date: {date}
image: {image_path}
categories: [{', '.join([f'"{category}"' for category in categories])}]
featured: false
draft: false
---

{text}
"""

    # ファイル名を決定
    file_name = f"{date.split('T')[0]}-{title.lower().replace(' ', '-')}.md"
    file_path = os.path.join("./", file_name)

    # ファイルを書き込む
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(md_content)

    print(f"マークダウンファイルが作成されました: {file_path}")


response_content = [ContentBlock(text='---\ntitle: "ネット空間で大規模な「猫の惑星」が出現！？無数の猫が集まり新たな惑星を形成" \ndate: 2094-04-14T10:30:00Z\nimage: /images/post/a8j2k9f0d1h5.png\ncategories: ["暮らし", "ネットで話題"]\nfeatured: false\ndraft: false\n---\n\n## ネット空間に突如現れた「猫の惑星」\n\n2094年4月14日、デジジャパンのネット空間に突如として巨大な惑星が出現しました。その正体は、なんと全て猫で構成された惑星だったのです！無数の猫たちが集まり、自らを組み合わせて直径約1万kmにも及ぶ巨大な天体を形成していました。\n\n猫たちは互いの体を絡み合わせ、まるで有機的に繋がったかのように協調して惑星を維持しています。表面には猫の毛皮が覆い尽くされ、山脈や海には猫の顔が浮かび上がっているという、何ともシュールな光景が広がっているようです。\n\n## 猫の惑星に住民が殺到！？\n\nこの突如出現した「猫の惑星」には、早くも多くのネット住民が殺到しているとのこと。猫好きにはたまらない癒しの空間として、休日の行楽地になりつつあります。\n\n惑星内部には猫たちが作り上げた街があり、訪れた住民を歓迎しているそうです。巨大なねこじゃらしのオブジェが立ち並び、空には猫じゃらしの衛星が浮かんでいるなど、ここは正に猫好きの楽園！猫と戯れながら癒しのひと時を過ごせると、口コミで評判が広がっています。\n\nただし、惑星に近づきすぎるとあまりの可愛さに悶絶して気絶してしまう恐れがあるため、にゃんこ防護服の着用が推奨されています。\n\n一体なぜ猫たちはこのような惑星を形成したのか、その目的は謎に包まれています。しかし、癒し空間として多くのネット住民に愛される存在となった「猫の惑星」。今後どのように進化していくのか目が離せません！', type='text')]
generate_md_file(response_content)
