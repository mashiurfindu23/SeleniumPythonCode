

from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()

driver.find_element(By.LINK_TEXT, "Click Here").click()
handles=driver.window_handles
driver.switch_to.window(handles[1])

newWindowText=driver.find_element(By.TAG_NAME, "h3").text
print(newWindowText)
assert newWindowText == "New Window"


driver.switch_to.window(handles[0])
parentWindowText=driver.find_element(By.TAG_NAME, "h3").text
print(parentWindowText)

assert parentWindowText == "Opening a new window"



