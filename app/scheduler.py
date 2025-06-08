from apscheduler.schedulers.asyncio import AsyncIOScheduler
from app.database import SessionLocal
from app.ingestion import fetch_options_data
from app.models import OptionContract
from datetime import datetime

async def ingest_and_store(symbol: str, target_date: str):
    data = await fetch_options_data(symbol, target_date)
    async with SessionLocal() as session:
        for item in data["data"]:
            contract = OptionContract(
                contractID=item["contractID"],
                symbol=item["symbol"],
                expiration=datetime.strptime(item["expiration"], "%Y-%m-%d").date(),
                strike=float(item["strike"]),
                type=item["type"],
                last=float(item["last"]),
                mark=float(item["mark"]),
                bid=float(item["bid"]),
                ask=float(item["ask"]),
                volume=int(item["volume"]),
                open_interest=int(item["open_interest"]),
                date=datetime.strptime(item["date"], "%Y-%m-%d").date(),
                implied_volatility=float(item["implied_volatility"]),
                delta=float(item["delta"]),
                gamma=float(item["gamma"]),
                theta=float(item["theta"]),
                vega=float(item["vega"]),
                rho=float(item["rho"]),
            )
            session.add(contract)
        await session.commit()

def start_scheduler():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(
        ingest_and_store,
        trigger='cron',
        hour=18,
        minute=0,
        args=["PLTR", datetime.now().strftime("%Y-%m-%d")]
    )
    scheduler.start()
