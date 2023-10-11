from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep Chrome Open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

URL = "https://orteil.dashnet.org/experiments/cookie/"

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# Maximize the browser window
driver.maximize_window()

clicks = 0

while clicks < 2002:
    # Find the cookie and click it
    cookie = driver.find_element(By.CSS_SELECTOR, value="div #cookie")
    cookie.click()
    clicks += 1

