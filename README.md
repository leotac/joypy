# JoyPy

JoyPy is a one-function Python package based on matplotlib + pandas with a single purpose: drawing joyplots.

<img src="temperatures.png" width="600" alt="A joyplot.">

The code for JoyPy borrows from the code for kdes in `pandas.plotting`, and uses a couple
of utility functions therein. (This could be probably avoided with a little bit of
extra effort.) 

Whare are joyplots?
---
Joyplots are stacked, partially overlapping density plots, simple as that. They are a nice way to plot data
to visually compare distributions, especially those that change across one dimension (e.g., over time).
Though hardly a new technique, they have become much popular lately thanks to the R package [ggjoy](https://github.com/clauswilke/ggjoy) 
(which is clearly much better developed/maintained than this one, so I suggest you to use that if you can use R and ggplot.)

Why are they called joyplots?
---
If you don't know Joy Division, you are lucky: you can still listen to them for the first time!
Here's a hint: google ["Unknown Pleasures"](https://www.youtube.com/watch?v=ncJ8FCvCofw).

Examples
--------

Take a look at this [jupyter notebook](Joyplot.ipynb) for a couple of simple examples. 

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

Disclaimer + contributing
-----

This is just a sunday afternoon hack, so no guarantees! If you want to contribute or just copy/fork, feel free to. 
