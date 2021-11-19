from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Open cookie clicker page in Selenium
s = Service("C:/Users/Jack/Documents/Development/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
assert "Cookie" in driver.title

# Find and save essential UI elements
cookie = driver.find_element(By.ID, "cookie")
money = driver.find_element(By.ID, "money")
cursor = driver.find_element(By.ID, "buyCursor")
grandma = driver.find_element(By.ID, "buyGrandma")
factory = driver.find_element(By.ID, "buyFactory")
mine = driver.find_element(By.ID, "buyMine")
shipment = driver.find_element(By.ID, "buyShipment")
alchemy = driver.find_element(By.ID, "buyAlchemy lab")
portal = driver.find_element(By.ID, "buyPortal")
timeMachine = driver.find_element(By.ID, "buyTime machine")

# # Play the game
# CLICK_INTERVAL = 0.00001
# CYCLES_TIL_UPGRADE = 501
# cycle = 0
# while True:
#     # Click on cookie
#     time.sleep(CLICK_INTERVAL)
#     cookie.click()
#     # Occasionally check for upgrades
#     cycle += 1
#     if cycle >= CYCLES_TIL_UPGRADE:
#         print("5s has passed")
#         cycle = 0


def upgrade():
    print(money.text)


upgrade()