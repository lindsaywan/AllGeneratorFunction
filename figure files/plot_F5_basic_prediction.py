# -*- coding: utf-8 -*-
"""
Created on Mon May 25 17:10:22 2015

@author: Lindsay

This module plots the comparison of spikes and firing rates between model
prediction and electrophysiological recordings for normal SAI afferents.
"""

import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(4, 2, figsize=(6, 7))
for axes_id, axes in enumerate(axs.ravel()):
    axes.text(-.12, 0.95, chr(65+axes_id), transform=axes.transAxes,
              fontsize=12, fontweight='bold', va='top')
axs0 = axs[0, 0]
axs1 = axs[0, 1]
axs2 = axs[1, 0]
axs3 = axs[1, 1]
axs4 = axs[2, 0]
axs5 = axs[2, 1]
axs6 = axs[3, 0]
axs7 = axs[3, 1]


# %% Plot 1: Model spike with generator current
d2_gen_spike = np.genfromtxt('./data/disp2_gen_spike.csv', delimiter=',')
d3_gen_spike = np.genfromtxt('./data/disp3_gen_spike.csv', delimiter=',')
axs0.vlines(d2_gen_spike, ymin=-1.5, ymax=-0.5, linewidth=0.5, color='0.5')
axs0.axhline(y=-1, xmin=0, xmax=5, linewidth=0.5, color='0.5')
axs0.vlines(d3_gen_spike, ymin=0.5, ymax=1.5, linewidth=0.5, color='0')
axs0.axhline(y=1, xmin=0, xmax=5, linewidth=0.1, color='0')
axs0.set_xlim(0, 5)
axs0.set_ylim(-2, 2)
axs0.set_xlabel('Time (sec)')
axs0.set_ylabel('Spikes')
axs0.get_yaxis().set_ticks([])


# %% Plot 2: Model fr with generator current
d2_gen_fr_time = np.genfromtxt('./data/disp2_gen_inst_fr_time.csv',
                               delimiter=',')
d3_gen_fr_time = np.genfromtxt('./data/disp3_gen_inst_fr_time.csv',
                               delimiter=',')
d2_gen_fr_fr = np.genfromtxt('./data/disp2_gen_inst_fr_fr.csv', delimiter=',')
d3_gen_fr_fr = np.genfromtxt('./data/disp3_gen_inst_fr_fr.csv', delimiter=',')
axs1.plot(d2_gen_fr_time, d2_gen_fr_fr, marker='.', linestyle='None',
          color='0.5')
axs1.plot(d3_gen_fr_time, d3_gen_fr_fr, marker='.', linestyle='None',
          color='0')
axs1.set_xlim(0, 5)
axs1.set_ylim(0, 200)
axs1.set_xlabel('Time (sec)')
axs1.set_ylabel('FR (Hz)')


# %% Plot 3: Model spike with generator current: New approach 1
ap1_d2_gen_spike = np.genfromtxt('./data/ap1_disp2_gen_spike.csv',
                                 delimiter=',')
ap1_d3_gen_spike = np.genfromtxt('./data/ap1_disp2_gen_spike.csv',
                                 delimiter=',')
axs2.vlines(ap1_d2_gen_spike, ymin=-1.5, ymax=-0.5, linewidth=0.5, color='0.5')
axs2.axhline(y=-1, xmin=0, xmax=5, linewidth=0.5, color='0.5')
axs2.vlines(ap1_d3_gen_spike, ymin=0.5, ymax=1.5, linewidth=0.5, color='0')
axs2.axhline(y=1, xmin=0, xmax=5, linewidth=0.1, color='0')
axs2.set_xlim(0, 2)
axs2.set_ylim(-2, 2)
axs2.set_xlabel('Time (sec)')
axs2.set_ylabel('Spikes')
axs2.get_yaxis().set_ticks([])


# %% Plot 4: Model fr with generator current: New approach 1
ap1_d2_gen_fr_time = np.genfromtxt('./data/ap1_disp2_gen_inst_fr_time.csv',
                                   delimiter=',')
ap1_d3_gen_fr_time = np.genfromtxt('./data/ap1_disp3_gen_inst_fr_time.csv',
                                   delimiter=',')
ap1_d2_gen_fr_fr = np.genfromtxt('./data/ap1_disp2_gen_inst_fr_fr.csv',
                                 delimiter=',')
ap1_d3_gen_fr_fr = np.genfromtxt('./data/ap1_disp3_gen_inst_fr_fr.csv',
                                 delimiter=',')
axs3.plot(ap1_d2_gen_fr_time, ap1_d2_gen_fr_fr, marker='.', linestyle='None',
          color='0.5')
axs3.plot(ap1_d3_gen_fr_time, ap1_d3_gen_fr_fr, marker='.', linestyle='None',
          color='0')
