from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#driver = webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver_win32\chromedriver.exe")
driver = webdriver.Firefox(executable_path="C:\DRIVERS\geckodriver-v0.28.0-win64\geckodriver.exe")
driver.get("https://www.kaysonseducation.co.in/")
print(driver.title)
driver.get("https://edumple.com/")
time.sleep(10)
print(driver.title)
driver.back()
time.sleep(10)
print(driver.title)
driver.forward()
time.sleep(10)
print(driver.title)
driver.quit()