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

time.sleep(2)

element_userpass = driver.find_element_by_css_selector(
    "#content > form:nth-child(11) > fieldset:nth-child(1) > label:nth-child(5) > input:nth-child(3)")


element_userpass.clear() #clearing password field

element_userpass.send_keys("admin")   #setting password field

time.sleep(2)

element_login = driver.find_element_by_css_selector("#content > form:nth-child(11) > fieldset:nth-child(1) > input:nth-child(8)")

element_login.send_keys(Keys.RETURN)


t = randint(5,7)

time.sleep(t)

element_admin = driver.find_element_by_css_selector("#content > a:nth-child(12)")

element_admin.send_keys(Keys.RETURN)

time.sleep(t)

element_task = driver.find_element_by_css_selector("#content > form:nth-child(2) > fieldset:nth-child(1) > label:nth-child(2) > select:nth-child(3)")

element_task.send_keys("Announcements")

time.sleep(t)

element_select_task = driver.find_element_by_css_selector(
    "#content > form:nth-child(2) > fieldset:nth-child(1) > input:nth-child(5)")

element_select_task.send_keys(Keys.RETURN)

#driver.close()
