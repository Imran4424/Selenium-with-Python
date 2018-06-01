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
        driver.get("http://www.livescore.com/soccer/brazil/")

elif sports == 2:
    print("1. Live")
    print("2. ICC World Cup One-Day")
    print("3. ICC World Cup T20")
    print("4. International One-Day")
    print("5. International T20")
    print("6. International Test")
    print("7. ICC Champions Trophy")
    print("8. Bangladesh")

    cricket = int(input("chose an option: "))

    if cricket == 1:
        driver.get("http://www.livescore.com/cricket/live/")
    elif cricket == 2:
        driver.get("http://www.livescore.com/cricket/wc_odi/")
    elif cricket == 3:
        driver.get("http://www.livescore.com/cricket/icc-world-t20/")
    elif cricket == 4:
        driver.get("")
