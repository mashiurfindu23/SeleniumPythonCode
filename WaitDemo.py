import time
from selenium import webdriver
from selenium.webdriver.common.by import By


expectedList= ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actualList=[]

driver= webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()


driver.find_element(By.CSS_SELECTOR, "input.search-keyword").send_keys("ber")
time.sleep(3)
results=driver.find_elements(By.XPATH, "//div[@class='products']/div")
count=len(results)
assert count>0
for result in results:
    actualList.append(result.find_element(By.XPATH, "h4").text)
    result.find_element(By.XPATH, "div/button").click()         # webelement chaining

assert expectedList == actualList

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

#sum validation
prices =driver.find_elements(By.XPATH, "//tr/td[5]/p")
sum=0
for price in prices:
    sum= sum+ int(price.text)
print(sum)
totalAmount=int(driver.find_element(By.CSS_SELECTOR, "span.totAmt").text)
assert sum== totalAmount
driver.find_element(By.XPATH, "//input[@class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH, "//button[@class='promoBtn']").click()
promotext = driver.find_element(By.XPATH, "(//span[@class='promoInfo'])[1]").text
print(promotext)
assert promotext == "Code applied ..!"

discountPrice= float(driver.find_element(By.CLASS_NAME, "discountAmt").text)

assert totalAmount > discountPrice




