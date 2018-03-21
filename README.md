# COWC and VEDAI

Создайте папку images и скачайте с Yandex.Disk испольую wget:

```bash
wget "https://s86sas.storage.yandex.net/rdisk/6792a74cf1e68cf57e5be496db873ce6657e1b9d3e7d087c9a459de40f717d00/5ab1f9ed/XdfMxdH_MOJhO8KXmNHCApGWGJVCUBut601Tx5r_ZFt3MI-C__ac98WzXNxG5iWCU3FgXa9Xw8_RtI3DbPgfsA==?uid=136485697&filename=images.tar.gz&disposition=attachment&hash=&limit=0&content_type=application%2Fgzip&fsize=2387118080&hid=3ebfaef37299f65ca3d18e651b21d57a&media_type=compressed&tknv=v2&etag=ebd81b2131d95283446f8ec5d51686d2&rtoken=oNSAx44T5YWX&force_default=yes&ycrid=na-427f7f68ef2eb9098b52a57d9f700115-downloader18e&ts=567e633d09540&s=e1bf16e3a0a996fdf57f4d59ab1dae45971b1e867dd7aedb2d24b2186ffc0444&pb=U2FsdGVkX18DU0jul5agHNwzpWJSflCVPjv2OG-qQQO7I1UuZm_wfTuopT1-zH4KD-bAj2R3c0sq6JXuSUYNmJG61bty6ROv7olfvOXpHlU" -O images.tar.gz
```

Запустите скрипты:`cowc.py` для создания COWC и `vedai.py` для VEDAI. После работы скриптов у вас в папке `images/` будут лежать `xml` файлы для создания данных в формате `tfRecord`
