
from selenium.webdriver.support.select import Select

from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")
driver.maximize_window()
page_title=driver.title
print(page_title)
page_url=driver.current_url
print(page_url)
countryList=driver.find_element(By.ID, "Form_getForm_Country")
#print(countryList)
select=Select(countryList)
countries=select.options
for val in countries:
    print(val.text)
    if val.text== "Mexico":
        val.click()
        break





