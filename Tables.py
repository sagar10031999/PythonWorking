from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver_win32\chromedriver.exe")
driver.get("file:///C:/SeleniumPractice/sample.html")
rows=len(driver.find_elements_by_xpath("/html/body/table/tbody/tr"))
cols=len(driver.find_elements_by_xpath("/html/body/table/tbody/tr[1]/th"))
print("Rows in Table is : ",rows)
print("Columns in Table is : ", cols)
print("Product"+"    "+"Article"+"  "+"Price")
for r in range(2, rows+1):
    for c in range(1, cols+1):
        value=driver.find_element_by_xpath("/html/body/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(value, end='  ')
    print()