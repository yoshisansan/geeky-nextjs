from io import BytesIO
import requests

def download_image_as_file(image_url):
    response = requests.get(image_url)
    if response.status_code == 200:
        # メモリ上にファイルを作成して返す
        return BytesIO(response.content)
    else:
        raise Exception("画像のダウンロードに失敗しました。")

def save_image_to_local(file_object, file_name):
    with open(file_name, 'wb') as file:
        file.write(file_object.read())

