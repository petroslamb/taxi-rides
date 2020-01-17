Taxi Rides
==============================

Taxi rides prediction from a set of sample rides.

The deliverable is a report, but it is possible to reproduce datasets and
models.

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


--------

# Installation


## Setup environment

To setup the project use `virtualenv` and create a `python3` virtual environment to install
all dependencies. For example:

```
mkvirtualenv --python=python3 taxi-rides
workon taxi-rides
```

## Install taxi-rides

To install the source files and project dependencies, from the project root folder run:

```
pip install .
pip install -r requirements.txt
```

The library `fbprophet` may appear to fail at first, but will shortly resume installation.

## Usage

Use the inventory above to locate where everything is in the project. Use `make` to explore your
options, however, some are there for showcasing.

All reports and figures are in the relevant folder:

```
./reports/
```

To run the notebooks you need to reproduce the datasets. Place the raw data inside:

```
./data/raw/routes.csv
```
and run `Jupyer Notebook`

```
cd ./notebooks
jupyter notebook
```

## Recreate datasets

You need the following folders:
```
mkdir ./data
mkdir ./data/interim
mkdir ./data/raw
mkdir ./data/external
mkdir ./data/processed
```
To recreate all datasets, make sure you have `./data/raw/routes.csv` and run:

```
make data
```

The process takes several minutes to complete.

After the process is complete, you should be able to run notebooks out of order
in order to replicate results and models. Models will be added in the relevant
directory.

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
