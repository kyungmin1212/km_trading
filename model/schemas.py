from pydantic import BaseModel, BaseSettings

class Settings(BaseSettings):
    BINANCE_KEY: str
    BINANCE_SECRET: str
    DISCORD_WEBHOOK_URL: str | None = None
    
    class Config:
        env_file = '.env'
        env_file_encoding = "utf-8"
        

class AlertMessage(BaseModel):
    exchange: str
    ticker: str
    side: str
    amount: float