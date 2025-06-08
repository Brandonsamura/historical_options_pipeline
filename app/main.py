from fastapi import FastAPI
from database import init_db
from scheduler import start_scheduler
from schemas import OptionContractSchema
from models import OptionContract
from database import SessionLocal
from sqlalchemy import select

def main():
    print("Running historical options pipeline...")
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await init_db()
    start_scheduler()

@app.get("/contracts/{symbol}", response_model=list[OptionContractSchema])
async def get_contracts(symbol: str):
    async with SessionLocal() as session:
        result = await session.execute(select(OptionContract).where(OptionContract.symbol == symbol))
        return result.scalars().all()
