import time
from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()

# entering the site

driver.get("https://github.com/")

t = randint(7,12)

time.sleep(t)

# go to profile

driver.get("https://github.com/Imran4424")

t = randint(7, 12)

time.sleep(t)

# scroll_down

driver.execute_script("window.scrollTo(0,200*1)")

t = randint(7, 12)

time.sleep(t)

# scroll down 2nd time in a row

driver.execute_script("window.scrollTo(0,200*2)")

t = randint(7, 12)

time.sleep(t)

# closing the tab or browser

driver.close()
