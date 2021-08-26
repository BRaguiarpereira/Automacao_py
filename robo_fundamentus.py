from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.keys import Keys

class RoboExcel(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"./chromedriver.exe")

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://fundamentus.com.br/buscaavancada.php")
        elem = driver.find_element_by_name("liq_max")
        elem.send_keys("1000000")
        elem = driver.find_element_by_name("patrim_max")
        elem.send_keys("0")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)