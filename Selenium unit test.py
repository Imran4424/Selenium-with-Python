import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase):
    
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        
