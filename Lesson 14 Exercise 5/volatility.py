import pandas as pd
import numpy as np

def get_most_volatile(prices):
    """Return the ticker symbol for the most volatile stock.
    
    Parameters
    ----------
    prices : pandas.DataFrame
        a pandas.DataFrame object with columns: ['ticker', 'date', 'price']
    
    Returns
    -------
    ticker : string
        ticker symbol for the most volatile stock
    """
    
    prices = prices.set_index('date')

    stock_return_volatility = []

    for ticker in prices.ticker.unique():
        prices_for_ticker = prices[prices['ticker'] == ticker]['price']
        log_return = np.log(prices_for_ticker) - np.log(prices_for_ticker.shift(1))
        stock_return_volatility.append(log_return.std())

    volatility_series = pd.Series(stock_return_volatility, index=prices.ticker.unique())

    return volatility_series.idxmax()


def test_run(filename='prices.csv'):
    """Test run get_most_volatile() with stock prices from a file."""
    prices = pd.read_csv(filename, parse_dates=['date'])
    print("Most volatile stock: {}".format(get_most_volatile(prices)))


if __name__ == '__main__':
    test_run()
