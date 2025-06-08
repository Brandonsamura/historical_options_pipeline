import httpx
from .config import settings

async def fetch_options_data(symbol: str, target_date: str):
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "HISTORICAL_OPTIONS",
        "symbol": symbol,
        "date": target_date,
        "apikey": settings.alphavantage_api_key
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        response.raise_for_status()
        return response.json()
