import re
from datetime import datetime


class ContentBlock:
    def __init__(self, text, type):
        self.text = text
        self.type = type

def get_json_file_name():
    now = datetime.now()
    json_file_name = now.strftime("%Y%m%d_%H%M%S") + ".json"
    return json_file_name

def generate_json_file(content_blocks):
    text = content_blocks[0]['text']
    print(text)
    json_start_bracket = re.search(r"{", text).start()
    json_end_bracket = re.search(r"}\s*", text)
    if json_end_bracket:
        json_end_bracket = json_end_bracket.end()
    else:
        text += "}"
    json_end_bracket = len(text)
    json_data = text[json_start_bracket:json_end_bracket]
    cleaned_json_data = re.sub(r"[\n\t]", "", json_data)
    print(cleaned_json_data)
    json_file_name = get_json_file_name()
    with open(f'./outputs/{json_file_name}', 'w') as f:
        f.write(cleaned_json_data)


response_content = [{"text":"以下の条件で記事を作成しました。\n\n{\n\t\"title\" : \"ネオ日本の人気VTuberが異次元合体!? 新たな存在「VTuberロボ」が誕生し話題に\",\n\t\"categories\" : \"['エンタメ', 'アニメ']\",\n\t\"featured\" : false,\n\t\"draft\": false,\n\t\"contents\": \"<p>ネオ日本のオンバーチャル空間で活動する人気VTuberたちが、異次元合体を果たし「VTuberロボ」となって話題を呼んでいる。</p>\n\n<p>きっかけは、あるVTuberが自身のニューラリンクポッドのアップデート中に発生したバグ。そのバグの影響で、複数のVTuberのアバターデータが混ざり合い、全く新しい存在が生まれたのだ。</p>\n\n<p>通称「VTuberロボ」と呼ばれるこの存在は、合体に関わったVTuberたちの特徴を併せ持つ。中には、顔はAのVTuber、体はBのVTuber、声はCのVTuber、といった具合にパーツごとに別のVTuberの要素が混ざり合ったキメラのようなものも。</p>\n\n<h2>VTuberファンから歓喜の声</h2>\n\n<p>このニュースを受け、VTuberファンからは歓喜の声が上がっている。あるファンは「推しVTuberたちが合体するなんて夢のよう！」と興奮気味に語った。また「普段は共演することのない者同士が一つになるのはすごく新鮮」という声も。</p>\n\n<h2>VTuber事務所は対応に追われる</h2>\n\n<p>一方、VTuberが所属する事務所は対応に追われている模様。ニューラリンクポッドのバグが原因とはいえ、無断で他者のアバターデータを使用することになるため、肖像権などの問題が懸念されるためだ。</p>\n\n<p>ただ、今回のケースでは、関係者の話し合いにより、「VTuberロボ」としての限定的な活動を特例的に認める方向で調整が進んでいるという。ファンにとっては、喜ばしいニュースと言えるだろう。</p>\n\n<p>「VTuberロボ」は、今後どのような活躍を見せてくれるのか。オンバーチャル空間の住人たちの注目を集めている。</p>\"\n}","type":"text"}]
generate_json_file(response_content)