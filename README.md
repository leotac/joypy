# JoyPy

JoyPy is a tiny Python package based on matplotlib + pandas with a single purpose: drawing joyplots.

JoyPy is heavily inspired by the code for kdes in `pandas.plotting`, and uses a couple
of utility functions therein. (This could be probably avoided with a little bit of
extra effort.) 

Whare are joyplots?
---
Joyplots are stacked density plots, simple as that. 

Why are they called joyplots?
---
If you don't know Joy Division, you are lucky: you can still listen to them for the first time!

Examples
--------

Take a look at this [jupyter notebook](Joyplot.ipynb). 

Dependencies
------------

- Python 3.4+

- [numpy](http://www.numpy.org/)

- [scipy](http://www.scipy.org/)

- [matplotlib](http://matplotlib.org/)

- [pandas](http://pandas.pydata.org/)

Not sure what are the oldest supported versions. 
As long as you have somewhat recent versions, you should be fine.
I haven't tested it with Python 2 -- it might work, it might not, but why bother?

License
-------

Released under the MIT license.
