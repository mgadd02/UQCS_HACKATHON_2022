from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates

plt.style.use('ggplot')

pytrends = TrendReq(hl='en-US')

timeframes = ['today 5-y', 'today 12-m',
              'today 3-m', 'today 1-m']
cat = '0'
geo = ''
gprop = ''

def check_trends(topic):
    mean = 0.0
    avg = 0.0
    avg2 = 0.0
    trend = 0.0
    trend2 = 0.0

    for kw in topic:
        pytrends.build_payload([kw],
                        cat,
                        timeframes[0],
                        geo,
                        gprop)

        data = pytrends.interest_over_time()

        mean += round(data.mean(),2)[kw]
        avg += round(data[kw][-52:].mean(),2) #Last year average
        avg2 += round(data[kw][:52].mean(),2) #Yearly average of 5 years ago.
        trend += round(((avg/mean)-1)*100,2)
        trend2 += round(((avg/avg2)-1)*100,2)

    amount = len(topic)
    mean /= amount
    avg /= amount
    avg2 /= amount
    trend /= amount
    trend2 /= amount
    
    print('The average 5 years interest of ' + str(topic) + ' was ' + str(mean) + '.')
    print('The last year interest of ' + str(topic) + ' compared to the last 5 years'
          + ' has changed by ' + str(trend)+ '%.')
    #Stable trend
    if mean > 75 and abs(trend) <= 5:
        print('The interest for ' + str(topic) + ' is stable in the last 5 years.')
    elif mean > 75 and trend > 5:
        print('The interest for ' + str(topic) + ' is stable and increasing in the last 5 years.')
    elif mean > 75 and trend < -5:
        print('The interest for ' + str(topic) + ' is stable and decreasing in the last 5 years.')

    #Relatively stable
    elif mean > 60 and abs(trend) <= 15:
        print('The interest for ' + str(topic) + ' is relatively stable in the last 5 years.')
    elif mean > 60 and trend > 15:
        print('The interest for ' + str(topic) + ' is relatively stable and increasing in the last 5 years.')
    elif mean > 60 and trend < -15:
        print('The interest for ' + str(topic) + ' is relatively stable and decreasing in the last 5 years.')

    #Seasonal
    elif mean > 20 and abs(trend) <= 15:
        print('The interest for ' + str(topic) + ' is seasonal.')

    #New keyword
    elif mean > 20 and trend > 15:
        print('The interest for ' + str(topic) + ' is trending.')

    #Declining keyword
    elif mean > 20 and trend < -15:
        print('The interest for ' + str(topic) + ' is significantly decreasing.')

    #Cyclinal
    elif mean > 5 and abs(trend) <= 15:
        print('The interest for ' + str(topic) + ' is cyclical.')

    #New
    elif mean > 0 and trend > 15:
        print('The interest for ' + str(topic) + ' is new and trending.')

    #Declining
    elif mean > 0 and trend < -15:
        print('The interest for ' + str(topic) + ' is declining and not comparable to its peak.')

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

def trends(all_topics):
    for topic in all_topics:
        check_trends(topic)

def main():
    all_topics = [['kid named finger'], ['market fryer'], ['fortnite battle pass'], ['joe mama'], ['joe', 'mama']]
    trends(all_topics)

if __name__ == "__main__":
    main()