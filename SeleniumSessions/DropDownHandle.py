import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
# for select
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")
print(driver.title)
ele_emp = driver.find_element(By.ID, "Form_submitForm_NoOfEmployees")
ele_emp.click()
select = Select(ele_emp)
select.select_by_value("76 - 100")





time.sleep(10)
driver.quit()
