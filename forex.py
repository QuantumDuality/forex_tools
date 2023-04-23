# import the package
from mt5linux import MetaTrader5
# connecto to the server
mt5 = MetaTrader5(
    host = '192.168.100.8',
    port = 18812
) 
# use as you learned from: https://www.mql5.com/en/docs/integration/python_metatrader5/
#mt5.initialize()
#mt5.terminal_info()
#rates = mt5.copy_rates_from_pos('VALE3',mt5.TIMEFRAME_M1,0,1000)
#print(rates)
# ...
# don't forget to shutdown
#mt5.shutdown()


# connect to the MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()

# set the currency pair symbol
symbol = "EURUSD"

# get the current market data for the symbol
market_data = mt5.symbol_info_tick(symbol)

# if the request was successful, print the open price
if market_data is not None:
    print("Open price for", symbol, "is:", market_data.bid)
else:
    print("Failed to get market data for", symbol)

# shut down the connection to the terminal
mt5.shutdown()

