import cv2
import numpy as np

def read_img(uploader):
    """
    Функция за прочитане на изображение качено с интерактивния uploader на ipywidgets
    
    аргументи:
        uploader: инстанцията на uploader, където е качен файла

    Връща изображението като масив.
    """
    # зареди първия качен файл
    uploaded_file = uploader.value[0]
    # провери дали типа на файла е изображение
    if 'image' in uploaded_file.type:
        # прочитане на байтовете и преобразуване като numpy масив
        np_array = np.frombuffer(uploaded_file.content.tobytes(), np.uint8)
        # преобразуване като изображение
        image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
        # преобразуване в стандартната за openCV цветова схема синьо/зелено/червено
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        print("Изображението беше успешно заредено. Размер (височина х широчина х цветови канали):")
        # изписване на размера на изображението
        print(image.shape)
        
        return image
    else:
        print('Файлът не е изображение, опитайте отново.')

    