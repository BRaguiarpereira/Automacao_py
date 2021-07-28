from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"./chromedriver.exe")
driver.implicitly_wait(10) # seconds
driver.get("http://www.python.org")
myDynamicElement = driver.find_element_by_id("myDynamicElement")