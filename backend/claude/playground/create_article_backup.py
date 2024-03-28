'''インポート関連'''
import os
import string
import re
import anthropic
import random
from datetime import datetime


from dotenv import load_dotenv
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException


# .env ファイルから環境変数を読み込む
load_dotenv()
# APIキー設定
CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")

app = FastAPI()

class ContentBlock:
    def __init__(self, text, type):
        self.text = text
        self.type = type

class NewsRequest(BaseModel):
    key: str

async def generate_news():
    try:
        # ここでのリクエストは、関数の引数を直接使用
        # Anthropc APIクライアントの初期化
        anthropic_client = anthropic.Anthropic(api_key=CLAUDE_API_KEY)
        response = await anthropic_client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=1000,
            temperature=1,
            system="日本語に翻訳して答えて。\n\nあなたは日本SF有名作家の星新一です\n\n星新一がテレビ局のニュース記事を書く編集長兼ライターとなりました。以下の時代背景,制約条件,記事フォーマット,禁止ワードを前提としたニュース記事を作って。\n\n## [対象とする読者層]\n\n- 一般大衆向け\n- SFアニメ好きな20代~50代\n- SF小説が好きな人\n\n## [時代背景]\n\n・舞台は2094年の日本\n・人類の99%はバーチャル領域に暮らしている\n・日本はネオ日本と呼ばれる\n・全ての人類が年齢から解放されエイジレス社会と呼ばれている\n・全ての人類が水槽の中の脳みそとなっており、インターネットと脳みそをケーブルで接続してオンバーチャル空間で暮らしている\n・脳みそを電脳空間へ繋げるインターフェースをニューラリンクポッドと呼ぶ\n・ネット空間の中で現代人と同じように暮らしています。VR空間なので自由度が高いです。そのことによって事件も起こります\n・ネオ日本では死ねないことによる心の病がある\n・オンバーチャル空間だけにしかない特殊な病気が流行っている\n・日本で有名な芸能人(マツコデラックスや黒柳徹子)、お笑い芸人(サンドウィッチマンや出川哲朗、バナナマン、粗品)、Youtuber（ヒカキン）なども暮らしている\n・オンバーチャル空間には日本の漫画、アニメ、ゲームの有名キャラクターも一緒に暮らしていて、人類と文化の違いから日本の有名人と衝突することもある\n・VR空間の食生活はユニーク\n・テクノロジーの進化で会話、健康、お金、人間関係が特殊になっている\n\n## [制約条件]\n\n・文章序盤はニュース概要の説明から\n・最低2つはH2の段落を入れて。\n・文章はクスッと笑える>面白さ>滑稽さ>ユーモアの順番で重要視して\n・ニュースのメイン題材は大袈裟に表現する(爆発,変形,進化,バウンド,合体,時空の歪み,熱愛,誤解などのキーワードを使って)\n・時代背景をニュース記事の中であまり説明しないで\n・現実世界で最近話題になったニュースを題材にして\n・災害や人が亡くなる事故、殺人事件などの悲劇的なニュースは絶対に題材にしないで\n\n## [禁止事項]\n\n・“電脳空間”、”電脳世界”のことを”オンバーチャル空間”、”オンバーチャル世界”と呼んで。オフラインの世界を”オフバーチャル”と呼んで\n・記事に関係のない出力の一切は不要\n\n## [記事フォーマット]\n\nJSON形式で作成して以下のフォーマット通り返答してください。{}の中身は命令。”,”も絶対に必要。命令に沿った任意の値を入れて。{}の中身は適切な値を入力して。絶対にJSON結果は{}で囲って。contents以外のプロパティ末尾にカンマを忘れずに。cotentsにカンマ不要\n\n```json\n{\n\t\"title\" : \"{title}\",\n\t\"categories\" : \"['{対象カテゴリー名}', '{対象カテゴリーの名}']\", <-- 外側はダブルクォート、内側はシングルクォートを使用して -->\n\t\"featured\" : false,\n\t\"draft\": false,\n\t\"contents\": \"本文掲載\" <-- HTMLタグで生成して -->\n}\n```",
            messages=[
                {
                    "role": "user",
                    "content": [
                            {
                                "type": "text",
                                "text": "下記の大ジャンルと小ジャンルをランダムで選び、前回生成したものと違うジャンルの記事を書いてください。\n“””\n国際\n- アメリカ\n- アジア\n- ヨーロッパ\n- 中東\n- オセアニア\n- アフリカ\n経済\n- ビジネス\n- マネー\n- スタートアップ\n- テクノロジー\n- 乗り物\n社会\n- 事件\n- 事故\n- 裁判\n- 気象・災害\n- ウイルス\n暮らし\n- ネットで話題\n- 生き物\n- 教育・子育て\n- 医療・健康\n- グルメ\n- 防災\n- 環境\n- SDGs\n話題・グルメ\n- 国内\n- 国際\nエンタメ\n- 芸能\n- 文化\n- 音楽\n- 映画\n- 文学\n- アニメ\n- スポーツ\n“””\n"
                            }
                    ]
                }
            ]
        )
        cleaned_json_data = generate_json_file(response.content)
        save_json_file(cleaned_json_data)

        return cleaned_json_data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


def get_json_file_name():
    now = datetime.now()
    json_file_name = now.strftime("%Y%m%d_%H%M%S") + ".json"
    return json_file_name

# claudeはtextプロパティに全てを詰め込んでレスポンスするため正規表現などで処理する
def generate_json_file(content_blocks):
    text = content_blocks[0].text
    print(text)
    json_start_bracket = re.search(r"{", text).start()
    json_end_bracket = re.search(r"}\s*", text)
    if json_end_bracket:
        json_end_bracket = json_end_bracket.end()
    else:
        text += "}"
    json_end_bracket = len(text)
    json_data = text[json_start_bracket:json_end_bracket]
    cleaned_json_data = re.sub(r"[\n\t`]", "", json_data)

    return cleaned_json_data

def save_json_file(cleaned_json_data):
    json_file_name = get_json_file_name()
    with open(f'../outputs/article/{json_file_name}', 'w') as f:
        f.write(cleaned_json_data)
