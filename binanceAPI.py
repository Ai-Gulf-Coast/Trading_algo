from dotenv import load_dotenv
load_dotenv()

import os
from binance.client import Client
from binance.helpers import round_step_size


api_key = os.environ.get('BINANCE_API_KEY_TEST')
api_secret = os.environ.get('BINANCE_API_SECRET_TEST')
client = Client(api_key,api_secret, tld='us')

def getBalance(symbol):
    balance = float(client.get_asset_balance(asset=symbol)['free'])
    return balance

def makeBuyOrder(amount, all):
    btc_quantity = 0
    btc_price = client.get_symbol_ticker(symbol="BTCUSDT")['price']
    if all == True:
        usdt_balance = float(client.get_asset_balance(asset='USDT')['free'])
        btc_quantity = usdt_balance / float(btc_price)
    elif all == False:
        btc_quantity = amount / float(btc_price)
    else:
        return "False all value, needs to be bool"
    tick_size = 0.00001
    btc_quantity = round_step_size(btc_quantity, tick_size)
    print(btc_quantity)

    order = client.order_market_buy(
            symbol='BTCUSDT',
            quantity=btc_quantity
        )
    return order
    


def makeSellOrder(amount, all):
    btc_quantity = 0
    if all == True:
        btc_balance = float(client.get_asset_balance(asset='BTC')['free'])
        btc_quantity = btc_balance
    elif all == False:
        btc_quantity = amount
    else:
        return "False all value, needs to be bool"
    tick_size = 0.00001
    btc_quantity = round_step_size(btc_quantity, tick_size)

    order = client.order_market_sell(
            symbol='BTCUSDT',
            quantity=btc_quantity
        )
    return order

def testFunc(test):
    print(test)

#Buys $30 worth of BTC
#makeBuyOrder(30,False)

#Sells 0.001 of BTC
#makeSellOrder(0.001,False)

#Buys 100% of BTC that can with tether in account
#makeBuyOrder(0,True)

#Sells all of BTC available 
#makeSellOrder(0,True)
