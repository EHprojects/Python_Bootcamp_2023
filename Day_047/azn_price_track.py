import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import smtplib

load_dotenv("../.idea/.env")

# Email
EMAIL_ADDR = os.getenv("EMAIL_ADDR")
EMAIL_PASS = os.getenv("EMAIL_PASS")
EMAIL_RECV = os.getenv("EMAIL_RECV")


def send_mail_notif(pdt_title, pdt_price, pdt_url):
    subject = "Amazon Price Alert!"
    message = f"{pdt_title} now {pdt_price}\n{pdt_url}"

    email_content = f"Subject: {subject}\n\n{message}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL_ADDR, password=EMAIL_PASS)
        connection.sendmail(from_addr=EMAIL_ADDR,
                            to_addrs=EMAIL_RECV,
                            msg=email_content)


URL = "https://www.amazon.com/dp/B075CYMYK6"

azn_head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

azn_req = requests.get(url=URL, headers=azn_head)
azn_resp = azn_req.text

soup = BeautifulSoup(azn_resp, "lxml")

# product_title = soup.find('span', id='productTitle').getText(strip=True)
product_title = soup.find('span', id='productTitle').getText()
product_title = product_title.strip().encode('utf-8')
print(product_title)

price_list = soup.find_all(name="span", class_="a-offscreen")
azn_new = price_list[1].getText()
azn_new = float(azn_new.replace('$', ''))
print(azn_new)

if azn_new < 120:
    send_mail_notif(product_title, azn_new, URL)
