import requests
from twilio.rest import Client
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='72576d178c2f44f0a04211486390b677')

alphavantage_api= "Your key"

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_parameteres = {"function":"TIME_SERIES_DAILY", "symbol": STOCK, "apikey": alphavantage_api}

response = requests.get(STOCK_ENDPOINT, stock_parameteres)
data = response.json()
previous_day = float(data["Time Series (Daily)"]['2021-05-17']['4. close'])
current_day = float(data["Time Series (Daily)"]['2021-05-18']['4. close'])
print(previous_day)
print(current_day)

print(previous_day - current_day)

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 



## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.

#----------------twilio ----------
# client = Client(account_sid, auth_token)
# message = client.messages.create(body="It is going to rain today hey ☂️.", from_='+19032010801', to='+5521969920545')
# print(message.status)



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

