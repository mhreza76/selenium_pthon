import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

browserName = "chrome"
if browserName == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif  browserName == "firefox":
    driver =  webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif  browserName == "safari":
    driver =  webdriver.Safari()
elif browserName == "chromium":
    driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
elif browserName == "e dge":
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
else:
    print("Please pass the correct browser name: " +  browserName )
    raise Exception("Driver not found")

driver.implicitly_wait(10)
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")
print(driver.title)
driver.find_element(By.ID, 'Form_submitForm_subdomain').send_keys("reza768")
# driver.find_element(By.ID, '.private-form__input-wrapper #password').send_keys("reza768")
# driver.find_element(By.ID, 'loginBtn').click()
time.sleep(3)
driver.quit()
