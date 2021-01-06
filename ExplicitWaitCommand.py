from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver_win32\chromedriver.exe")
# driver = webdriver.Firefox(executable_path="C:\DRIVERS\geckodriver-v0.28.0-win64\geckodriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.expedia.com")
# driver.find_element_by_id("tab-flight-tab-hp").click()
driver.find_element(By.ID, "tab-flight-tab-hp").click()     # Flights Button
time.sleep(5)
driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("SFO")
driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("NYC")
driver.find_element(By.ID, "flight-departing-hp-flight").clear()
driver.find_element(By.ID, "flight-departing-hp-flight").send_keys("12/10/2018")
driver.find_element(By.ID, "flight-departing-hp-flight").clear()
driver.find_element(By.ID, "flight-returning-hp-flight").send_keys("15/10/2018")
driver.find_element(By.XPATH, "//*[@id='gcw-flights-form-hp-flights']/div[7]/label/button").click()     # SEARCH
# ExplicitWaits Starts Here
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='stopFilter_stops-0']")))
element.click()
time.sleep(10)
driver.quit()
