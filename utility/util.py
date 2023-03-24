from utility import send_message

def binance_ticker_to_symbol(ticker):
    if ticker.endswith('USDT') or ticker.endswith('USDTPERP'):
        ticker = ticker.replace('USDT','')
        ticker = ticker.replace('PERP','')
        return ticker+'/'+'USDT'
    else:
        send_message('잘못된 ticker입니다.')