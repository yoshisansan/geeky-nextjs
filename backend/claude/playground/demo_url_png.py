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
# 使用例
image_url = "https://oaidalleapiprodscus.blob.core.windows.net/private/org-vM99ZyYJ4JkUT8b1YqNcy5zi/user-kResN0pbcYgnfVadSIxRmAeY/img-VNPNqcQUPZ9kHp2uTYotnB2h.png?st=2024-03-24T15%3A16%3A18Z&se=2024-03-24T17%3A16%3A18Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-03-23T21%3A06%3A52Z&ske=2024-03-24T21%3A06%3A52Z&sks=b&skv=2021-08-06&sig=PUfiESjx0763liuZu5Cu/5aVci3dYEU%2Bq2E5fjuQ0YA%3D"
file_object = download_image_as_file(image_url)
save_image_to_local(file_object, 'test.png')
print(file_object)

