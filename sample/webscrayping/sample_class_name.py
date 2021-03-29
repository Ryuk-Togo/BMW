from selenium import webdriver
from selenium.webdriver.common.keys import Keys
 
#ChromeDriverのパスを引数に指定しChromeを起動
driver = webdriver.Chrome()
#指定したURLに遷移する
driver.get("https://www.google.co.jp")
#検索テキストボックスの要素をClass属性名から取得
element = driver.find_element_by_class_name("gsfi")
#検索テキストボックスに"Selenium"を入力
element.send_keys("Selenium")
#Enterキーを押下して検索を実行
element.send_keys(Keys.ENTER)