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
driver.get("https://classic.crmpro.com/index.html")
print(driver.title)
username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")
login_button = driver.find_element(By.XPATH, "//input[@value='Login']")

username.send_keys("mhreza76")
password.send_keys("123456")
login_button.click()


time.sleep(2)
driver.quit()

