# coding: utf-8
from __future__ import unicode_literals
import joypy
import pandas as pd
import numpy as np
from matplotlib import cm

import pytest

print('joypy version',joypy.__version__)

@pytest.fixture
def iris():
    return pd.read_csv("data/iris.csv")

@pytest.fixture
def temp():
    return pd.read_csv("data/daily_temp.csv", comment="%")

@pytest.fixture
def CFR():
    return pd.read_csv("data/CFR.csv",comment='#')

def test_basic(iris):
    fig, axes = joypy.joyplot(iris)

def test_groupby(iris):
    fig, axes = joypy.joyplot(iris, by="Name")
    fig, axes = joypy.joyplot(iris, by="Name", ylim='own')
    fig, axes = joypy.joyplot(iris, by="Name", overlap=3)

def test_groupby_hist(iris):
    fig, axes = joypy.joyplot(iris, by="Name", column="SepalWidth",
                              hist="True", bins=20, overlap=0,
                              grid=True, legend=False)
def test_temperature(temp):
    labels=[y if y%10==0 else None for y in list(temp.Year.unique())]
    fig, axes = joypy.joyplot(temp, by="Year", column="Anomaly", labels=labels, range_style='own', 
                              grid="y", linewidth=1, legend=False, figsize=(6,5),
                              title="Global daily temperature 1880-2014 \n(°C above 1950-80 average)",
                              colormap=cm.autumn_r)

def test_raw_counts(temp):
    labels=[y if y%10==0 else None for y in list(temp.Year.unique())]
    fig, axes = joypy.joyplot(temp, by="Year", column="Anomaly", labels=labels, range_style='own', 
                              grid="y", linewidth=1, legend=False, fade=True, figsize=(6,5),
                              title="Global daily temperature 1880-2014 \n(°C above 1950-80 average)",
                              kind="counts", bins=30)

def test_raw_data():
    x = np.arange(0, 100, 0.1)
    y =[n*x for n in range(1,4)]
    fig, ax = joypy.joyplot(y, labels=["a","b","c"])
    
def test_lognorm(CFR):
    zmask = CFR['ratio'] > 0
    labels = CFR['date'].unique()
    for i in range(1,len(labels)):
        if labels[i].split('-')[2] != '01':
            labels[i] = None
    fig,axes = joypy.joyplot(CFR[zmask], by='date', column='ratio', labels = labels,
                           kind = 'lognorm', range_style='own', tails = 0.1, 
                           overlap = 4, x_range=[0.0,0.061], grid="y",
                           linewidth=0.25, figsize=(6.5,9.0),
                           title='Case Fatality Ratio',
                           colormap=cm.Blues_r,
                           ylim = 'own',
                           normalize = True, floc=None)       