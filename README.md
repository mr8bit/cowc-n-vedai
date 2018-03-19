# COWC and VEDAI

Создайте папку images и распакуйте туда файлы с  [изображениями](https://drive.google.com/file/d/1xgCwZEO2-3jIXbiIZ-K9z2F8dZXwl0Ox/view?usp=sharing)

Или же скачайте с Yandex.Disk испольую wget:

```bash
wget "https://s51sas.storage.yandex.net/rdisk/0a132b6312a891570c8652187628f07453f4910cceb555e19ce31ec88c1e897f/5ab07e99/XdfMxdH_MOJhO8KXmNHCAmnm9FjwnlGNSkBhzumUBYhHTMDHUZMs6Tb_4Z1BgcE5JtczASO0brxuMB5K-DCufA==?uid=0&filename=images.tar.gz&disposition=attachment&hash=O4PvbGKvhLsx36MhbVgNrCUhJW0a%2BX4OT4V9CvlV4dQ%3D&limit=0&content_type=application%2Fgzip&fsize=2941327360&hid=7ec1bcca8894e56942790aa23aa0c134&media_type=compressed&tknv=v2&rtoken=hNBXitMe2ivD&force_default=no&ycrid=na-6f00bf2abd51f41f88e712c04869d203-downloader6h&ts=567cf97ba1840&s=adb4976b440dbae1facf3d73009049b499d19ed559b277ec222e36e90da2c26c&pb=U2FsdGVkX1_Y6kKKu7vMnNY-ZfweXYlilh0BRWhfbxYkjVra_P3-7xzobGX35leImLJl0f9d_0mEpNfvVot70sQipAnB8SQOwD8bN0J5gSM" -O images.tar.gz
```

Запустите скрипты:`cowc.py` для создания COWC и `vedai.py` для VEDAI. После работы скриптов у вас в папке `images/` будут лежать `xml` файлы для создания данных в формате `tfRecord`
wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=/1xgCwZEO2-3jIXbiIZ-K9z2F8dZXwl0Ox/view?usp=sharing' -O images.tar.gz
