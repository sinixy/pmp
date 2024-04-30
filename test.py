import yfinance
from datetime import datetime


ticker = yfinance.Ticker('CAUD')
for news in ticker.get_news():
    print(datetime.fromtimestamp(news['providerPublishTime']).isoformat(), news['title'])