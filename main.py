import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt



DATAPATH = './data.csv'

data = pd.read_csv(DATAPATH, sep=";")

data.head(5)