from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver_win32\chromedriver.exe")
driver.get("https://seleniumhq.github.io/selenium/docs/api/java/index.html")
driver.switch_to_frame("packageListFrame")
driver.find_element_by_link_text("org.openaq.selenium").click()
time.sleep(3)
driver.switch_to_default_content()
driver.switch_to_frame("packageFrame")
driver.find_element_by_link_text("WebDriver").click()
time.sleep(3)
driver.switch_to_default_content()
time.sleep(3)
driver.switch_to_frame("classFrame")
driver.find_element_by_xpath("/html/body/div[1]/ul/li[5]").click()