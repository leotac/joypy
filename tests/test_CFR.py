#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 14:51:11 2021

@author: jsibert
"""

import pandas as pd
import sys
from matplotlib import cm
joypy_dir = '/home/jsibert/Projects/Python/joypy'
sys.path.append(joypy_dir)
from joypy import joyplot

CFR = pd.read_csv(joypy_dir+"/data/CFR.csv",comment='#')
print(CFR)
zmask = CFR['ratio'] > 0
labels = CFR['date'].unique()
for i in range(1,len(labels)):
    if labels[i].split('-')[2] != '01':
        labels[i] = None
fig,axes = joyplot(CFR[zmask], by='date', column='ratio', labels = labels,
                       range_style='own', tails = 0.1, 
                       kind = 'lognorm',
             #         ylim='max',
                       overlap = 3, 
                       x_range=[0.0,0.061],
                       grid="y", linewidth=0.25, legend=False, figsize=(6.5,8.0),
                       title='Case Fatality Ratio',
                       colormap=cm.Blues_r)
