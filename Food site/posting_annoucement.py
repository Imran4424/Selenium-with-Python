import time
from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()

driver.get("http://localhost/foodsite/index.php")

t = randint(5, 7)

time.sleep(t)

element_username = driver.find_element_by_css_selector(
    "#content > form:nth-child(11) > fieldset:nth-child(1) > label:nth-child(2) > input:nth-child(3)")


element_username.clear()  #clearing username field

element_username.send_keys("admin") #setting username admin

element_userpass = driver.find_element_by_css_selector(
    "#content > form:nth-child(11) > fieldset:nth-child(1) > label:nth-child(5) > input:nth-child(3)")


element_userpass.clear() #clearing password field

element_userpass.send_keys("admin")   #setting password field

