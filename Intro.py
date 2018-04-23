import time
from random import randint
from selenium import  webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox();

driver.get("http://www.python.org")

assert "Python" in driver.title

t = randint(10,15)

time.sleep(t)

element = driver.find_element_by_name("q")

element.clear() #for clearing the search field

element.send_keys("pycon")  #giving input to search key "pycon"

element.send_keys(Keys.RETURN)   # returning result

assert "No results found." not in driver.page_source  #if there is nothing in return

time.sleep(t)

driver.close()