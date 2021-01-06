from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver_win32\chromedriver.exe")
driver.get('http://demo.automationtesting.in/Windows.html')
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
print(driver.current_window_handle)
handles=driver.window_handles
for i in handles:
    driver.switch_to_window(i)
    print(driver.title)
    if driver.title=="Frames & windows":
        driver.close()
driver.quit()