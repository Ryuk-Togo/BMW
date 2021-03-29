from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
import os, sys, time

SEND_KEY = '犬'
os.makedirs('dogimg', exist_ok=True)

driver = webdriver.Chrome()
driver.get('https://www.google.com/')       # Googleを開く
# print(driver.current_url)

# Googleで検索を行う
search = driver.find_element_by_name('q')   # HTML内で検索ボックス(name='q')を指定する
search.send_keys(SEND_KEY)                  # 検索ワードを送信する
search.submit()                             # 検索を実行
time.sleep(3)                               # 3秒間待機

# 検索後の画面で画像を選択する
img_link = driver.find_element_by_link_text('画像')
img_link.click()

# スクロールして最後まで画像を表示
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.find_element_by_tag_name('body').send_keys(Keys.END)
    time.sleep(2)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# 画像データを取得
cnt = 0
pic_elems = driver.find_elements_by_class_name('rg_i')
for pic_elem in pic_elems:
    cnt += 1
    url = pic_elem.get_attribute('src')
    try:
        urllib.request.urlretrieve(url, 'dogimg/dogimg_' + str(cnt) + '.png')
    except:
        pass

driver.quit()