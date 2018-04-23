import time
from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()

# entering the site

driver.get("http://localhost/foodsite/index.php")

t = randint(5, 7)

time.sleep(t)


# log in

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


time.sleep(t)


# going to admin page

element_admin = driver.find_element_by_css_selector("#content > a:nth-child(12)")

element_admin.send_keys(Keys.RETURN)

time.sleep(t)

# setting task to announcements

element_task = driver.find_element_by_css_selector("#content > form:nth-child(2) > fieldset:nth-child(1) > label:nth-child(2) > select:nth-child(3)")

element_task.send_keys("Announcements")

time.sleep(t)

# returning announcements page

element_select_task = driver.find_element_by_css_selector(
    "#content > form:nth-child(2) > fieldset:nth-child(1) > input:nth-child(5)")

element_select_task.send_keys(Keys.RETURN)

time.sleep(t)

# posting a new announcement

element_announcement_text = driver.find_element_by_css_selector(
    "#content > div:nth-child(8) > form:nth-child(1) > label:nth-child(1) > textarea:nth-child(3)")

element_announcement_text.clear()

element_announcement_text.send_keys("Posting from selenium python script")

time.sleep(t)

element_publish = driver.find_element_by_css_selector("#content > div:nth-child(8) > form:nth-child(1) > input:nth-child(2)")

element_publish.send_keys(Keys.RETURN)

time.sleep(t)

# going to home

element_home = driver.find_element_by_css_selector("#navigation > li:nth-child(1) > a:nth-child(1)")

element_home.send_keys(Keys.RETURN)

time.sleep(t)

# announcements page

element_announcements = driver.find_element_by_css_selector("#content > a:nth-child(7)")

element_announcements.send_keys(Keys.RETURN)

time.sleep(t)

# going to home

element_home = driver.find_element_by_css_selector("#navigation > li:nth-child(1) > a:nth-child(1)")

element_home.send_keys(Keys.RETURN)

time.sleep(t)

# log out

element_logout = driver.find_element_by_css_selector("#content > form:nth-child(15) > input:nth-child(1)")

element_logout.send_keys(Keys.RETURN)

driver.close()
