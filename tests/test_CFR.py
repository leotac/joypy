#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 14:51:11 2021

@author: jsibert
"""

import pandas as pd
from matplotlib import cm
#joypy_dir = '/home/jsibert/Projects/Python/joypy'
from joypy import joyplot

CFR = pd.read_csv("../data/CFR.csv",comment='#')
zmask = CFR['ratio'] > 0
labels = CFR['date'].unique()
for i in range(1,len(labels)):
    if labels[i].split('-')[2] != '01':
        labels[i] = None
fig,axes = joyplot(CFR[zmask], by='date', column='ratio', labels = labels,
                       kind = 'lognorm', range_style='own', tails = 0.1, 
                       overlap = 3, x_range=[0.0,0.061], grid="y",
                       linewidth=0.25, figsize=(6.5,9.0),
                       title='Case Fatality Ratio',
                       colormap=cm.Blues_r)
