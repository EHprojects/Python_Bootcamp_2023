from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


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
        pass


bot = InternetSpeedTwitterBot()

bot.get_internet_speed()
bot.tweet_at_provider()
