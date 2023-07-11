import random
import pandas as pd
import numpy as np

def mark_result():
    # Generate a random number between 0 and 1
    random_number = random.random()
    #change for model accurccy
    if random_number <= 0.55:
        return "CORRECT"
    else:
        return "INCORRECT"
priceData =   pd.read_csv("BITSTAMP_BTCUSD, 5.2.csv")
correct = []
for i in range(len(priceData)):
    open = priceData['open'][i]
    close = priceData['close'][i]
    if(open <= close):
        correct.append('BUY')
    else:
        correct.append('SELL')

priceData['correct'] = correct


totals = []
#amount of test runs ran with the same data number
days = 100
for i in range(days):
    #starting amount per day
    tether = 100
    #bitcoin amount
    BTCP = 0
    numOfFiveMinInterval = 2080
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


    if(BTCP != 0):
        tether = priceData['close'][numOfFiveMinInterval] *BTCP
    totals.append(tether)


def Average(lst):
    return sum(lst) / len(lst)

average = Average(totals)
 
# Printing average of the list
print("Average of the list =", round(average, 2))


