# Cryptocurrency Data Collection Application

This application fetches cryptocurrency data from the CoinMarketCap API and saves it to a MySQL database. It utilizes object-oriented programming principles, Docker, and scheduled data fetching to provide an automated way of collecting and storing cryptocurrency data.

## Prerequisites

Before running the application, ensure you have the following:

- Python 3.8 or higher installed.
- Docker and Docker Compose installed.
- CoinMarketCap API key (sign up at https://coinmarketcap.com/api/).
- MySQL database credentials.

## Setup

1. Clone this repository to your local machine.

2. Navigate to the project directory:

   ```bash
   cd cryptocurrency_etl

3. Create a .env file in the project directory and add your API key and database credentials:

    ```bash
    API_KEY=your_actual_api_key_here
    ENDPOINT=sandbox-api.coinmarketcap.com
    CRYPTO_LIST=BTC,ETH,LTC,XRP
    DB_HOST=mysql
    DB_USER=your_db_username
    DB_PASSWORD=your_db_password
    DB_NAME=crypto_db
    DB_ROOT_PASSWORD=your_db_root_password

4. Build and start the Docker containers:

    ```
    docker-compose up --build

## How it Works

* The coinmarketcap_api.py module handles communication with the CoinMarketCap API to fetch cryptocurrency data.
* The crypto_classes.py module defines the Coin class to represent cryptocurrency data.
* The crypto_database.py module defines the CryptoDatabase class for interacting with the MySQL database.
* The main.py script combines the API communication, data processing, and database interactions.
* The application is scheduled to run the data fetching process every minute using the schedule library.