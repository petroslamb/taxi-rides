import matplotlib.pylab as plt
from statsmodels.tsa import seasonal
from models.stats_tests import test_stationarity
from src.visualization.visualize import plot_decomposition


def multilevel_seasonal_decompose(timeseries,
                                  level=1,
                                  plot=False,
                                  keep_all_levels=False,
                                  stationarity_test=None,
                                  decomp_model='additive'):
    ts_decomps = []
    temp_decomp = None
    temp_ts = timeseries

    for l in range(level):
        temp_decomp = seasonal.seasonal_decompose(temp_ts, model=decomp_model)

        if keep_all_levels:
            ts_decomps.append((temp_ts, temp_decomp))

        temp_ts = temp_decomp.trend
        temp_ts.dropna(inplace=True)

    if plot:
        plot_decomposition(temp_ts, temp_decomp)
        plt.show()

    if stationarity_test:
        test_stationarity(temp_ts, method=stationarity_test)

    if keep_all_levels:
        return ts_decomps
    return temp_ts, temp_decomp
