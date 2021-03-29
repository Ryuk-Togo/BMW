from selenium import webdriver

browser = webdriver.Chrome()
type(browser)
browser.get('http://inventwithpython.com/')

try:
    print('そのクラス名を持つ要素<{}>を見つけた。'.format(elem.tag_name))
except:
    print('そのクラス名を持つ要素は見つからなかった。')

link_elem = browser.find_element_by_link_text('More Info')
link_elem.click()
