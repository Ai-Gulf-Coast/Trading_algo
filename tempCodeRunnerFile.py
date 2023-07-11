import random
import pandas as pd
import numpy as np
tether = 1000
BTCP = 0
def mark_result():
    # Generate a random number between 0 and 1
    random_number = random.random()
    if random_number <= 0.6:
        return "CORRECT"
    else:
        return "INCORRECT"
priceData =   pd.read_csv("BITSTAMP_BTCUSD, 5.csv")
correct = []
for i in range(len(priceData)):
    open = priceData['open'][i]
    close = priceData['close'][i]
    if(open <= close):
        correct.append('BUY')
    else:
        correct.append('SELL')

priceData['correct'] = correct


numOfFiveMinInterval = 288
for i in range(numOfFiveMinInterval):
    check = mark_result()
    if(check == "CORRECT"):
        if(priceData['correct'][i] == 'BUY'):
            if(tether != 0):
                BTCP = tether / priceData['open'][i]
                tether = 0
        if(priceData['correct'][i] == "SELL"):
            if(BTCP!= 0):
                tether = priceData['open'][i] * BTCP
                BTCP = 0


    else:
        if(priceData['correct'][i] == 'BUY'):
            if(BTCP!= 0):
                tether = priceData['open'][i] * BTCP
                BTCP = 0
        if(priceData['correct'][i] == "SELL"):
            if(tether != 0):
                BTCP = tether / priceData['open'][i]
                tether = 0




print(tether)
print(BTCP)