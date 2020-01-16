import pandas as pd
import numpy as np
import matplotlib
import seaborn as sns
import mpu
import warnings


matplotlib.use('nbagg')
warnings.filterwarnings("ignore")
sns.set()


def outlier_removal(input_filepath, output_filepath):

    # Load and clean
    raw_pd = pd.read_csv(input_filepath, delimiter='\t')
    raw_pd = raw_pd.dropna()
    raw_pd.request_date = pd.to_datetime(raw_pd.request_date)
    data = raw_pd

    data['distance'] = data.apply(
        lambda x: mpu.haversine_distance(
            (x['source_latitude'], x['source_longitude']),
            (x['destination_latitude'], x['destination_longitude'])
        ),
        axis=1
    )

    data.to_csv('../data/interim/raw_data_with_haversine_distance')

    tmp = data.copy().reset_index()

    for col in ['source_latitude', 'source_longitude', 'destination_latitude',
                'destination_longitude', 'distance']:

        lower = np.percentile(data[col], 00.1)
        upper = np.percentile(data[col], 99.9)
        tmp = tmp.query(
            '{lower}<{col}<{upper}'.format(lower=lower, col=col, upper=upper)
        )

    tmp.to_csv('../data/interim/dropped_outlier_data_with_haversine_distance')

    # Change gears to temporal data: trips-per-hour
    data2 = tmp.set_index(tmp.request_date)
    data2.drop(
        [
            'passenger_id', 'source_address',
            'destination_address', 'request_date'
        ],
        1, inplace=True
    )
    data2['trip_counts'] = 1
    trips = data2.resample('1H')[['trip_counts']].sum()

    lower = np.percentile(trips.trip_counts, 00.1)
    upper = np.percentile(trips.trip_counts, 99.9)

    trips2 = trips.where(
        trips.trip_counts > lower, lower
    ).where(
        trips.trip_counts < upper, upper
    )

    trips2.to_csv(
        '../data/interim/trips_per_hour_dropped_na_and_all_outliers_'
        'under_001_and_over_999.csv'
    )
    trips2.to_csv(output_filepath)
