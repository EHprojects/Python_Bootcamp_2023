import requests
import os
from dotenv import load_dotenv
import smtplib

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
CHANGE_VAL = 0.0045

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

load_dotenv("../.idea/.env")

# Alpha Vantage
AV_API_KEY = os.getenv("AV_API_KEY")
# News API
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
# Email
EMAIL_ADDR = os.getenv("EMAIL_ADDR")
EMAIL_PASS = os.getenv("EMAIL_PASS")
EMAIL_RECV = os.getenv("EMAIL_RECV")


def send_mail_notif(stock_info):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL_ADDR, password=EMAIL_PASS)
        connection.sendmail(from_addr=EMAIL_ADDR,
                            to_addrs=EMAIL_RECV,  # change to "email"
                            msg=f"Test\n\n{stock_info['brief']}")

# {stock_info['stock']}: {stock_info['chng_symb']}{stock_info['change']}: {stock_info['headline']}
# STEP 1: Use https://www.alphavantage.co/query When STOCK price increase/decreases by 5% between
# yesterday and the day before yesterday then print("Get News"). HINT 1: Get the closing price for yesterday and the
# day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive
# difference is 20. HINT 2: Work out the value of 5% of yerstday's closing stock price.

alpha_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": AV_API_KEY,
}

alpha_response = requests.get(url=STOCK_ENDPOINT, params=alpha_params)
alpha_response.raise_for_status()
last_day = list(alpha_response.json()["Time Series (Daily)"].keys())[0]
prev_day = list(alpha_response.json()["Time Series (Daily)"].keys())[1]

last_day_dat = alpha_response.json()["Time Series (Daily)"][last_day]
last_day_close = float(alpha_response.json()["Time Series (Daily)"][last_day]["4. close"])
prev_day_dat = alpha_response.json()["Time Series (Daily)"][prev_day]
prev_day_close = float(alpha_response.json()["Time Series (Daily)"][prev_day]["4. close"])

last_prev_diff = abs(last_day_close - prev_day_close)  # diff btw last day and prev day
pct_chng = round(((last_day_close / prev_day_close) - 1), ndigits=4)

print(f"last_day_close: {last_day_close}")
print(f"prev_day_close: {prev_day_close}")
print(f"last_prev_diff: {last_prev_diff}")
print(f"pct_chng: {pct_chng}")

if abs(pct_chng) > CHANGE_VAL:
    print("Get News")

# STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
# HINT 1: Think about using the Python Slice Operator

news_params = {
    "apiKey": NEWS_API_KEY,
    "q": COMPANY_NAME
}

news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
news_response.raise_for_status()
news_articles = news_response.json()["articles"][0:1]
print(news_articles)

# STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
# HINT 1: Consider using a List Comprehension.

articles = []

for article in news_articles:
    new_article = {
        "stock": STOCK,
        "change": pct_chng,
        "headline": article["title"],
        "brief": article["description"]
    }
    if pct_chng > 0:
        new_article["chng_symb"] = "up"
    else:
        new_article["chng_symb"] = "dn"

    articles.append(new_article)

for article in articles:
    send_mail_notif(article)

# Optional: Format the SMS message like this:
"""TSLA: 🔺2% Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. Brief: We at Insider Monkey have 
gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings 
show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
 
or "TSLA: 🔻5% Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. Brief: We at Insider Monkey 
have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F 
filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus 
market crash."""
