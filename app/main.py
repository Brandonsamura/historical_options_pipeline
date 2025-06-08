from app.database import init_db, SessionLocal
from app.scheduler import start_scheduler
from app.schemas import OptionContractSchema
from app.models import OptionContract
from sqlalchemy import select
from fastapi import FastAPI

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
