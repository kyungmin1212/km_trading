import uvicorn

from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from model import AlertMessage
from exchange import Binance
from utility import binance_ticker_to_symbol

app = FastAPI()

whitelist = ["52.89.214.238", "34.212.75.30", "54.218.53.128", "52.32.178.7", "127.0.0.1"]

@app.middleware('http')
async def settings_whitelist_middleware(request: Request, call_next):
    if request.client.host not in whitelist:
        msg = f"{request.client.host}는 접속이 거부되었습니다."
        print(msg)
        return JSONResponse(status_code=status.HTTP_403_FORBIDDEN, content=f"{request.client.host} Not Allowed")
    response = await call_next(request)
    return response

@app.post("/order")
async def order(alert_message: AlertMessage):
    print(alert_message)
    if alert_message.exchange == 'BINANCE':
        exchange = Binance()
        symbol = binance_ticker_to_symbol(alert_message.ticker)
        exchange.market_order(symbol,alert_message.side,alert_message.amount)

@app.get("/hi")
async def hi():
    return 'hi'


if __name__ == "__main__":
    uvicorn.run("main:app",host="0.0.0.0", port=8000 ,reload=True)