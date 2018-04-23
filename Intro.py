from selenium import  webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox();

driver.get("http://www.python.org")

assert "Python" in driver.title

element = driver.find_element_by_name("d")

element.clear() #for clearing the search field

element.send_keys("pycon")  #giving input to search key "pycon"

element.send_keys(Keys.RETURN)   # returning result

