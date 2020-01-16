import pandas as pd
from statsmodels.tsa.stattools import adfuller, kpss


def test_stationarity(
        timeseries, plot=False, plt=None, method='ADF', print_results=True):
    """
    Check the stationary of the timeseries

    - Calculate rolling stats
    - Plot original timeseries, mean and std
    - Perform Augmented Dickey-Fuller hypothesis test
    """

    # Rolling statistics. We select one day: 24 hours
    rolmean = timeseries.rolling(window=24).mean()
    rolstd = timeseries.rolling(window=24).std()

    if plot:
        # Plot rolling statistics of orginal, mean and std:
        plt.plot(timeseries, color='blue', label='Original')
        plt.plot(rolmean, color='red', label='Rolling Mean')
        plt.plot(rolstd, color='black', label='Rolling Std')
        plt.legend(loc='best')
        plt.title('Rolling Mean & Standard Deviation')

    if method == 'ADF':
        test = adfuller(timeseries, autolag='AIC')
        test = [t for t in test]
        del test[3]
    if method == 'KPSS':
        test = kpss(timeseries, regression='ct')

    output = pd.Series(
        test[0:3],
        index=[
            'Test Statistic',
            'p-value',
            '#Lags Used',
            #             'Number of Observations Used'
        ]
    )
    for key, value in test[3].items():
        output['Critical Value (%s)' % key] = value

    if print_results:
        print('Results of {} Test:'.format(method))
        print(output)

    return output
