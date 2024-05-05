import numpy as np
import yfinance as yf
from math import sqrt
import matplotlib.pyplot as plt
import matplotlib.dates as matplot_dates

### common functions ###
def fetch_ticker(ticker_name):
    # fetch ticker data from yahoo finance
    return yf.Ticker(ticker_name)

def fetch_ticker_hist(ticker, duration="30d"):
    # fetch history
    return ticker.history(period=duration)

### PLOT operations ###

def plot_side_by_side(ticker_1_hist, ticker_2_hist):

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(16,5))
    axes[0].plot(ticker_1_hist.index, ticker_1_hist['Close'])
    axes[0].axes.get_xaxis().set_visible(False)
    axes[1].plot(ticker_2_hist.index, ticker_2_hist['Close'])
    axes[1].axes.get_xaxis().set_visible(False)
    plt.show()

def plot_at_once(ticker_1_hist, ticker_2_hist):

    fig, ax_1 = plt.subplots(figsize=(16,9))

    color = 'tab:blue'
    ax_1.set_xlabel('time')
    ax_1.set_ylabel('Close ticker_1 ', color=color)
    ax_1.plot(ticker_1_hist.index, ticker_1_hist['Close'], color=color)
    ax_1.tick_params(axis='y', labelcolor=color)

    ax_2 = ax_1.twinx() 

    color = 'tab:red'
    ax_2.set_ylabel('Close ticker_2', color=color) 
    ax_2.plot(ticker_2_hist.index, ticker_2_hist['Close'], color=color)
    ax_2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout() 
    plt.show()

def plot_regression(ticker_hist, degree):
        # polynomial fit AMUNDI data

        x = np.arange(ticker_hist.index.size)
        coefs = np.poly1d(np.polyfit(x, ticker_hist['Close'], degree))

        ffit = np.poly1d(coefs)
        x_new = np.linspace(x[0], x[-1], num=len(x)*10)

        plt.plot(x_new, ffit(x_new))
        plt.plot(x, ticker_hist['Close'])


def calc_mean(sample):
    n = len(sample)
    sum_of_items = 0.0
    for item in sample:
        sum_of_items = sum_of_items + item
    return sum_of_items / n

def calc_variance(sample):
    n = len(sample)
    mean = calc_mean(sample)
    temp = 0
    for item in sample:
        temp = temp + ((item - mean)**2)
    return temp / (n)

def calc_sample_covariance(x,y):
    if len(x) != len(y):
        print(len(x))
        print(len(y))
        print("len(x) != len(y)")
        return 0
    n = len(x)
    mean_x = calc_mean(x)
    mean_y = calc_mean(y)
    temp = 0
    for i in range(n):
        temp = temp + ((y[i] - mean_y)*(x[i] - mean_x))
    return temp / (n-1)

def calc_corr_coeff(x,y):
    cov = calc_sample_covariance(x,y)
    var1 = sqrt(calc_variance(x))
    var2 = sqrt(calc_variance(y))
    return cov/(var1*var2)