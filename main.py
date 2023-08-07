import os
import time
import logging
import schedule
from dotenv import load_dotenv
from coinmarketcap_api import CoinMarketCapAPI
from crypto_classes import Coin
from crypto_database import CryptoDatabase

def get_crypto_data(symbol_list, api):
    """
    Fetch cryptocurrency data for a list of symbols.

    Args:
        symbol_list (list): List of cryptocurrency symbols.
        api (CoinMarketCapAPI): Instance of CoinMarketCapAPI.

    Returns:
        list: List of Coin objects containing cryptocurrency data.
    """
    crypto_data = []
    for symbol in symbol_list:
        data = api.get_data(symbol)
        name = data['name']
        price = data['quote']['USD']['price']
        crypto_data.append(Coin(symbol, name, price))
    return crypto_data

def main():
    """
    Main function to fetch cryptocurrency data and save to the database.
    """
    load_dotenv()
    api_key = os.getenv("API_KEY")
    endpoint=os.getenv("ENDPOINT")
    symbol_list = os.getenv("CRYPTO_LIST").split(",")
    db_host = os.getenv("DB_HOST")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_name = os.getenv("DB_NAME")

    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        filename="logs/app.log",
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    logger = logging.getLogger(__name__)

    api = CoinMarketCapAPI(api_key, endpoint)
    crypto_data = get_crypto_data(symbol_list, api)

    db = None
    max_retries = 10
    for retry in range(max_retries):
        try:
            db = CryptoDatabase(db_host, db_user, db_password, db_name)
            break  # Connection successful, exit the retry loop
        except mysql.connector.Error:
            logger.warning(f"Connection attempt {retry + 1} failed. Retrying in 5 seconds...")
            time.sleep(5)
    
    if db is None:
        logger.error("Unable to establish a connection to the database. Exiting.")
        return
    
    for crypto in crypto_data:
        db.create_table(crypto.symbol)
        db.insert_data(crypto.symbol, crypto.name, crypto.price)
        logging.info(f"Saved data for {crypto.name} ({crypto.symbol})")

    db.close_connection()

if __name__ == "__main__":

    # Schedule running the main function every minute
    schedule.every(1).minutes.do(main)

    # Run the scheduling loop
    while True:
        schedule.run_pending()
        time.sleep(1)
