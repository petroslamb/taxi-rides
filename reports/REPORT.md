# Taxi Ride Analysis: Forecasting for the city of Lima

This report centralizes the findings of the analysis and modelling.

It was written in a short timeframe and should act only as a review of the project.

Much like a table of contents.

## Introduction

Taxi ride analysis is an important metric for a company working in the field.
Even more so for hourly trip count forecasting, which is chosen as
 our analysis centerpoint.

## Setup

The project is an installable package, and organized to help a future analyst
reproduce and extend the results. It was based on:

https://drivendata.github.io/cookiecutter-data-science/

Take a look at `README.md` for a quick tour, installation and usage instuctions.

The detailed analysis lives in the 5 notebooks under `/notebooks` and we'll
get into it right away.

## Exploration and Outliers

The data was first explored and cleaned during the first two notebooks.

Numbers on headers represent the relevant notebooks.

### 0. Load and explore data

Pandas is used throughout the analysis as the container type of choice for our
dataset and timeseries data.

`NaN` values were dropped as they were but a small percentage  (<<0.01) of the data.

#### Locations

First the columns `source_latitude`, `source_longitude` and equivalent two destination
columns were explored.

Starting with a quick boxplot and histogram to find out the std, mean and variance,
helps to start thinking about possible outliers. Quick scatterplots and use of
maps with `folium` (https://python-visualization.github.io/folium/) helped to 
make sure, in a quick and dirty way, that trips were on land and at the right city.

#### Trip counts

After making sure there were not many trips outside the city, the next thing was
to do the same boxplot and histogram for trip counts per day. 

The data spawned for about 122 days.

#### Passenger id's and addresses

Passenger id's were a problem to decipher, as some id's would conduct thousands 
of trips from and to specific addresses, without necessarily going back.

It was concluded that these id's have some special quality, for which the context
is missing, and is no use getting much into.

#### Trip distances

The feature was created introduced to the datacet and explored with the 
same methods (boxplot, histogram) as the rest.

#### Other considerations

There was no time, but a correlation matrix between dataset features was in order at
this point.

### 1. Outlier removal and timeseries exploration

This next notebook removed outliers which were under `0.5%` and over `99.5%`
of the range of all numerical values: `lat`, `lon`, `distance` and `trip_counts`
per hour.

Then after switching gear to the  timeseries depicting `trip-counts-per-hour`,
a deliberate graphical exploration revealed the general trend and 2 most 
prevelant seasonalities of the dataset.

### 2. ARIMA forecasting

This part goes through the ideas of stationality on a dataset and introduces
the basic tests to clear that notion.

Furthermore, autocorrelation and frequency graphs help give an idea of the 
complexity inherent in the timeseries.

After preparing a simple train-test split, an automatic grid search algorithm
was used to determine the three key values for ARIMA.

As a standard process forecasts are evaluated in and out of sample. Then the
standardized residual is also evaluated in a qualitative manner. RMSE is used
as a metric for out-of-sample predictions.






