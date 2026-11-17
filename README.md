# Real-Time Crypto Data Pipeline 🚀

## Project Overview
This is a Data Engineering project that extracts real-time cryptocurrency data from the CoinGecko API, transforms the data using Python, and loads it into a structured MySQL database.

## Tech Stack
* **Language:** Python
* **Libraries:** `requests`, `pymysql`
* **Database:** MySQL
* **API:** CoinGecko REST API

## Architecture Flow
1. **Extraction:** Python fetches live market data (JSON) of top cryptocurrencies via API.
2. **Transformation:** Data format standardization (e.g., converting ISO timestamps to MySQL DATETIME format).
3. **Loading:** The processed data is automatically inserted into a MySQL relational database using `pymysql` `DictCursor`.

## How to Run
1. Clone the repository.
2. Run the SQL script to create the `live_prices` table in MySQL.
3. Update database credentials in `pipeline.py`.
4. Execute `python pipeline.py` to start the ETL process.
