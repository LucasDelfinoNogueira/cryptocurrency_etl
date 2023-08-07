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

    ```
    API_KEY=your_actual_api_key_here
    ENDPOINT=sandbox-api.coinmarketcap.com
    CRYPTO_LIST=BTC,ETH,LTC,XRP
    DB_HOST=mysql
    DB_USER=your_db_username
    DB_PASSWORD=your_db_password
    DB_NAME=crypto_db
    DB_ROOT_PASSWORD=your_db_root_password
    ```

    For the purpose os this project, it was used the sandbox endpoint and api key provided by CoinMarketCap. This sandbox environment is used for testing purpose, since it has mock data. If you want to use the mock data, keep the API_KEY        and ENDPOINT variables in .env file the way they are:

   ```
   API_KEY=b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c
   ENDPOINT=sandbox-api.coinmarketcap.com
   ```

   If you want to get real data, you will need to create an account in CoinMarketCap developers page to generate your personal API_KEY and also change the ENDPOINT value to `pro-api.coinmarketcap.com`.

   ```
   API_KEY=your_actual_api_key_here
   ENDPOINT=pro-api.coinmarketcap.com
   ```

   To set which Cryptocoin you want to get the data, just fill the comma sepparated list with all the desired crypto symbol.

   ```
   CRYPTO_LIST=BTC,ETH,LTC,XRP
   ```

5. Build and start the Docker containers:

    ```bash
    docker-compose up --build

## How it Works

* The coinmarketcap_api.py module handles communication with the CoinMarketCap API to fetch cryptocurrency data.
* The crypto_classes.py module defines the Coin class to represent cryptocurrency data.
* The crypto_database.py module defines the CryptoDatabase class for interacting with the MySQL database.
* The main.py script combines the API communication, data processing, and database interactions.
* The application is scheduled to run the data fetching process every minute using the schedule library.
* MySQL data is persisted in a Docker Volume

## Accessing the Output

   To access your data, I would recomend a visual desktop application like DBeaver. Your database will be exposed by port 3306. Fill with your credentials and you should be good to go.

   ![test_cadastra_1](https://github.com/LucasDelfinoNogueira/cryptocurrency_etl/assets/140350700/ead42749-e93d-4faf-8976-9691529ac6de)

   ![test_cadastra_2](https://github.com/LucasDelfinoNogueira/cryptocurrency_etl/assets/140350700/4d95a5a7-4505-41d7-a052-f94cca9a7448)


   

## Logs

Logs are stored in the app.log file in the logs directory. This file provides information about the data fetching process, database interactions, and any errors encountered.
