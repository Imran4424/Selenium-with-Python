import time
from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()

# entering the site

driver.get("http://www.livescore.com/")

# user inputs


print("1.Football")
print("2.Cricket")
print("3.Tennis")
print("4.Basketball")
print("5.Hockey\n")


sports = int(input("chose an option: "))

if sports == 1:
    print("1. Live")
    print("2. World Cup")
    print("3. International")
    print("4. Champions League")
    print("5. Brazil")
    print("6. England")

    football = int(input("chose an option: "))

    if football == 1:
        driver.get("http://www.livescore.com/soccer/live/")
    elif football == 2:
        driver.get("http://www.livescore.com/worldcup/")
    elif football == 3:
        driver.get("http://www.livescore.com/soccer/intl/")
    elif football == 4:
        driver.get("http://www.livescore.com/soccer/champions-league/")
    elif football == 5:
        print("buiding in process")

elif sports == 2:
    print("1. ICC World Cup One-Day")
    print("2. ICC World Cup T20")
    print("3. International One-Day")
    print("3. International T20")
    print("3. International Test")
    print("4. ICC Champions Trophy")
    print("5. B")
