# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 21:11:25 2015

@author: Lindsay
"""

import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(4, 1, figsize=(3, 7))
for axes_id, axes in enumerate(axs.ravel()):
    axes.text(-.12, 0.95, chr(65+axes_id), transform=axes.transAxes,
              fontsize=12, fontweight='bold', va='top')
axs0 = axs[0]
axs1 = axs[1]
axs2 = axs[2]
axs3 = axs[3]
t = np.genfromtxt('./data/disp2_fine_time.csv', delimiter=',')

# %% Plot 1: Original current
orig_nr_cur = np.genfromtxt('./data/disp2_nr_current.csv', delimiter=',')
orig_mc_cur = np.genfromtxt('./data/disp2_mc_current.csv', delimiter=',')
axs0.plot(t, -orig_nr_cur*1e9, linestyle='-', color='0')
axs0.plot(t, -orig_mc_cur*1e9, linestyle='--', color='0')
axs0.set_xlim(0, 2)
axs0.set_ylim(-15, 0)
axs0.set_yticks([-15, -10, -5, 0])
axs0.set_xlabel('Time (sec)')
axs0.set_ylabel('Current (pA)')


# %% Plot 2: Current: new approach 1
ap1_nr_cur = np.genfromtxt('./data/ap1_disp2_nr_current.csv', delimiter=',')
ap1_mc_cur = np.genfromtxt('./data/ap1_disp2_mc_current.csv', delimiter=',')
axs1.plot(t, -ap1_nr_cur[:, 0]*1e9, linestyle='-', color='0')
axs1.plot(t, -ap1_mc_cur[:, 0]*1e9, linestyle='--', color='0')
axs1.set_xlim(0, 2)
axs1.set_ylim(-15, 0)
axs1.set_yticks([-15, -10, -5, 0])
axs1.set_xlabel('Time (sec)')
axs1.set_ylabel('Current (pA)')


# %% Plot 3: Current: new approach 2
ap2_nr_cur = np.genfromtxt('./data/ap2_disp2_nr_current.csv', delimiter=',')
ap2_mc_cur = np.genfromtxt('./data/ap2_disp2_mc_current.csv', delimiter=',')
ap2_ia_cur = np.genfromtxt('./data/ap2_disp2_ia_current.csv', delimiter=',')
axs2.plot(t, -ap2_nr_cur[:, 0]*1e9, linestyle='-', color='0')
axs2.plot(t, -ap2_mc_cur[:, 0]*1e9, linestyle='--', color='0')
axs2.plot(t, -ap2_ia_cur[:, 0]*1e9, linestyle='-.', color='0')
axs2.set_xlim(0, 2)
axs2.set_ylim(-15, 0)
axs2.set_yticks([-15, -10, -5, 0])
axs2.set_xlabel('Time (sec)')
axs2.set_ylabel('Current (pA)')


# %% Plot 4: Current: new approach 3
ap3_nr_cur = np.genfromtxt('./data/ap3_disp2_nr_current.csv', delimiter=',')
ap3_mc_cur = np.genfromtxt('./data/ap3_disp2_mc_current.csv', delimiter=',')
axs3.plot(t, -ap3_nr_cur[:, 0]*1e9, linestyle='-', label='RA', color='0')
axs3.plot(t, -ap3_mc_cur[:, 0]*1e9, linestyle='--', label='SA', color='0')
axs3.plot(5, 5, linestyle='-.', label='IA', color='0')
axs3.set_xlim(0, 2)
axs3.set_ylim(-15, 0)
axs3.set_yticks([-15, -10, -5, 0])
axs3.set_xlabel('Time (sec)')
axs3.set_ylabel('Current (pA)')
leg3 = axs3.legend(loc=4, prop={'size': 10})


# %%
fig.tight_layout()
fig.savefig('./F14 new approach currents/F14 new approach currents.tif',
            dpi=600)
