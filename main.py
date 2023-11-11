from fastapi import FastAPI, File, UploadFile
import requests

app = FastAPI()

def upload_image(image: UploadFile, description: str, tags: str):
    # Обработка изображения
    image_data = image.file.read()

    # Создание объекта элемента формы для отправки запроса на contributor.stock.adobe.com
    form_data = {
        'image': (image.filename, image_data, image.content_type),
        'description': description,
        'tags': tags
    }

    # Отправка запроса на contributor.stock.adobe.com для загрузки изображения
    response = requests.post('https://contributor.stock.adobe.com/api/path/to/upload', files=form_data)

    # Возвращение ответа
    return response.json()

@app.post('/upload')
async def upload(image: UploadFile = File(...), description: str, tags: str):
    result = upload_image(image, description, tags)
    return result