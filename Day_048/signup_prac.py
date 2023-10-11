# Interaction
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep Chrome Open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

URL = "http://secure-retreat-92358.herokuapp.com/"

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# Maximize the browser window
driver.maximize_window()

# Find boxes by Name
fname_input = driver.find_element(By.NAME, value="fName")
fname_input.send_keys("Anon")

# Find boxes by CSS Selector
lname_input = driver.find_element(By.CSS_SELECTOR, value='input[name="lName"]')
lname_input.send_keys("Ymous")

email_input = driver.find_element(By.NAME, value="email")
email_input.send_keys("anon@ymous.com")

signup_btn = driver.find_element(By.CSS_SELECTOR, value='button.btn.btn-lg.btn-primary.btn-block[type="submit"]')

# Alt way to find
# signup_btn = driver.find_element(By.CSS_SELECTOR, value="form button")
signup_btn.click()