axs3.set_xlim(0, 2)
axs3.set_ylim(0, 200)
axs3.set_xlabel('Time (sec)')
axs3.set_ylabel('FR (Hz)')


# %% Plot 5: Model spike with generator current: New approach 1
ap4_d2_gen_spike = np.genfromtxt('./data/ap4_disp2_gen_spike.csv',
                                 delimiter=',')
ap4_d3_gen_spike = np.genfromtxt('./data/ap4_disp2_gen_spike.csv',
                                 delimiter=',')
axs4.vlines(ap4_d2_gen_spike, ymin=-1.5, ymax=-0.5, linewidth=0.5, color='0.5')
axs4.axhline(y=-1, xmin=0, xmax=5, linewidth=0.5, color='0.5')
axs4.vlines(ap4_d3_gen_spike, ymin=0.5, ymax=1.5, linewidth=0.5, color='0')
axs4.axhline(y=1, xmin=0, xmax=5, linewidth=0.1, color='0')
axs4.set_xlim(0, 2)
axs4.set_ylim(-2, 2)
axs4.set_xlabel('Time (sec)')
axs4.set_ylabel('Spikes')
axs4.get_yaxis().set_ticks([])


# %% Plot 6: Model fr with generator current: New approach 1
ap4_d2_gen_fr_time = np.genfromtxt('./data/ap4_disp2_gen_inst_fr_time.csv',
                                   delimiter=',')
ap4_d3_gen_fr_time = np.genfromtxt('./data/ap4_disp3_gen_inst_fr_time.csv',
                                   delimiter=',')
ap4_d2_gen_fr_fr = np.genfromtxt('./data/ap4_disp2_gen_inst_fr_fr.csv',
                                 delimiter=',')
ap4_d3_gen_fr_fr = np.genfromtxt('./data/ap4_disp3_gen_inst_fr_fr.csv',
                                 delimiter=',')
axs5.plot(ap4_d2_gen_fr_time, ap4_d2_gen_fr_fr, marker='.', linestyle='None',
          color='0.5')
axs5.plot(ap4_d3_gen_fr_time, ap4_d3_gen_fr_fr, marker='.', linestyle='None',
          color='0')
axs5.set_xlim(0, 2)
axs5.set_ylim(0, 200)
axs5.set_xlabel('Time (sec)')
axs5.set_ylabel('FR (Hz)')


# %% Plot 7: Recording spike with generator current
d2_rec_gen_spike = np.genfromtxt('./data/rec_disp2_run2_gen_spike.csv',
                                 delimiter=',')
d4_rec_gen_spike = np.genfromtxt('./data/rec_disp4_run3_gen_spike.csv',
                                 delimiter=',')
axs6.vlines(d2_rec_gen_spike, ymin=-1.5, ymax=-0.5, linewidth=0.5, color='0.5')
axs6.axhline(y=-1, xmin=0, xmax=5, linewidth=0.5, color='0.5')
axs6.vlines(d4_rec_gen_spike, ymin=0.5, ymax=1.5, linewidth=0.5, color='0')
axs6.axhline(y=1, xmin=0, xmax=5, linewidth=0.1, color='0')
axs6.set_xlim(0, 2)
axs6.set_ylim(-2, 2)
axs6.set_xlabel('Time (sec)')
axs6.set_ylabel('Spikes')
axs6.get_yaxis().set_ticks([])


# %% Plot 8: Recording fr with generator current
d2_rec_inst_fr_time = np.genfromtxt('./data/'
                                    'rec_disp2_run2_gen_inst_fr_time.csv',
                                    delimiter=',')
d4_rec_inst_fr_time = np.genfromtxt('./data/'
                                    'rec_disp4_run3_gen_inst_fr_time.csv',
                                    delimiter=',')
d2_rec_inst_fr_fr = np.genfromtxt('./data/rec_disp2_run2_gen_inst_fr_fr.csv',
                                  delimiter=',')
d4_rec_inst_fr_fr = np.genfromtxt('./data/rec_disp4_run3_gen_inst_fr_fr.csv',
                                  delimiter=',')
axs7.plot(d2_rec_inst_fr_time, d2_rec_inst_fr_fr, marker='.', linestyle='None',
          color='0.5')
axs7.plot(d4_rec_inst_fr_time, d4_rec_inst_fr_fr, marker='.', linestyle='None',
          color='0')
axs7.set_xlim(0, 2)
axs7.set_ylim(0, 200)
axs7.set_xlabel('Time (sec)')
axs7.set_ylabel('FR (Hz)')


# %%
fig.tight_layout()
fig.savefig('./F5 basic prediction/F5 basic prediction 2 sec.tif', dpi=600)
