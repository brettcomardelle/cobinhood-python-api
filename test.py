from cobinhood import Cobinhood

cobinhood = Cobinhood()

out = cobinhood.getOrderBook('BTC-USD')
print(out)

