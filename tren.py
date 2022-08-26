'''# connect to google 
from pytrends.request import TrendReq
pytrends = TrendReq(hl='en-US', tz=600) 

# build payload
kw_list = ["kid named finger","better call saul","breaking bad","markiplier"] # list of keywords to get data 
pytrends.build_payload(kw_list)

#1 Interest over Time
data = pytrends.interest_over_time()
data = data.reset_index()

import plotly.express as px

fig = px.line(data, x="date", y=kw_list, title='Keyword Web Search Interest Over Time')
fig.show()

hist_int = pytrends.get_historical_interest(kw_list, year_start=2021, month_start=9, day_start=1, hour_start=0, year_end=2021, month_end=9, day_end=30, hour_end=0, cat=0, sleep=0)
hist_int.head(10)

by_region = pytrends.interest_by_region(resolution='COUNTRY', inc_low_vol=True, inc_geo_code=False)
by_region.head(10) 


import pandas as pd                        
from pytrends.request import TrendReq
pytrend = TrendReq()

pytrend.build_payload(kw_list=['Taylor Swift'])# Interest by Region
df = pytrend.interest_by_region()
df.head(10)

df.reset_index().plot(x='geoName', y='Taylor Swift', figsize=(120, 10), kind ='bar')

from lib2to3 import pytree
from pytrends.request import TrendReq
import pandas as pd
from datetime import datetime, date, time

pytrend = TrendReq()
pytrend.build_payload(kw_list=['vlog','blog'], timeframe='today 4-y' , geo ='ID')

Interest_over_time df = pytrend.interest_over_time()
print(interest_over_time_df.head())'''

from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates

plt.style.use('ggplot')

pytrends = TrendReq(hl='en-US')

all_keywords = ['kid named finger', 'ben']
keywords = []

timeframes = ['today 5-y', 'today 12-m',
              'today 3-m', 'today 1-m']
cat = '0'
geo = ''
gprop = ''

countries = ['australia', 'united_states']

#Part 1 - Google trends analysis

def check_trends():
    pytrends.build_payload(keywords,
                           cat,
                           timeframes[0],
                           geo,
                           gprop)

    data = pytrends.interest_over_time()
    mean = round(data.mean(),2)
    avg = round(data[kw][-52:].mean(),2) #Last year average
    avg2 = round(data[kw][:52].mean(),2) #Yearly average of 5 years ago.
    trend = round(((avg/mean[kw])-1)*100,2)
    trend2 = round(((avg/avg2)-1)*100,2)
    print('The average 5 years interest of ' + kw + ' was ' + str(mean[kw]) + '.')
    print('The last year interest of ' + kw + ' compared to the last 5 years'
          + ' has changed by ' + str(trend)+ '%.')
    #Stable trend
    if mean[kw] > 75 and abs(trend) <= 5:
        print('The interest for ' + kw + ' is stable in the last 5 years.')
    elif mean[kw] > 75 and trend > 5:
        print('The interest for ' + kw + ' is stable and increasing in the last 5 years.')
    elif mean[kw] > 75 and trend < -5:
        print('The interest for ' + kw + ' is stable and decreasing in the last 5 years.')

    #Relatively stable
    elif mean[kw] > 60 and abs(trend) <= 15:
        print('The interest for ' + kw + ' is relatively stable in the last 5 years.')
    elif mean[kw] > 60 and trend > 15:
        print('The interest for ' + kw + ' is relatively stable and increasing in the last 5 years.')
    elif mean[kw] > 60 and trend < -15:
        print('The interest for ' + kw + ' is relatively stable and decreasing in the last 5 years.')

    #Seasonal
    elif mean[kw] > 20 and abs(trend) <= 15:
        print('The interest for ' + kw + ' is seasonal.')

    #New keyword
    elif mean[kw] > 20 and trend > 15:
        print('The interest for ' + kw + ' is trending.')

    #Declining keyword
    elif mean[kw] > 20 and trend < -15:
        print('The interest for ' + kw + ' is significantly decreasing.')

    #Cyclinal
    elif mean[kw] > 5 and abs(trend) <= 15:
        print('The interest for ' + kw + ' is cyclical.')

    #New
    elif mean[kw] > 0 and trend > 15:
        print('The interest for ' + kw + ' is new and trending.')

    #Declining
    elif mean[kw] > 0 and trend < -15:
        print('The interest for ' + kw + ' is declining and not comparable to its peak.')

    #Other
    else:
        print('This is something to be checked.')

    #Comparison last year vs. 5 years ago
    if avg2 == 0:
        print('This didn\'t exist 5 years ago.')
    elif trend2 > 15:
        print('The last year interest is quite higher compared to 5 years ago.'
              + ' It has increased by ' + str(trend2)+'%.')
    elif trend2 < -15:
        print('The last year interest is quite lower compared to 5 years ago.'
              + ' It has decreased by ' + str(trend2)+'%.')
    else:
        print('The last year interest is comparable to 5 years ago. '
              + ' It has changed by ' + str(trend2)+'%.')
    
    print('')

for kw in all_keywords:
    keywords.append(kw)
    check_trends()
    keywords.pop()

#Part 5 - Trending searches
def trending_searches(country):
    data = pytrends.trending_searches(country)
    print(data.head(5))

for country in countries:
    print(country)
    print('')
    trending_searches(country)
    print('')