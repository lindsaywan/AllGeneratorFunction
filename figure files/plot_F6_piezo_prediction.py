# -*- coding: utf-8 -*-
"""
Created on Mon May 25 16:00:55 2015

@author: Lindsay

This module plots currents and firing rate comparisons of model and recordings
under normal and Piezo2 deficient conditions.
"""

import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(5, 1, figsize=(3, 9))
for axes_id, axes in enumerate(axs.ravel()):
    axes.text(-.2, 1.1, chr(65+axes_id), transform=axes.transAxes,
              fontsize=12, fontweight='bold', va='top')
axs0 = axs[0]
axs1 = axs[1]
axs2 = axs[2]
axs3 = axs[3]
axs4 = axs[4]


# %% Plot 1: Piezo2: recording firing rates
rec_disp1_piezo_time, rec_disp1_piezo_fr = np.genfromtxt('./data/rec_disp1_'
                                                         'piezo_fr.csv',
                                                         delimiter=',').T
rec_disp2_piezo_time, rec_disp2_piezo_fr = np.genfromtxt('./data/rec_disp2_'
                                                         'piezo_fr.csv',
                                                         delimiter=',').T
axs0.plot(rec_disp1_piezo_time-1, rec_disp1_piezo_fr, marker='.',
          linestyle='None', color='0')
axs0.plot(rec_disp2_piezo_time-1, rec_disp2_piezo_fr, marker='.',
          linestyle='None', color='0.5')
axs0.set_xlim(0, 2)
axs0.set_ylim(0, 200)
axs0.set_xlabel('Time (sec)')
axs0.set_ylabel('FR (Hz)')


# %% Plot 2: Piezo2: original model firing rates
orig_d2_nr_fr_time = np.genfromtxt('./data/disp2_nr_inst_fr_time.csv',
                                   delimiter=',')
orig_d3_nr_fr_time = np.genfromtxt('./data/disp3_nr_inst_fr_time.csv',
                                   delimiter=',')
orig_d2_nr_fr_fr = np.genfromtxt('./data/disp2_nr_inst_fr_fr.csv',
                                 delimiter=',')
orig_d3_nr_fr_fr = np.genfromtxt('./data/disp3_nr_inst_fr_fr.csv',
                                 delimiter=',')
axs1.plot(orig_d2_nr_fr_time, orig_d2_nr_fr_fr, marker='.', linestyle='None',
          color='0.5')
axs1.plot(orig_d3_nr_fr_time, orig_d3_nr_fr_fr, marker='.', linestyle='None',
          color='0')
axs1.set_xlim(0, 2)
axs1.set_ylim(0, 200)
axs1.set_xlabel('Time (sec)')
axs1.set_ylabel('FR (Hz)')


# %% Plot 3: Piezo2: New approach 1 model firing rates
ap1_d2_nr_fr_time = np.genfromtxt('./data/ap1_disp2_nr_inst_fr_time.csv',
                                  delimiter=',')
ap1_d3_nr_fr_time = np.genfromtxt('./data/ap1_disp3_nr_inst_fr_time.csv',
                                  delimiter=',')
ap1_d2_nr_fr_fr = np.genfromtxt('./data/ap1_disp2_nr_inst_fr_fr.csv',
                                delimiter=',')
ap1_d3_nr_fr_fr = np.genfromtxt('./data/ap1_disp3_nr_inst_fr_fr.csv',
                                delimiter=',')
axs2.plot(ap1_d2_nr_fr_time, ap1_d2_nr_fr_fr, marker='.', linestyle='None',
          color='0.5')
axs2.plot(ap1_d3_nr_fr_time, ap1_d3_nr_fr_fr, marker='.', linestyle='None',
          color='0')
axs2.set_xlim(0, 2)
axs2.set_ylim(0, 200)
axs2.set_xlabel('Time (sec)')
axs2.set_ylabel('FR (Hz)')


# %% Plot 4: Piezo2: New approach 3 model firing rates
ap3_d2_nr_fr_time = np.genfromtxt('./data/ap3_disp2_nr_inst_fr_time.csv',
                                  delimiter=',')
ap3_d3_nr_fr_time = np.genfromtxt('./data/ap3_disp3_nr_inst_fr_time.csv',
                                  delimiter=',')
ap3_d2_nr_fr_fr = np.genfromtxt('./data/ap3_disp2_nr_inst_fr_fr.csv',
                                delimiter=',')
ap3_d3_nr_fr_fr = np.genfromtxt('./data/ap3_disp3_nr_inst_fr_fr.csv',
                                delimiter=',')
axs3.plot(ap3_d2_nr_fr_time, ap3_d2_nr_fr_fr, marker='.', linestyle='None',
          color='0.5')
axs3.plot(ap3_d3_nr_fr_time, ap3_d3_nr_fr_fr, marker='.', linestyle='None',
          color='0')
axs3.set_xlim(0, 2)
axs3.set_ylim(0, 200)
axs3.set_xlabel('Time (sec)')
axs3.set_ylabel('FR (Hz)')


# %% Plot 5: Piezo2: New approach 4 model firing rates
ap4_d2_nr_fr_time = np.genfromtxt('./data/ap4_disp2_nr+ia_inst_fr_time.csv',
                                  delimiter=',')
ap4_d3_nr_fr_time = np.genfromtxt('./data/ap4_disp3_nr+ia_inst_fr_time.csv',
                                  delimiter=',')
ap4_d2_nr_fr_fr = np.genfromtxt('./data/ap4_disp2_nr+ia_inst_fr_fr.csv',
                                delimiter=',')
ap4_d3_nr_fr_fr = np.genfromtxt('./data/ap4_disp3_nr+ia_inst_fr_fr.csv',
                                delimiter=',')
axs4.plot(ap4_d2_nr_fr_time, ap4_d2_nr_fr_fr, marker='.', linestyle='None',
          color='0.5')
axs4.plot(ap4_d3_nr_fr_time, ap4_d3_nr_fr_fr, marker='.', linestyle='None',
          color='0')
axs4.set_xlim(0, 2)
axs4.set_ylim(0, 200)
axs4.set_xlabel('Time (sec)')
axs4.set_ylabel('FR (Hz)')


# %%
fig.tight_layout()
fig.savefig('./F6 piezo prediction/F6 piezo prediction 2 sec.tif', dpi=600)
