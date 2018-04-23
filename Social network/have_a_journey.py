import time
from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()

# entering the site

driver.get("https://github.com/")

t = randint(8,10)

time.sleep(t)

# closing the tab or browser

driver.close()
