import mysql.connector

class CryptoDatabase:
    def __init__(self, host, user, password, database):
        """
        Initialize the CryptoDatabase instance.

        Args:
            host (str): Database host address.
            user (str): Database username.
            password (str): Database password.
            database (str): Database name.
        """
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.db.cursor()

    def create_table(self, symbol):
        """
        Create a table for a cryptocurrency if it doesn't exist.

        Args:
            symbol (str): Symbol of the cryptocurrency.
        """
        query = f"""
        CREATE TABLE IF NOT EXISTS {symbol} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            price FLOAT
        )
        """
        self.cursor.execute(query)
        self.db.commit()

    def insert_data(self, symbol, name, price):
        """
        Insert cryptocurrency data into the appropriate table.

        Args:
            symbol (str): Symbol of the cryptocurrency.
            name (str): Name of the cryptocurrency.
            price (float): Price of the cryptocurrency.
        """
        query = f"""
        INSERT INTO {symbol} (name, price)
        VALUES (%s, %s)
        """
        values = (name, price)
        self.cursor.execute(query, values)
        self.db.commit()

    def close_connection(self):
        """
        Close the database connection and cursor.
        """
        self.cursor.close()
        self.db.close()
