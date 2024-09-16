import time

from selenium.webdriver.support.select import Select

from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "#name").send_keys("Mashiur")
time.sleep(3)
driver.find_element(By.ID, "alertbtn").click()
alert=driver.switch_to.alert
alertText=alert.text
print(alertText)
alert.accept()

time.sleep(5)
