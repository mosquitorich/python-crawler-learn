from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# 设置无头模式（不显示浏览器窗口）
options = Options()
options.add_argument('--headless==new')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)
driver.get("https://www.baidu.com")
print("标题:", driver.title)
time.sleep(2)
driver.quit()
