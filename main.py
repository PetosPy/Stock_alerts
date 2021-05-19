import requests
from twilio.rest import Client
from newsapi import NewsApiClient
import math 
import os

account_sid = os.environ.get("TWILIO_ACC_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
twilio_number = os.environ.get("TWILIO_NUMBER")
my_number = os.environ.get("MY_NUMBER")

alphavantage_api = os.environ.get("ALPHAVANTAGE_API")
news_api = os.environ.get("NEWS_API")

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_parameteres = {"function":"TIME_SERIES_DAILY", "symbol": STOCK, "apikey": alphavantage_api}

response = requests.get(STOCK_ENDPOINT, stock_parameteres)
response.raise_for_status()
data = response.json()
previous_day = float(data["Time Series (Daily)"]['2021-05-17']['4. close'])
current_day = float(data["Time Series (Daily)"]['2021-05-18']['4. close'])



def sender(*messages):
	for x in messages:
		client = Client(account_sid, auth_token)
		message = client.messages.create(body=f"{x}", from_=twilio_number, to=my_number)
		print(message.status)


difference = current_day - previous_day
increased = round((100 / current_day) * difference) 
	
if increased > 5:
	news_parameteres = {"q": COMPANY_NAME, "from": "2021-05-18", "to" : "2021-05-18", "sortBy": "popularity", "apiKey": news_api }
	news_response = requests.get(NEWS_ENDPOINT, news_parameteres)
	news_response.raise_for_status()
	data = news_response.json()


	title_1 = data["articles"][0]["title"]
	descr_1 = data["articles"][0]["description"]
	article_1 = f"{title_1}\n\n{descr_1}"

	title_2 = data["articles"][1]["title"]
	descr_2 = data["articles"][1]["description"]
	article_2 = f"{title_2}\n\n{descr_2}"

	title_3 = data["articles"][2]["title"]
	descr_3 = data["articles"][2]["description"]
	article_3 = f"{title_3}\n\n{descr_3}"

	sender(article_1, article_2, article_3)

else:
	print("Not much has changed")

## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.

#----------------twilio ----------




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

