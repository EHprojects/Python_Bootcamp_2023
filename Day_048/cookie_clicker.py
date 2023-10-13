from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Keep Chrome Open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

URL = "https://orteil.dashnet.org/experiments/cookie/"

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# Maximize the browser window
driver.maximize_window()

# get the cookie item
cookie = driver.find_element(By.CSS_SELECTOR, value="div #cookie")


# Check store items and buy the most expensive one possible
def buy_item():
    money_val = driver.find_element(By.ID, value="money")
    money = int(money_val.text)

    # get the items from the store
    store = driver.find_element(By.ID, value="store")
    store_items = store.find_elements(By.TAG_NAME, value="div")

    for item in store_items[::-1]:
        # print(item.text)
        if item.text != "":
            # print(item.text)
            item_cost = item.find_element(By.TAG_NAME, value="b").text
            item_cost = int(item_cost.split("-")[1].strip().replace(",", ""))
            # print(item_cost)
            if money >= item_cost:
                item.click()
                break


game_dur = time.time() + 60  # time in secs
check_time = time.time() + 5

# Main Loop
while True:
    cookie.click()
    if time.time() > game_dur:
        break

    if time.time() > check_time:
        buy_item()
        check_time = time.time() + 5


# clicks = 0
#
# while clicks < 550:
#     # Find the cookie and click it
#     cookie.click()
#     clicks += 1


