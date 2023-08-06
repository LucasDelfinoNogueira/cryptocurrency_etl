import requests

class CoinMarketCapAPI:
    def __init__(self, api_key, endpoint):
        """
        Initialize the CoinMarketCapAPI instance.

        Args:
            api_key (str): Your CoinMarketCap API key.
        """
        self.api_key = api_key
        self.base_url = f"https://{endpoint}/v1/"

    def get_data(self, symbol):
        """
        Fetch cryptocurrency data from the CoinMarketCap API.

        Args:
            symbol (str): Symbol of the cryptocurrency.

        Returns:
            dict: Dictionary containing cryptocurrency data.
        """
        endpoint = f"cryptocurrency/quotes/latest"
        params = {
            "symbol": symbol,
            "convert": "USD"
        }
        headers = {
            "X-CMC_PRO_API_KEY": self.api_key
        }

        response = requests.get(self.base_url + endpoint, params=params, headers=headers)
        data = response.json()

        return data["data"][symbol]
