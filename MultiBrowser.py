from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver_win32\chromedriver.exe")
#driver = webdriver.Firefox(executable_path="C:\DRIVERS\geckodriver-v0.28.0-win64\geckodriver.exe")
driver.get("https://edumple.com/")
print(driver.title)
print(driver.current_url)
#print(driver.page_source)
driver.close()