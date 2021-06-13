# JoyPy

[![PyPI version](https://badge.fury.io/py/joypy.svg)](https://badge.fury.io/py/joypy) [![python version](https://img.shields.io/badge/python-3.5+-blue.svg)](https://www.python.org/download/releases/3.5.0/)  [![Build Status](https://travis-ci.org/leotac/joypy.svg?branch=master)](https://travis-ci.org/leotac/joypy) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Downloads](https://pepy.tech/badge/joypy)](https://pepy.tech/project/joypy)


JoyPy is a one-function Python package based on matplotlib + pandas with a single purpose: drawing joyplots (a.k.a. ridgeline plots).

<img src="temperatures.png" width="600" alt="A joyplot.">

The code for JoyPy borrows from the code for kdes in `pandas.plotting`, and uses a couple
of utility functions therein.

What are joyplots?
---
Joyplots are stacked, partially overlapping density plots, simple as that. They are a nice way to plot data
to visually compare distributions, especially those that change across one dimension (e.g., over time).
Though hardly a new technique, they have become very popular lately thanks to the R package [ggjoy](https://github.com/clauswilke/ggjoy) 
(which is much better developed/maintained than this one -- and I strongly suggest you use that if you can use R and ggplot.)
**Update**: the ggjoy package has now been renamed [ggridges](https://github.com/clauswilke/ggridges).

Why are they called joyplots?
---
If you don't know Joy Division, you are lucky: you can still listen to them for the first time!
Here's a hint: google ["Unknown Pleasures"](https://www.youtube.com/watch?v=fhCLalLXHP4).
This kind of plot is now also known as *ridgeline plot*, since the original name is controversial. 

Documentation and examples
--------

JoyPy has no real documentation.
You're strongly encouraged to take a look at this [jupyter notebook](Joyplot.ipynb) with a growing number of examples.
Similarly, github issues may contain some wisdom :-)

A minimal example is the following:
```python
import joypy
import pandas as pd

iris = pd.read_csv("data/iris.csv")
fig, axes = joypy.joyplot(iris)
```

By default, `joypy.joyplot()` will draw joyplot with a density subplot for each numeric column in the dataframe. The density is obtained with the `gaussian_kde` function of scipy.

Note: `joyplot()` returns n+1 axes, where n is the number of visible rows (subplots).
Each subplot has its own axis, while the last axis (`axes[-1]`) is the one that is used for things such as plotting the background or changing xticks, and is the one you might need to play with in case you want to manually tweak something.


Dependencies
------------

- Python 3.5+  
Compatibility with python 2.7 has been dropped with release 0.2.0.

- [numpy](http://www.numpy.org/)
- [scipy](http://www.scipy.org/) >= 0.11
- [matplotlib](http://matplotlib.org/)
- [pandas](http://pandas.pydata.org/) >= 0.20  **Warning**: compatibility with pandas >= 0.25 requires joypy >= 0.2.1


Not sure what are the oldest supported versions. 
As long as you have somewhat recent versions, you should be fine.

Installation
------

It's actually on PyPI, because why not:
    
    pip install joypy

To install from github, run:

    git clone git@github.com:leotac/joypy.git
    cd joypy
    pip install .

License
-------

Released under the MIT license.

Disclaimer + contributing
-----

This is just a sunday afternoon hack, so no guarantees! If you want to contribute or just copy/fork, feel free to. 
