# historical_options_pipeline


# Historical Options Pipeline


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


