# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 21:38:37 2015

@author: Lindsay
"""

import os

os.chdir('./figure files/datafilter/')

for fname in os.listdir('.'):
    if 'trans' in fname:
        os.rename(fname, fname.replace('trans', 'gen'))
