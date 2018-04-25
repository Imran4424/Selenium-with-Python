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

y = 0

driver.execute_script("window.scrollTo(0,y+200)")

y += 200

t = randint(7, 12)

time.sleep(t)

# scroll down 2nd time in a row


driver.execute_script("window.scrollTo(0,y+200)")

t = randint(7, 12)

time.sleep(t)

# closing the tab or browser

driver.close()
