import pandas as pd
import yfinance as yf
import math

# List of S&P 500 tickers
df = pd.read_csv('/home/madlad_/local/GitHub/equal_weighted_portfolio/starter_sp500_tickers.csv')
tickers1 = df['Ticker'].tolist()

tickers = [
    'MMM', 'AOS', 'ABT', 'ABBV', 'ACN', 'ADBE', 'AMD', 'AES', 'AFL', 'APD', 'ABNB', 'AKAM', 'ALB', 'ARE', 'ALGN', 'ALLE', 
    'LNT', 'ALL', 'GOOG', 'GOOGL', 'MO', 'AMZN', 'AMCR', 'AMD', 'AIG', 'AMT', 'AWK', 'AMP', 'ABC', 'AME', 'AMGN', 'APH', 'ADI', 'ANSS', 'ANTM', 
    'AON', 'APA', 'AAPL', 'AMAT', 'APTV', 'ADM', 'ARNC', 'ARW', 'ASML', 'AVB', 'AVY', 'BKR', 'BALL', 'BAC', 'BAX', 'BD', 'BRK', 'BBY', 'BIO', 
    'BIIB', 'BLK', 'BWA', 'BXP', 'BSX', 'BMY', 'AVGO', 'BR', 'BF', 'CHRW', 'COF', 'CHTR', 'CVX', 'CMG', 'CB', 'CHD', 'CI', 'CINF', 'CTAS', 'CSCO', 
    'CFG', 'CTXS', 'CLX', 'CME', 'CMS', 'KO', 'CTSH', 'CL', 'CMCSA', 'CMA', 'CAG', 'COP', 'ED', 'STZ', 'CPRT', 'GLW', 'COST', 'COTY', 'CCI', 'CSX'
]

# Investment amount
investment_amount = 1000000000  # $1 billion

# Download data in chunks to avoid rate limiting
chunk_size = 50
data = pd.DataFrame()

for i in range(0, len(tickers), chunk_size):
    chunk_tickers = tickers[i:i + chunk_size]
    try:
        chunk_data = yf.download(chunk_tickers, start="2020-01-01", end="2024-01-01", group_by='ticker', timeout=30)
        data = pd.concat([data, chunk_data], axis=1)
    except Exception as e:
        print(f"Error downloading data for tickers {chunk_tickers}: {str(e)}")

# Create portfolio
try:
    latest_prices = data.xs('Close', level=1, axis=1).iloc[-1]
    latest_prices = latest_prices.dropna()
    
    portfolio = pd.DataFrame(index=latest_prices.index)
    portfolio['Ticker'] = portfolio.index
    portfolio['Price (per share)'] = latest_prices.values
    
    # Calculate portfolio metrics
    num_stocks = len(portfolio)
    portfolio['Portfolio Weight'] = 1.0 / num_stocks
    portfolio['Allocation'] = investment_amount * portfolio['Portfolio Weight']
    portfolio['Shares to Buy'] = portfolio['Allocation'] / portfolio['Price (per share)']
    portfolio['Shares to Buy'] = portfolio['Shares to Buy'].apply(lambda x: math.floor(x))
    portfolio['Total Spent'] = portfolio['Shares to Buy'] * portfolio['Price (per share)']
    
    # Save to Excel
    portfolio.to_excel('sp500_portfolio.xlsx', index=False)
    print("Portfolio saved to 'sp500_portfolio.xlsx'")
    
except Exception as e:
    print(f"Error creating portfolio: {str(e)}")