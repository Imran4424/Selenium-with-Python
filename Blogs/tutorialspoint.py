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

driver.execute_script("window.scrollTo(0,300*1)")

t = randint(7, 12)

time.sleep(t)

# scroll down 2nd time in a row

driver.execute_script("window.scrollTo(0,300*2)")

t = randint(7, 12)

time.sleep(t)

# going to library

element_library = driver.find_element_by_xpath("/html/body/div[4]/div[3]/div[3]/div[1]/div/a/img")


element_library.send_keys(Keys.RETURN)

t = randint(7, 12)

time.sleep(t)

# close 

driver.close()
