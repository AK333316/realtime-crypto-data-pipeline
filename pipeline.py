import requests
import pymysql
from datetime import datetime


# 1. CoinGecko API-la irunthu Data Fetch Pandrathu
def fetch_crypto_data():
    # CoinGecko markets endpoint
    url = 'https://api.coingecko.com/api/v3/coins/markets'
    params = {
        'vs_currency': 'usd',
        'ids': 'bitcoin,ethereum,solana,ripple,cardano'  # Ungaluku thevaiyana coins
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print("The data could not be fetched from the API!")
        return []


# 2. PyMySQL moolama Database-la Data Insert Pandrathu
def insert_into_db(crypto_data):
    # Unga MySQL details-a inga mathikonga
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='root',  # Unga MySQL password podunga
        database='crypto_data',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        with connection.cursor() as cursor:
            for coin in crypto_data:
                # API tharra time format-a (ISO) MySQL-ku etha mari mathurathu
                raw_time = coin.get('last_updated')
                if raw_time:
                    formatted_time = raw_time.replace('T', ' ')[:19]
                else:
                    formatted_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                # Database-la insert pandra query
                sql = """
                    INSERT INTO live_prices (coin_id, coin_name, current_price_usd, market_cap, last_updated)
                    VALUES (%s, %s, %s, %s, %s)
                """
                cursor.execute(sql, (
                    coin['id'],
                    coin['name'],
                    coin['current_price'],
                    coin['market_cap'],
                    formatted_time
                ))

            # Changes-a save pandrathu
            connection.commit()
            print(f"{len(crypto_data)} the coins data has been inserted into the database successfully!")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        connection.close()


# Script execution inga thaan start aagum
if __name__ == "__main__":
    print("The API is fetch from the CoinGecko...")
    data = fetch_crypto_data()

    if data:
        print("inserting into database in Mysql...")
        insert_into_db(data)