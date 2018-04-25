import time
from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()

# entering the site

driver.get("https://www.tutorialspoint.com/index.htm")

t = randint(7,12)

time.sleep(t)

# scrolling down the page

driver.execute_script("window.scrollTo(0,200*1)")

#t = randint(7, 12)

#time.sleep(t)

# scroll down 2nd time in a row

driver.execute_script("window.scrollTo(0,200*2)")

t = randint(7, 12)

time.sleep(t)


