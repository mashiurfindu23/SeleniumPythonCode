import time

from selenium.webdriver.support.select import Select

from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()

driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
countries=driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
countryList=len(countries)
print(countryList)

for country in countries:
    if country.text== "India":
        country.click()
        break

# find attribute value
print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))


#Assertion
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"


time.sleep(5)

