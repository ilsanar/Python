import requests
import os
import datetime as dt
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla"


today=dt.date.today()
if today.weekday() == 0:  
    yesterday = today - dt.timedelta(days=3)
else:
    yesterday = today - dt.timedelta(days=1)
    
day_before_yesterday = str(yesterday - dt.timedelta(days=1))
yesterday = str(yesterday)


def get_stock(company):
    


    # print(yesterday,day_before_yesterday)
    ## STEP 1: Use https://www.alphavantage.co
    # When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
    url = "https://www.alphavantage.co/query"
    parameters = {
        "function":"TIME_SERIES_DAILY",
        "symbol":company,
        "outputsize":"compact",
        "apikey":os.environ["AV_API"]
    }

    data = requests.get(url=url,params=parameters)
    data.raise_for_status()
    print(data.json())
    # yesterday_close = float(data.json()['Time Series (Daily)'][yesterday]["4. close"])
    # day_before_yesterday_close = float(data.json()["Time Series (Daily)"][day_before_yesterday]["4. close"])
    # print(yesterday_close ,day_before_yesterday_close)
    # delta = yesterday_close - day_before_yesterday_close
    # delta_pcent = delta / day_before_yesterday_close
    
    return 0.02


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
def get_news(company):
    url="https://newsapi.org/v2/everything"
    parameters = {
        "apiKey":os.environ["OPEN_NEWS_API"],
        "q":company,
        "searchIn":["title","description"],
        "from":str(day_before_yesterday),
        "to":str(today),
        "language":["en","pl"]    
    }

    data = requests.get(url=url, params=parameters)
    data.raise_for_status()
    articles=data.json()["articles"][0:3]
    # print(data.json()["articles"])
    # print(articles)
    return articles


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
def send_msg(company,chng_rate):
    account_sid = os.environ["TWILIO_SID"]
    auth_token = os.environ["TWILIO_AUTH_TOKEN"]
    articles = get_news(company)
    if chng_rate>0:
        change_indicator="🔺"
    else:
        change_indicator = "🔻"
        
    articles_formatted= [f"{company} {change_indicator} {int(chng_rate*100)}%\nHeadline: {article['title']}\n Brief:{article['description']}\n" for article in articles]
    for article in articles_formatted:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
        body=article,
        from_="whatsapp:+14000000000",
        to="whatsapp:+31000000000",
        )
        print(message.status)

chng_rate = get_stock(STOCK)
abs_chng_rate = abs(chng_rate)   
if abs_chng_rate >= 0.02:
    send_msg(company=STOCK,chng_rate=chng_rate)










