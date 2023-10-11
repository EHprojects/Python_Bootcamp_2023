# Interaction
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep Chrome Open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

URL = "https://en.wikipedia.org/wiki/Main_Page"

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# Maximize the browser window
driver.maximize_window()

# Locate the button donation popup close button and click it
close_dono = driver.find_element(By.CSS_SELECTOR, value='button.frb-icon-btn.frb-close[aria-label="Close"]')
close_dono.click()

article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")  # CSS Selector option
# print(article_count.text)
# article_count.click()

ongoing = driver.find_element(By.LINK_TEXT, value="Ongoing")
# ongoing.click()

search = driver.find_element(By.NAME, value="search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

# driver.quit()  # closes application
