import os
import openai

from dotenv import load_dotenv
from fastapi import HTTPException

# .env ファイルから環境変数を読み込む
load_dotenv()
DALLE2_KEY = os.getenv("DALLE2_KEY")
openai.api_key = DALLE2_KEY


system_prompt = """
下の記事を最初にコンテンツポリシーに引っかからないように内容を変換してください。それから内容に合う画像を生成して。日本の漫画風でコミカルにしてください。ポリシー違反しないよう記事内で著作権に関わる名前があれば関連した画像を生成しないように可能な限り注意を払ってください。
"""

async def create_thumbnail(json_article):
    try:
        prompt = f"""
        {system_prompt}
        {json_article}
        """

        image_url = await generate_image_with_dalle3(prompt)
        print(f'サムネイル画像URLを生成しました：{image_url}')
        return image_url
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) from e



async def generate_image_with_dalle3(prompt):
    # Official API Reference: https://beta.openai.com/docs/api-reference/images
    response = openai.images.generate(
      model="dall-e-3", # dall-e-3 0.08ドル/回
      prompt=prompt,
      size="1792x1024",
      quality="standard",
      n=1,
    )
    image_url = response.data[0].url
    return image_url

# image_url = generate_image_with_dalle2(prompt)
# print(image_url)



# https://oaidalleapiprodscus.blob.core.windows.net/private/org-vM99ZyYJ4JkUT8b1YqNcy5zi/user-kResN0pbcYgnfVadSIxRmAeY/img-wciJudLd1PMiAsY0Njb6hXVM.png?st=2024-03-24T12%3A54%3A31Z&se=2024-03-24T14%3A54%3A31Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-03-23T18%3A48%3A59Z&ske=2024-03-24T18%3A48%3A59Z&sks=b&skv=2021-08-06&sig=MmNheWPaifzvxYnFsfco4CPQm5yx/eV7rPOMaES8ZfM%3D