# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 14:52:30 2015

@author: Lindsay
"""

import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(2, 2, figsize=(6, 3.3))
for axes_id, axes in enumerate(axs.ravel()):
    axes.text(-.1, 1.05, chr(65+axes_id), transform=axes.transAxes,
              fontsize=12, fontweight='bold', va='top')
ax0 = axs[0, 0]
ax1 = axs[0, 1]
ax2 = axs[1, 0]
ax3 = axs[1, 1]
d2_t = np.genfromtxt('./data/ap4_disp2_fine_time.csv', delimiter=',')
d2_nr_cur = np.genfromtxt('./data/ap4_disp2_nr_current.csv', delimiter=',')
d2_mc_cur = np.genfromtxt('./data/ap4_disp2_mc_current.csv', delimiter=',')
d2_ia_cur = np.genfromtxt('./data/ap4_disp2_ia_current.csv', delimiter=',')
d2_gen_cur = np.genfromtxt('./data/ap4_disp2_gen_current.csv', delimiter=',')


# %% Plot 1: Normal mice, separate currents
ax0.plot(d2_t, -d2_nr_cur*1e9, linestyle='-.', color='0')
ax0.plot(d2_t, -d2_mc_cur*1e9, linestyle='--', color='0')
ax0.plot(d2_t, -d2_ia_cur*1e9, linestyle=':', color='0')
ax0.set_xlim(0, 2)
ax0.set_ylim(-10, 0)
ax0.set_yticks([-10, -5, 0])
ax0.set_xlabel('Time (sec)')
ax0.set_ylabel('Current (pA)')


# %% Plot 2: Piezo2 mice, separate currents
ax1.plot(d2_t, -d2_nr_cur*1e9, linestyle='-.', color='0')
ax1.plot(d2_t, -d2_ia_cur*1e9, linestyle=':', color='0')
ax1.set_xlim(0, 2)
ax1.set_ylim(-10, 0)
ax1.set_yticks([-10, -5, 0])
ax1.set_xlabel('Time (sec)')
ax1.set_ylabel('Current (pA)')


# %% Plot 3: Normal mice, total current
ax2.plot(d2_t, -d2_gen_cur*1e9, linestyle='-', color='0')
ax2.set_xlim(0, 2)
ax2.set_ylim(-10, 0)
ax2.set_yticks([-10, -5, 0])
ax2.set_xlabel('Time (sec)')
ax2.set_ylabel('Current (pA)')


# %% Plot 4: Piezo2 mice, total current
ax3.plot(d2_t, -(d2_nr_cur+d2_ia_cur)*1e9, linestyle='-', label='total',
         color='0')
ax3.plot(5, 5, linestyle='-.', label='RA', color='0')
ax3.plot(5, 5, linestyle='--', label='SA', color='0')
ax3.plot(5, 5, linestyle=':', label='USA', color='0')
ax3.set_xlim(0, 2)
ax3.set_ylim(-10, 0)
ax3.set_yticks([-10, -5, 0])
ax3.set_xlabel('Time (sec)')
ax3.set_ylabel('Current (pA)')
leg3 = ax3.legend(loc=4, prop={'size': 10})


# %%
fig.tight_layout()
fig.savefig('./Unused figures/approach4_current.tif', dpi=600)