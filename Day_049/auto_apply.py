from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Keep Chrome Open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

URL = "https://www.linkedin.com/jobs/search/?currentJobId=3687854509&geoId=92000000&keywords=behavioral%20neuroscience"

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# Maximize the browser window
driver.maximize_window()

time.sleep(2)

# Find the link using link text and click it
signin_link = driver.find_element(By.LINK_TEXT, value="Sign in")
signin_link.click()

user_in = driver.find_element(By.CSS_SELECTOR, value="#username")
user_in.send_keys("test@test.com")

pass_in = driver.find_element(By.CSS_SELECTOR, value="#password")
pass_in.send_keys("123456789")

# Find the button using CSS class and click it
button = driver.find_element(By.CSS_SELECTOR, value='.btn__primary--large.from__button--floating')
button.click()
