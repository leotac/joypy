# coding: utf-8
from __future__ import unicode_literals
import joypy
import pandas as pd
from matplotlib import cm

import pytest

@pytest.fixture
def iris():
    return pd.read_csv("data/iris.csv")

@pytest.fixture
def temp():
    return pd.read_csv("data/daily_temp.csv", comment="%")

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
