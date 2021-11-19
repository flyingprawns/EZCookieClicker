from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# --------------  Open cookie clicker page in Selenium --------------- #
s = Service("C:/Users/Jack/Documents/Development/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
assert "Cookie" in driver.title

# -------------- Find and save essential UI elements -------------- #
cookie = driver.find_element(By.ID, "cookie")
cursor = driver.find_element(By.ID, "buyCursor")
grandma = driver.find_element(By.ID, "buyGrandma")
factory = driver.find_element(By.ID, "buyFactory")
mine = driver.find_element(By.ID, "buyMine")
shipment = driver.find_element(By.ID, "buyShipment")
alchemy = driver.find_element(By.ID, "buyAlchemy lab")
portal = driver.find_element(By.ID, "buyPortal")
timeMachine = driver.find_element(By.ID, "buyTime machine")
shop = [timeMachine, portal, alchemy, shipment, mine, factory, grandma, cursor]


# -------------- Cookie clicker functions -------------- #
def get_money():
    # Parses the text field of "money" to get cookies per second
    txt = driver.find_element(By.ID, "money").text
    return int(txt.strip(","))


def get_cps():
    # Parses the text field of "cps" to get cookies per second
    txt = driver.find_element(By.ID, "cps").text
    num_found = False
    ans = ""
    for char in txt:
        if char.isnumeric():
            ans += char
            num_found = True
        elif num_found and char != ",":
            break
    return int(ans)


def get_price(item):
    # Parses the text field of an item and returns its price.
    num_found = False
    ans = ""
    for char in item.text:
        if char.isnumeric():
            ans += char
            num_found = True
        elif num_found and char != ",":
            break
    return int(ans)


def upgrade():
    # Finds the item with highest base price, then attempts to buy it.
    money = get_money()
    for item in shop:
        if get_price(item) <= money:
            item.click()
            return


# -------------- Before 500 cookies/s is reached -------------- #
click_interval = 0.00001
cycles_til_upgrade = 300
cycle = 0
while True:
    # Click on cookie
    time.sleep(click_interval)
    cookie.click()
    # Occasionally check for upgrades
    cycle += 1
    if cycle >= cycles_til_upgrade:
        upgrade()
        # Refresh page elements after upgrade
        cookie = driver.find_element(By.ID, "cookie")
        cursor = driver.find_element(By.ID, "buyCursor")
        grandma = driver.find_element(By.ID, "buyGrandma")
        factory = driver.find_element(By.ID, "buyFactory")
        mine = driver.find_element(By.ID, "buyMine")
        shipment = driver.find_element(By.ID, "buyShipment")
        alchemy = driver.find_element(By.ID, "buyAlchemy lab")
        portal = driver.find_element(By.ID, "buyPortal")
        timeMachine = driver.find_element(By.ID, "buyTime machine")
        shop = [timeMachine, portal, alchemy, shipment, mine, factory, grandma, cursor]
        # Reset cycle
        cycle = 0
        if get_cps() >= 500:
            print("CPS exceeds chosen limit. Program will no longer click.")
            break

# -------------- After 500 cookies/s is reached -------------- #
UPGRADE_INTERVAL = 8
while True:
    time.sleep(UPGRADE_INTERVAL)
    upgrade()
    # Refresh page elements after upgrade
    cookie = driver.find_element(By.ID, "cookie")
    cursor = driver.find_element(By.ID, "buyCursor")
    grandma = driver.find_element(By.ID, "buyGrandma")
    factory = driver.find_element(By.ID, "buyFactory")
    mine = driver.find_element(By.ID, "buyMine")
    shipment = driver.find_element(By.ID, "buyShipment")
    alchemy = driver.find_element(By.ID, "buyAlchemy lab")
    portal = driver.find_element(By.ID, "buyPortal")
    timeMachine = driver.find_element(By.ID, "buyTime machine")
    shop = [timeMachine, portal, alchemy, shipment, mine, factory, grandma, cursor]
