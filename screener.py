import pandas as pd
import requests
from config import HEADERS


url = 'https://finviz.com/screener.ashx?v=111&f=geo_usa&o=-change&r={r}'

screener = pd.DataFrame()
for r in range(3):
    content = requests.get(url.format(r=r*20 + 1), headers=HEADERS).content
    screener = pd.concat([
        screener,
        pd.read_html(content, attrs={'class': 'screener_table'}, skiprows=1, flavor='bs4', na_values='-')[0]
    ], axis=0, ignore_index=True)
    
print(screener)