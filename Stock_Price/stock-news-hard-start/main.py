import requests
from twilio.rest import Client



STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


twilio_sid="ACc70c64f97435dab79762b6f88e9062eb"
twilio_auth="735e70b7a7f7c66623ade0cfac98a42e"

stock_api_key="AF7B6CYPUQQPITB4"
news_api_key="2c40971320d846e78e3ebd677376d8c6"

stock_para={
    "function": "TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey": stock_api_key
    }

stock_response=requests.get(STOCK_ENDPOINT,params=stock_para)
stock_data=stock_response.json()['Time Series (Daily)']
stock_response.raise_for_status()
stock_data_list=[value for (key,value) in stock_data.items()]

yesterday_stock_data=stock_data_list[0]
yesterday_stock_data_close=yesterday_stock_data['4. close']

day_before_yesterday_stock_data=stock_data_list[1]
day_before_yesterday_stock_data_close=day_before_yesterday_stock_data['4. close']

print(yesterday_stock_data_close)
print(day_before_yesterday_stock_data_close)

positive_difference=float(yesterday_stock_data_close)-float(day_before_yesterday_stock_data_close)
print(positive_difference)

marker=None
if positive_difference>0:
    marker="🔼"
else:
    marker="🔽"


difference_percent=round((positive_difference/float(yesterday_stock_data_close))*100,1)
print(difference_percent)

if abs(difference_percent)>0.5:
    # print("get news")


    news_para={
        "apiKey":news_api_key,
        "qInTitle":COMPANY_NAME,
    }
    news_respose=requests.get(url=NEWS_ENDPOINT,params=news_para)
    news_data=news_respose.json()

    articles=news_data['articles']
    three_articles=articles[:3]
    # print(three_articles)
    
    formatted_message=[f"Stock Name : {STOCK}:{marker}{difference_percent}.\nHeadline: {items['title']}. \nBrief: {items['description']}" for items in three_articles]
    # print(message)


client = Client(twilio_sid, twilio_auth)

for item in formatted_message:

    message = client.messages.create(
    body=item,
    from_='+12312254891',
    to='+919334462616'
    )

print(message.sid)


