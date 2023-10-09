from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome Open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

URL = "https://www.python.org/"

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# events = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]') # XPath option
events = driver.find_element(By.CSS_SELECTOR, value=".event-widget")  # CSS Selector option

python_events = {}

menu_items = events.find_elements(By.TAG_NAME, value="li")
for i in range(0, len(menu_items)):
    time_tag = menu_items[i].find_element(By.TAG_NAME, value="time")
    date = time_tag.get_attribute("datetime").split("T")[0]

    event_link = menu_items[i].find_element(By.CSS_SELECTOR, value="a")
    event = event_link.text

    python_events[i] = {
        "time": date,
        "name": event
    }

    # python_events[str(i)] = event_dict

print(python_events)

driver.quit()  # closes application
