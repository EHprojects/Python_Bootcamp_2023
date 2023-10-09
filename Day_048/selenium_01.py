from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome Open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# URL = "https://www.amazon.com/dp/B075CYMYK6"
URL = "https://www.python.org/"

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_dollar.text}.{price_cents.text}")

search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.tag_name)
print(search_bar.get_attribute("placeholder"))

button = driver.find_element(By.ID, value="submit")
print(button.size)

# <div class="small-widget documentation-widget">
#     <h2 class="widget-title">
#         <span aria-hidden="true" class="icon-documentation"/>Docs</h2>
#     <p>Documentation for Python's standard library, along with tutorials and guides, are available online.</p>
#     <p>
#         <a href="https://docs.python.org">docs.python.org</a>
#     </p>
# </div>

documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_link.text)

bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

# driver.close()  # closes tab
driver.quit()  # closes application
