# historical_options_pipeline


This project is a Python application that fetches historical options data from the Alpha Vantage API, processes it, and stores it in a PostgreSQL database.

It is designed to run as a background task, fetching data at regular intervals. 

The application is structured to be modular, with separate modules for fetching data, processing it, and storing it in the database.

It uses FastAPI for the web framework and SQLAlchemy for database interactions.

Example payload can be [viewed here.](https://www.alphavantage.co/query?function=HISTORICAL_OPTIONS&symbol=IBM&apikey=demo)


## 1. Create a .env file:

Create a `.env` file in the root directory of the project and add the following environment variables:


```shell
cp .env_example .env
nano .env
```


```plaintext
ALPHAVANTAGE_API_KEY=your_key
DATABASE_URL=postgresql+asyncpg://user:pass@localhost/dbname
```

## 2. Install dependencies:

```python
poetry install
```


## 3. Run the app:

```python
poetry run start
```


