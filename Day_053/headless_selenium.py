# Try using selenium headless with the following code:
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--headless=new")


def get_html(url):
    driver = webdriver.Chrome(options=options)

    # get source code
    driver.get(url)
    time.sleep(1)
    html = driver.page_source.encode("utf-8")

    # close web browser
    driver.close()
    return html

with open("test.html", "wb") as file:
    site_html = get_html("https://www.zillow.com/homedetails/407-N-9th-St-Las-Vegas-NV-89101/7014811_zpid/")
    file.write(site_html)

# print(get_html("https://www.zillow.com/homedetails/407-N-9th-St-Las-Vegas-NV-89101/7014811_zpid/"))
