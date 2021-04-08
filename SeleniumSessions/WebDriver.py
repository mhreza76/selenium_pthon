import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Users/reza/PycharmProjects/selenium_python/chromedriver")
driver.implicitly_wait(5)
driver.get("https://www.google.com/")
print(driver.title)
driver.find_element(By.NAME, 'q').send_keys('Bangladesh Army International')
optionList = driver.find_elements(By.CSS_SELECTOR, 'ul.erkvQe li span')
print(len(optionList))
for opt in optionList:
    print(opt.text)
    if opt.text == 'bangladesh army international tender':
        opt.click()
        break

time.sleep(2)
driver.quit()
