import time
from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()

# entering the site

driver.get("https://www.tutorialspoint.com/index.htm")

t = randint(7,12)

time.sleep(t)




