# from_video_to_txt


Это программа конвертирует звуковую дорожку из видео в текст

Для запуска:
1. необходимо установить flac

macOS
```
brew install flac
```

2. Установить ffmpeg

    https://ffmpeg.org/


3. Задать переменную среды

```
export IMAGEIO_FFMPEG_EXE=".../from_video_to_txt/ffmpeg"
```
где "..." - путь до директории


4. Установить зависимости

```
pip install -r requirements.txt
```

4. Запустить convert.py

```
python3 convert.py
```

Работает только с небольшими файлами!
