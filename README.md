# Equal Weighted Index Portfolio Calculator

This Python program calculates an **equal-weighted portfolio** for a stock index, similar to the S&P 500. Instead of using market capitalization weights, it distributes the investment **equally across all stocks** in the index.

---

## Features

- Calculates equal-weighted portfolio allocations  
- Downloads historical stock data using `yfinance`  
- Generates an Excel report with portfolio details  
- Handles large datasets efficiently with chunked downloads  
- Includes error handling for rate limiting and data issues  

---

## Requirements

- Python **3.8** or higher  
- Required Python packages:
  - `pandas`
  - `yfinance`
  - `openpyxl` (for Excel output)

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/madlad-code/equally_weighted_index.git
   cd equally_weighted_index
   ```

2. Install the required dependencies:
   ```bash
   pip install pandas yfinance openpyxl
   ```

---

## Usage

The program is configured by default for the **S&P 500** index. You can modify the tickers list in the code to use a different index (e.g., NASDAQ, Dow Jones).

To run the program:
```bash
python SP500_equal_weighted_index.py
```

The program will:
- Download historical stock data
- Calculate equal-weighted allocations
- Generate an Excel file: `sp500_portfolio.xlsx`

---

## Customizing for Other Indexes

To use this program with a different stock index:
1. Replace the `tickers` list with your desired index's stock symbols  
2. Adjust the `investment_amount` variable for your desired portfolio size  
3. Modify the date range in the `yf.download()` function if needed  

---

## Output

The Excel file contains:
- Ticker symbols  
- Current prices  
- Portfolio weights (equal for all stocks)  
- Dollar allocations  
- Number of shares to purchase  
- Total amount spent per stock  

---

## Error Handling

The program includes:
- Rate limiting protection for Yahoo Finance API  
- Error handling for data download failures  
- Chunked data downloads to prevent API rate limits  
- Graceful handling of missing or invalid data  
