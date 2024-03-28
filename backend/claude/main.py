import asyncio
from api.create_article import generate_news
from api.create_thumb import create_thumbnail
from api.post_article import post_article
from api.post_image_storage import post_image_storage

# post_article 関数を使用する例
# json_file_path = './outputs/article/ramen.json'

# image_url = 'https://oaidalleapiprodscus.blob.core.windows.net/private/org-vM99ZyYJ4JkUT8b1YqNcy5zi/user-kResN0pbcYgnfVadSIxRmAeY/img-NN04Y1N50HNTLL7dtUevCBi0.png?st=2024-03-27T23%3A11%3A32Z&se=2024-03-28T01%3A11%3A32Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-03-27T17%3A44%3A49Z&ske=2024-03-28T17%3A44%3A49Z&sks=b&skv=2021-08-06&sig=bZ0rnk3HVVgiBXskTL50uD/JgwwgzlEAJZ/1zioB/po%3D'
# article_id = 'ba0a2504-e91b-4531-8d58-14bb25215354'

json_article = {'title': 'ネオ日本のマツコ、また謎バウンド！「ニューラリンクポッドにバグか」とファン騒然', 'categories': "['エンタメ', '芸能']", 'featured': False, 'draft': False, 'contents': '<p>人気芸能人のマツコ・デラックスが、またしても電脳空間上で奇妙なバウンドを繰り返したことで話題になっている。</p><p>事の発端は、あるファンがオンバーチャル空間内でマツコと遭遇した際のこと。そのファンによると、マツコはいきなり宙高くジャンプし、そのまま何度もバウンドを繰り返し始めたという。「まるでゴム毬のようだった」と目撃者は証言している。</p><h2>「ニューラリンクポッドにバグか」の声も</h2><p>オンバーチャル空間での物理法則を無視したマツコの挙動に、ファンの間では「ニューラリンクポッドにバグが発生しているのでは」との憶測も飛び交っている。</p><p>一方、マツコの所属事務所は「本人の意図的な行動」とコメント。バグではなく、マツコお得意のエンターテイメント精神の発露だったようだ。</p><h2>バウンドしながら熱弁するマツコに注目集まる</h2><p>その後もマツコは、バウンドを繰り返しながら持論を展開。オンバーチャル空間ならではの表現方法に、多くの人が注目を集めている。</p><p>「重力に囚われない発想が斬新」「マツコ節全開だね」と、ファンからは好意的な声が上がっている。</p><p>2094年のエイジレス社会を象徴するような出来事に、改めてマツコ・デラックスの存在感の大きさを感じずにはいられない。</p>', 'article_id': '30f30178-2f3a-4339-aec0-a1b4bbf723e9'}

async def main():
    try:
        json_article = await generate_news()
        image_url = await create_thumbnail(json_article)
        await post_image_storage(image_url, json_article['article_id']) # uuid生成したarticle_idをsupabase storage上のサムネイル名として保存する
        await post_article(json_article)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    asyncio.run(main())

