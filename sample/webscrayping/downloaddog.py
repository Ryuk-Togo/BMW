#! python3
# downloaddog.py - Googleで検索した犬の画像をダウンロードする

import os, sys

import bs4
import requests
import selenium

url = 'https://www.google.com/search?q=%E7%8A%AC&rlz=1C5CHFA_enJP768JP786&hl=ja&sxsrf=ALeKk03eFrmlfhPWCpOEKIjFpZqn3HVUgQ:1614220676652&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjAgpXQgITvAhXNfd4KHbrIChkQ_AUoAXoECAcQAw&biw=1280&bih=536'
os.makedirs('dogimg', exist_ok=True)

res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser') # 第２引数はワーニング防止
# print(res.text)
# res.textから対象の画像とclassを調べる。srcと画像が一致するタグに注目
dogimg_elem = soup.select('img[class="t0fcAb"]')

row = 0
for url in dogimg_elem:
    row += 1
    # TODO: ページをダウンロードする
    print('{}件目'.format(row))
    dogimg_url = url.get('src')
    
    # TODO: 欲しいデータをダウンロードする
    print('画像をダウンロード中 {}...'.format(dogimg_url))
    res = requests.get(dogimg_url)
    res.raise_for_status()

    # TODO: 欲しいデータをHDDに保存する
    image_file = open(os.path.join('dogimg', os.path.basename('dogimg_' + str(row) + '.png')), 'wb')
    for chumk in res.iter_content(100000):
        image_file.write(chumk)
    image_file.close()

print('完了')