# JoyPy

[![PyPI version](https://badge.fury.io/py/joypy.svg)](https://badge.fury.io/py/joypy) [![python version](https://img.shields.io/badge/python-3.5+-blue.svg)](https://www.python.org/download/releases/3.5.0/)  [![Build Status](https://travis-ci.org/sbebo/joypy.svg?branch=master)](https://travis-ci.org/sbebo/joypy) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


JoyPy is a one-function Python package based on matplotlib + pandas with a single purpose: drawing joyplots.

<img src="temperatures.png" width="600" alt="A joyplot.">

The code for JoyPy borrows from the code for kdes in `pandas.plotting`, and uses a couple
of utility functions therein. (This could be probably avoided with a little bit of
extra effort.) 

What are joyplots?
---
Joyplots are stacked, partially overlapping density plots, simple as that. They are a nice way to plot data
to visually compare distributions, especially those that change across one dimension (e.g., over time).
Though hardly a new technique, they have become very popular lately thanks to the R package [ggjoy](https://github.com/clauswilke/ggjoy) 
(which is clearly much better developed/maintained than this one -- and I strongly suggest you use that if you can use R and ggplot.)
**Update**: the ggjoy package has now been renamed [ggridges](https://github.com/clauswilke/ggridges).

Why are they called joyplots?
---
If you don't know Joy Division, you are lucky: you can still listen to them for the first time!
Here's a hint: google ["Unknown Pleasures"](https://www.youtube.com/watch?v=ncJ8FCvCofw).
This kind of plot is now also known as *ridgeline plot*, since the original name is controversial. 

Examples
--------

Take a look at this [jupyter notebook](Joyplot.ipynb) for a couple of simple examples. 

Dependencies
------------

- Python 3.5+  
Compatibility with python 2.7 has been dropped with release 1.11.

- [numpy](http://www.numpy.org/)
- [scipy](http://www.scipy.org/) >= 0.11
- [matplotlib](http://matplotlib.org/)
- [pandas](http://pandas.pydata.org/) >= 0.20


Not sure what are the oldest supported versions. 
As long as you have somewhat recent versions, you should be fine.

Installation
------

It's actually on PyPI, because why not:
    
    pip install joypy

To install from github, run:

    git clone git@github.com:sbebo/joypy.git
    cd joypy
    pip install .

License
-------

Released under the MIT license.

Disclaimer + contributing
-----

This is just a sunday afternoon hack, so no guarantees! If you want to contribute or just copy/fork, feel free to. 
