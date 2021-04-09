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
username_url = driver.find_element(By.ID, 'Form_submitForm_subdomain')
first_name = driver.find_element(By.ID, 'Form_submitForm_FirstName')
last_name = driver.find_element(By.ID, 'Form_submitForm_LastName')
email = driver.find_element(By.ID, 'Form_submitForm_Email')
job_title = driver.find_element(By.ID, 'Form_submitForm_JobTitle')
about_link = driver.find_element(By.LINK_TEXT, 'About OrangeHRM')

username_url.send_keys("mhreza.com")
first_name.send_keys("Mahmudul Hasan")
last_name.send_keys("Reza")
email.send_keys("rezabaiust@gmail.com")
job_title.send_keys("Bekar")
about_link.click()


time.sleep(3)
driver.quit()
