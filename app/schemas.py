from pydantic import BaseModel
from datetime import date

class OptionContractSchema(BaseModel):
    contractID: str
    symbol: str
    expiration: date
    strike: float
    type: str
    last: float
    mark: float
    bid: float
    ask: float
    volume: int
    open_interest: int
    date: date
    implied_volatility: float
    delta: float
    gamma: float
    theta: float
    vega: float
    rho: float

    class Config:
        from_attributes = True
