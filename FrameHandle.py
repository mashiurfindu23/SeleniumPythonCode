import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/iframe")
driver.maximize_window()


time.sleep(7)
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("I am in iFrame")
driver.switch_to.default_content()
iFrameText=driver.find_element(By.TAG_NAME, "h3").text
print(iFrameText)

assert iFrameText == "An iFrame containing the TinyMCE WYSIWYG Editor"



