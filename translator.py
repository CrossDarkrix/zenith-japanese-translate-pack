import json, time
import asyncio
from googletrans import Translator # py-googletrans(https://github.com/ssut/py-googletrans)

with open("en_us.json", 'r', encoding='utf-8') as f:
    data = json.load(f)

async def translate_text():
    async with Translator() as translator:
        for ky, vl in data.items():
            try:
                if "/" in data[ky]:
                    continue
                try:
                    text = await translator.translate(data[ky], dest='ja', src='en')
                    print("{} -> {}".format(data[ky], text.text))
                    data[ky] = text.text
                except:
                    time.sleep(12)
                    try:
                        text = await translator.translate(data[ky], dest='ja', src='en')
                        print("{} -> {}".format(data[ky], text.text))
                        data[ky] = text.text
                    except:
                        print('excepted: {}'.format(data[ky]))
                        continue
            except KeyboardInterrupt:
                break

asyncio.run(translate_text())

with open("ja_jp.json", "w", encoding='utf-8') as j:
    json.dump(data, j, indent=2, ensure_ascii=False)