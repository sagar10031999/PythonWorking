from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver_win32\chromedriver.exe")
driver.get("https://edumple.com/signin/")
print(driver.current_url)
print(driver.title)
print("----------------------------------------------------------------------")
driver.find_element_by_id("login-form-username").send_keys("pulkit@kaysonseducation.co.in")
driver.find_element_by_id("login-form-password").send_keys("adminadmin")
driver.find_element_by_id("login-form-submit").click()
print(driver.current_url)
print(driver.title)
print("----------------------------------------------------------------------")
links=driver.find_elements(By.TAG_NAME, "a")
#driver.find_element(By.LINK_TEXT, "Institute").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "Inst").click()
"""print("Links Present : ",len(links))
for i in links:
    print(i.text)"""