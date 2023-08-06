class Coin:
    def __init__(self, symbol, name, price):
        """
        Initialize a Coin instance.

        Args:
            symbol (str): Symbol of the cryptocurrency.
            name (str): Name of the cryptocurrency.
            price (float): Price of the cryptocurrency.
        """
        self.symbol = symbol
        self.name = name
        self.price = price

    def __str__(self):
        """
        Return a string representation of the Coin object.

        Returns:
            str: String representation of the object.
        """
        return f"{self.name} ({self.symbol}): ${self.price:.2f}"
