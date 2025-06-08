from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy import String, Float, Integer, Date

class Base(DeclarativeBase):
    pass

class OptionContract(Base):
    __tablename__ = "option_contracts"

    contractID = mapped_column(String, primary_key=True)
    symbol = mapped_column(String)
    expiration = mapped_column(Date)
    strike = mapped_column(Float)
    type = mapped_column(String)
    last = mapped_column(Float)
    mark = mapped_column(Float)
    bid = mapped_column(Float)
    ask = mapped_column(Float)
    volume = mapped_column(Integer)
    open_interest = mapped_column(Integer)
    date = mapped_column(Date)
    implied_volatility = mapped_column(Float)
    delta = mapped_column(Float)
    gamma = mapped_column(Float)
    theta = mapped_column(Float)
    vega = mapped_column(Float)
    rho = mapped_column(Float)
