import time
from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()

# entering the site

driver.get("https://www.facebook.com")

t = randint(8,10)

time.sleep(t)

# writing to homepage wall

element_home_post = driver.find_element_by_css_selector("._1mf")

element_home_post.send_keys("Hi Dipak, Are you watching, Welcome to selenium automation")

time.sleep(t)

# closing the posting window

element_home_close = driver.find_element_by_css_selector(".sx_90723f")

time.sleep(t)




# closing the tab or browser

driver.close()