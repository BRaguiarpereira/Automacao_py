from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"./chromedriver.exe")
driver.get('https://selenium-python.readthedocs.io/installation.html')