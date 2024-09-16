

from selenium import webdriver
from selenium.webdriver.common.by import By
browserSortedVeggies=[]
driver= webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()

driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
veggiWebelemnts=driver.find_elements(By.XPATH, "//tr/td[1]")

for ele in veggiWebelemnts:
    browserSortedVeggies.append(ele.text)
originalSortedList = browserSortedVeggies.copy()
print(originalSortedList)

sortedList=browserSortedVeggies.sort()




assert browserSortedVeggies == originalSortedList



