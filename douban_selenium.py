from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://movie.douban.com/top250")
time.sleep(2)

# 查找所有电影标题元素
titles = driver.find_elements(By.CLASS_NAME, "title")
for title in titles:
    print(title.text)

driver.quit()
