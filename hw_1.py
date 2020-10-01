from bs4 import BeautifulSoup
from selenium import webdriver
import time
import dload

driver = webdriver.Chrome('./chromedriver')
driver.get("https://search.daum.net/search?w=img&nil_search=btn&DA=NTB&enc=utf8&q=%EC%95%84%EC%9D%B4%EC%A6%88%EC%9B%90%20%EA%B9%80%EC%B1%84%EC%9B%90") # 여기에 URL을 넣어주세요
time.sleep(5)

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')



thumbnails = soup.select("#imgList > div > a > img")

i = 0
for thumbnail in thumbnails:
    img = thumbnail['src']
    dload.save(img, f'./img_hw/{i}.jpg')
    i += 1

driver.quit() # 끝나면 닫아주기


