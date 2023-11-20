# import libraries
import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# download data
sp500_df = yf.download(tickers = "^SPX",  # list of tickers. select first ticker for comparison ex ^SPX
            period = "ytd",        # time period
            interval = "1d",       # trading interval
            prepost = False,       # download pre/post market hours data?
            repair = True)         # repair obvious price errors e.g. 100x?

sp500_df = sp500_df.drop(['Volume'],axis=1) # drops 'Volume' column from dataframe

vix_df = yf.download(tickers = "^VIX",  # list of tickers. select second ticker for comparison ex ^VIX
            period = "ytd",        # time period
            interval = "1d",       # trading interval
            prepost = False,       # download pre/post market hours data?
            repair = True)         # repair obvious price errors e.g. 100x?

# create figure
fig, ax1 = plt.subplots(figsize=(16,8), dpi=100)

ax1.plot(sp500_df['Close'], lw=2, color="#1118f2", label="S&P 500 Index") 
ax1.set_ylabel(r"S&P 500 Price ($)", fontsize=18, color="#1118f2", font='serif')
for label in ax1.get_yticklabels():
    label.set_color("blue")
    
ax2 = ax1.twinx()
ax2.plot(vix_df['Close'], lw=2, color="#ed1834", label="VIX Index (right)")
ax2.set_ylabel(r"VIX Price ($)", fontsize=18, color="#ed1834", font='serif')
for label in ax2.get_yticklabels():
    label.set_color("red")

plt.suptitle("S&P 500 vs VIX YTD", fontsize='24', fontweight='bold', font='serif')

ax1.set_xlabel('Year-Month-Day', fontsize=10)

ax1.xaxis.grid(True, which='major')
ax1.yaxis.grid(True, which='major')


# set facecolor
ax1.set_facecolor("#d9d9d9")

ax1.legend(loc=(0.01,.9))
ax2.legend(loc=(0.01,.85))

plt.show();