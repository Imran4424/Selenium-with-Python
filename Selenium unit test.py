import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase):
    
    
    def setUp(self):
        self.driver = webdriver.Firefox()


    def Test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")

        self.assertIn("Python", driver.title)

        element = driver.find_element_by_name("q")
        element.send_keys("pycon") 