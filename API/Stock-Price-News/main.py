import requests
from twilio.rest import Client

account_sid = "YOUR_ACC_SID"
auth_token = "YOUR_TOKEN"
client = Client(account_sid, auth_token)

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "YOUR_STOCK_API_KEY"
STOCK_END_POINT = "https://www.alphavantage.co/query"

NEWS_API_KEY = "YOUR_NEWS_API_KEY"
NEWS_END_POINT = "https://newsapi.org/v2/everything"

stock_para = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

news_para = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API_KEY
}

response = requests.get(STOCK_END_POINT, params=stock_para)
stock_data = response.json()["Time Series (Daily)"]
stock_list = [value for key, value in stock_data.items()]

yesterday_data_closing_price = stock_list[0]["4. close"]
day_before_yesterday_data_closing_price = stock_list[1]["4. close"]
# print(day_before_yesterday_data_closing_price)

diff = float(yesterday_data_closing_price) - float(day_before_yesterday_data_closing_price)
sign = None
if diff < 0:
    sign = "🔻"
else:
    sign = "🔺"

diff_percent = round((abs(diff)/float(yesterday_data_closing_price))*100, 2)
# print(diff_percent)
# print(stock_data['Time Series (Daily)']['2023-06-14'])
if diff_percent > 0.5:
    response2 = requests.get(NEWS_END_POINT, params=news_para)
    news_data = response2.json()["articles"]
    articles = news_data[:3]
    details = [f"TSLA: {sign}{diff_percent}% \nTitle: {article['title']} \nDescription: {article['description']}" for article in articles]
    # print(diff_percent)
    for i in details:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=i,
            to='YOUR_WHATSAPP_NUMBER'
        )




#Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent 
investors are required to file by the SEC The 13F filings show the funds' and investors' 
portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent 
investors are required to file by the SEC The 13F filings show the funds' and investors'
 portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""



