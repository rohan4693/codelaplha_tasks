import yfinance as yf
import pandas as pd

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, ticker, shares, purchase_price=None):
        """Adds a stock to the portfolio.

        Args:
            ticker (str): Stock ticker symbol.
            shares (float): Number of shares owned.
            purchase_price (float, optional): Purchase price per share. Defaults to None.
        """

        if ticker not in self.portfolio:
            self.portfolio[ticker] = {'shares': shares}
            if purchase_price:
                self.portfolio[ticker]['purchase_price'] = purchase_price
        else:
            print(f"Stock '{ticker}' already exists in the portfolio. Update shares or price instead.")

    def remove_stock(self, ticker):
        """Removes a stock from the portfolio.

        Args:
            ticker (str): Stock ticker symbol.
        """

        if ticker in self.portfolio:
            del self.portfolio[ticker]
            print(f"Stock '{ticker}' removed from the portfolio.")
        else:
            print(f"Stock '{ticker}' not found in the portfolio.")

    def update_purchase_price(self, ticker, price):
        """Updates the purchase price of a stock in the portfolio.

        Args:
            ticker (str): Stock ticker symbol.
            price (float): New purchase price per share.
        """

        if ticker in self.portfolio:
            self.portfolio[ticker]['purchase_price'] = price
            print(f"Purchase price for '{ticker}' updated.")
        else:
            print(f"Stock '{ticker}' not found in the portfolio.")

    def get_current_prices(self):
        """Retrieves current prices for all stocks in the portfolio using yfinance.

        Returns:
            pandas.DataFrame: DataFrame containing current prices and additional data
        """

        tickers = self.portfolio.keys()
        if not tickers:
            print("No stocks in the portfolio to fetch prices.")
            return None

        try:
            df = yf.download(tickers)["Close"][-1:]  # Get latest closing prices
            df.rename(columns={'Close': 'Current Price'}, inplace=True)
            df['Ticker'] = df.index
            df['Shares'] = [self.portfolio[ticker]['shares'] for ticker in df['Ticker']]
            if any(purchase_price in self.portfolio[ticker] for ticker, purchase_price in self.portfolio.items()):
                df['Purchase Price'] = [self.portfolio[ticker].get('purchase_price') for ticker in df['Ticker']]
                df['Unrealized Gain/Loss'] = (df['Current Price'] - df['Purchase Price']) * df['Shares']
            return df
        except (yf.DownloadError, KeyError) as e:
            print(f"Error retrieving prices: {e}")
            return None

    def display_portfolio(self, df=None):
        """Displays a summary of the portfolio, including current prices (if available).

        Args:
            df (pandas.DataFrame, optional): A DataFrame containing portfolio data, typically
                                             from get_current_prices(). Defaults to None.
        """

        if not self.portfolio:
            print("Portfolio is empty.")
            return

        if df is None:
            print("Current prices not available. Fetch them using get_current_prices().")
        else:
            print(df.to_string())

if __name__ == "__main__":
    portfolio = StockPortfolio()

    # Example usage
    portfolio.add_stock("AAPL", 100, 150)
    portfolio.add_stock("GOOG", 50)
    portfolio.update_purchase_price("GOOG", 2000)
    portfolio.remove_stock("TSLA")  # Won't remove as it's not added

    current_prices_df = portfolio.get_current_prices()
    portfolio.display_portfolio(current_prices_df)





# Explanation:

# Clear Function Definitions: The code is well-structured with clear function definitions and docstrings explaining their purpose and parameters.
# Error Handling: The get_current_prices function gracefully handles potential errors like `yf.Download
