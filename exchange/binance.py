import ccxt
from utility import settings, send_message

class Binance:
    def __init__(self):
        key = settings.BINANCE_KEY
        secret = settings.BINANCE_SECRET
        self.future = ccxt.binanceusdm({
            'apiKey': key,
            'secret': secret,
            'enableRateLimit': True
        })
        
    def market_order(self, symbol: str, side: str, amount: float):
        order = self.future.create_order(symbol, 'MARKET', side, amount)
        send_message(f'{symbol}, MARKET, 주문방향 : {side}, 체결가격 : {order["price"]}, 주문수량 : {order["amount"]}')