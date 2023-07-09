from binanceAPI import testFunc , makeBuyOrder, makeSellOrder, getBalance


# In this model True == increase and False == decrease


def getModelBool():
    var = True
    print("Will increse:"+ var)
    return var

def trade(isGoingUp):
    #If the price is going to increase
    if isGoingUp ==  True:
        #Buy if there is Terher balance.
        tether_bal = getBalance('USDT')
        #Will buy all the BTC it can with avalible balance
        if tether_bal != 0:
            order  = makeBuyOrder(0,True)
            return order
        #No money to tether avalible so it will hold
        else:
            return "No Trade made."
    #If the price is going to decrease
    elif isGoingUp == False:
        #Checks if there is BTC balance
        bitcoinBal = getBalance('BTC')
        #Will sell all the BTC avalible
        if bitcoinBal != 0:
            order = makeSellOrder(0,True)
            return order
        else:
            "No Sell Made"


modelVal =  getModelBool()

trade(modelVal)