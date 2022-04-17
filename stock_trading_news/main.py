import requests
from twilio.rest import Client
import time

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "GS6ELFFH4MP12652"
NEWS_API_KEY = "c3745b0df0e049a2be435e999b27f647"

# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g.
# [new_value for (key, value) in dictionary.items()]

stock_params = {
    "apikey": STOCK_API_KEY,
    "symbol": STOCK_NAME,
    "function": "TIME_SERIES_DAILY",
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_date = data_list[0]
yesterday_closing_price = data_list[0]["4. close"]

# Get the day before yesterday's closing stock price

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
#  Hint: https://www.w3schools.com/python/ref_func_abs.asp

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = ""
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# Work out the percentage difference in price between closing price yesterday and closing price
#  the day before yesterday.

diff_percent = round((abs(difference) / float(yesterday_closing_price)) * 100, 2)

# If TODO4 percentage is greater than 5 then print("Get News").

# STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

news_params = {
    "q": COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
}

if diff_percent > 0:
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

# Use Python slice operator to create a list that contains the first 3 articles.
# Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

three_articles = articles[:3]

# STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline:\n{article['title']}.\nBrief:\n{article['description']}" for article in three_articles]

# TODO 9. - Send each article as a separate message via Twilio.

account_sid = 'AC9312ddefb2f5a2e02275a4a3551dbdef'
auth_token = '24da38823f11a62d87c0232d16ba4331'
client = Client(account_sid, auth_token)

for article in formatted_articles:
    message = client.messages.create(
        body=article,
        from_='+16202071026',
        to='+380989725981'
    )
    print(message.status)
    time.sleep(30)

# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

