from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv

load_dotenv("../.idea/.env")

# [Twitter]
X_LOGIN = os.getenv("X_LOGIN")
X_PASS = os.getenv("X_PASS")


class InternetSpeedTwitterBot:

    def __init__(self):
        self.down_speed = 0
        self.up_speed = 0
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()

    def get_internet_speed(self):
        speed_url = "https://www.speedtest.net/"
        self.driver.get(speed_url)
        # time.sleep(3)
        # Find the link using its class name and click it
        link = self.driver.find_element('css selector', '.js-start-test.test-mode-multi')
        link.click()
        time.sleep(45)
        # btn_close = self.driver.find_element(By.CSS_SELECTOR, value="close-btn")
        # btn_close = self.driver.find_element(By.XPATH,
        #                                      value="/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/div[2]/a")
        # btn_close.click()
        dn_speed = self.driver.find_element(By.CSS_SELECTOR,
                                            value=".result-data-value.download-speed")
        # Close the pop-up if desired
        # dn_speed = self.driver.find_element(By.XPATH,
        #                                     value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        dn_speed = float(dn_speed.text)
        up_speed = self.driver.find_element(By.CSS_SELECTOR, value=".result-data-value.upload-speed")
        up_speed = float(up_speed.text)
        print(f"Down: {dn_speed}")
        print(f"Up: {up_speed}")

    def tweet_at_provider(self):
        twitter_url = "https://twitter.com/"
        self.driver.get(twitter_url)

        # Find the span element containing the specific text using XPath and click it
        btn_signin = self.driver.find_element(By.XPATH, value='//span[contains(text(),"Sign in")]')
        btn_signin.click()

        # Find the input box using its class attribute and type text into it
        # user_name = self.driver.find_element('css selector', 'input.r-30o5oe')
        time.sleep(1)
        user_name = self.driver.find_element(By.XPATH, value='/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        user_name.send_keys(X_LOGIN)

        btn_next = self.driver.find_element(By.XPATH, value='/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
        btn_next.click()

        time.sleep(1)
        input_pass = self.driver.find_element(By.XPATH, value='/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        input_pass.send_keys(X_PASS)

        btn_login = self.driver.find_element(By.XPATH, value='/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
        btn_login.click()

        time.sleep(1)
        btn_post = self.driver.find_element(By.XPATH, value='/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        btn_post.click()

        time.sleep(1)
        in_post = self.driver.find_element(By.XPATH, value='/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div')
        in_post.send_keys("This is a test!")

        btn_sendpost = self.driver.find_element(By.XPATH, value='/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]')
        btn_sendpost.click()


bot = InternetSpeedTwitterBot()

bot.get_internet_speed()
bot.tweet_at_provider()
