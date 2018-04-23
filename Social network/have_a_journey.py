import time
from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()

# entering the site

driver.get("https://www.facebook.com/")

t = randint(8,10)

time.sleep(t)

# writing to homepage wall

element_home_post = driver.find_element_by_css_selector("._1mf")


