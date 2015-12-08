# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 15:53:37 2015

@author: Lindsay
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

new_time = np.arange(0, 10, 6.25e-5)


# %% Plot 7: Recording spike with generator current
d2_rec_gen_spike = np.genfromtxt('./data/rec_disp2_run2_gen_spike.csv',
                                 delimiter=',')
d4_rec_gen_spike = np.genfromtxt('./data/rec_disp4_run3_gen_spike.csv',
                                 delimiter=',')
axs0.vlines(d2_rec_gen_spike, ymin=-1.5, ymax=-0.5, linewidth=0.5, color='0.5')
axs0.axhline(y=-1, xmin=0, xmax=5, linewidth=0.5, color='0.5')
axs0.vlines(d4_rec_gen_spike, ymin=0.5, ymax=1.5, linewidth=0.5, color='0')
axs0.axhline(y=1, xmin=0, xmax=5, linewidth=0.1, color='0')
axs0.set_xlim(0, 5)
axs0.set_ylim(-2, 2)
axs0.set_xlabel('Time (sec)')
axs0.set_ylabel('Spikes')
axs0.get_yaxis().set_ticks([])


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
axs1.plot(d2_rec_inst_fr_time, d2_rec_inst_fr_fr, marker='.', linestyle='None',
          color='0.5')
axs1.plot(d4_rec_inst_fr_time, d4_rec_inst_fr_fr, marker='.', linestyle='None',
          color='0')
axs1.set_xlim(0, 5)
axs1.set_ylim(0, 300)
axs1.set_xlabel('Time (sec)')
axs1.set_ylabel('FR (Hz)')

# %% Piezo2 Control
p2ctl_s_spike = np.genfromtxt('./data/NaturePaperGraphsData/'
                              'Piezo2CONT_cs_3.csv', delimiter=',')[:, 0]
p2ctl_s_fr_index = p2ctl_s_spike.nonzero()[0]
p2ctl_s_fr_time = new_time[p2ctl_s_fr_index]
p2ctl_s_fr_fr = np.r_[0, 1/np.diff(p2ctl_s_fr_time)]
p2ctl_m_spike = np.genfromtxt('./data/NaturePaperGraphsData/'
                              'Piezo2CONT_cs_2.csv', delimiter=',')[:, 0]
p2ctl_m_fr_index = p2ctl_m_spike.nonzero()[0]
p2ctl_m_fr_time = new_time[p2ctl_m_fr_index]
p2ctl_m_fr_fr = np.r_[0, 1/np.diff(p2ctl_m_fr_time)]
p2ctl_l_spike = np.genfromtxt('./data/NaturePaperGraphsData/'
                              'Piezo2CONT_cs_1.csv', delimiter=',')[:, 0]
p2ctl_l_fr_index = p2ctl_l_spike.nonzero()[0]
p2ctl_l_fr_time = new_time[p2ctl_l_fr_index]
p2ctl_l_fr_fr = np.r_[0, 1/np.diff(p2ctl_l_fr_time)]
axs2.vlines(p2ctl_s_fr_time-p2ctl_s_fr_time[0], ymin=-1.5, ymax=-0.5, linewidth=0.5, color='0.5')
axs2.axhline(y=-1, xmin=0, xmax=5, linewidth=0.5, color='0.5')
axs2.vlines(p2ctl_l_fr_time-p2ctl_l_fr_time[0], ymin=0.5, ymax=1.5, linewidth=0.5, color='0')
axs2.axhline(y=1, xmin=0, xmax=5, linewidth=0.1, color='0')
axs2.set_xlim(0, 5)
axs2.set_ylim(-2, 2)
axs2.set_xlabel('Time (sec)')
axs2.set_ylabel('Spikes')
axs2.get_yaxis().set_ticks([])
axs3.plot(p2ctl_s_fr_time-p2ctl_s_fr_time[0], p2ctl_s_fr_fr, marker='.', linestyle='None',
          color='0.5')
axs3.plot(p2ctl_l_fr_time-p2ctl_l_fr_time[0], p2ctl_l_fr_fr, marker='.', linestyle='None',
          color='0')
axs3.set_xlim(0, 5)
axs3.set_ylim(0, 300)
axs3.set_xlabel('Time (sec)')
axs3.set_ylabel('FR (Hz)')


# %% Piezo2 CKO
p2cko_s_spike = np.genfromtxt('./data/NaturePaperGraphsData/'
                              'Piezo2CKO_cs_3.csv', delimiter=',')[:, 0]
p2cko_s_fr_index = p2cko_s_spike.nonzero()[0]
p2cko_s_fr_time = new_time[p2cko_s_fr_index]
p2cko_s_fr_fr = np.r_[0, 1/np.diff(p2cko_s_fr_time)]
p2cko_m_spike = np.genfromtxt('./data/NaturePaperGraphsData/'
                              'Piezo2CKO_cs_2.csv', delimiter=',')[:, 0]
p2cko_m_fr_index = p2cko_m_spike.nonzero()[0]
p2cko_m_fr_time = new_time[p2cko_m_fr_index]
p2cko_m_fr_fr = np.r_[0, 1/np.diff(p2cko_m_fr_time)]
p2cko_l_spike = np.genfromtxt('./data/NaturePaperGraphsData/'
                              'Piezo2CKO_cs_1.csv', delimiter=',')[:, 0]
p2cko_l_fr_index = p2cko_l_spike.nonzero()[0]
p2cko_l_fr_time = new_time[p2cko_l_fr_index]
p2cko_l_fr_fr = np.r_[0, 1/np.diff(p2cko_l_fr_time)]
axs4.vlines(p2cko_s_fr_time-p2cko_s_fr_time[0], ymin=-1.5, ymax=-0.5, linewidth=0.5, color='0.5')
axs4.axhline(y=-1, xmin=0, xmax=5, linewidth=0.5, color='0.5')
axs4.vlines(p2cko_l_fr_time-p2cko_l_fr_time[0], ymin=0.5, ymax=1.5, linewidth=0.5, color='0')
axs4.axhline(y=1, xmin=0, xmax=5, linewidth=0.1, color='0')
axs4.set_xlim(0, 5)
axs4.set_ylim(-2, 2)
axs4.set_xlabel('Time (sec)')
axs4.set_ylabel('Spikes')
axs4.get_yaxis().set_ticks([])
axs5.plot(p2cko_s_fr_time-p2cko_s_fr_time[0], p2cko_s_fr_fr, marker='.', linestyle='None',
          color='0.5')
axs5.plot(p2cko_l_fr_time-p2cko_l_fr_time[0], p2cko_l_fr_fr, marker='.', linestyle='None',
          color='0')
axs5.set_xlim(0, 5)
axs5.set_ylim(0, 300)
axs5.set_xlabel('Time (sec)')
axs5.set_ylabel('FR (Hz)')


# %% Atoh1 CKO
a1cko_s_spike = np.genfromtxt('./data/NaturePaperGraphsData/'
                              'Atoh1CKO_cs_3.csv', delimiter=',')[:, 0]
a1cko_s_fr_index = a1cko_s_spike.nonzero()[0]
a1cko_s_fr_time = new_time[a1cko_s_fr_index]
a1cko_s_fr_fr = np.r_[0, 1/np.diff(a1cko_s_fr_time)]
a1cko_m_spike = np.genfromtxt('./data/NaturePaperGraphsData/'
                              'Atoh1CKO_cs_2.csv', delimiter=',')[:, 0]
a1cko_m_fr_index = a1cko_m_spike.nonzero()[0]
a1cko_m_fr_time = new_time[a1cko_m_fr_index]
a1cko_m_fr_fr = np.r_[0, 1/np.diff(a1cko_m_fr_time)]
a1cko_l_spike = np.genfromtxt('./data/NaturePaperGraphsData/'
                              'Atoh1CKO_cs_1.csv', delimiter=',')[:, 0]
a1cko_l_fr_index = a1cko_l_spike.nonzero()[0]
a1cko_l_fr_time = new_time[a1cko_l_fr_index]
a1cko_l_fr_fr = np.r_[0, 1/np.diff(a1cko_l_fr_time)]
axs6.vlines(a1cko_s_fr_time-a1cko_s_fr_time[0], ymin=-1.5, ymax=-0.5, linewidth=0.5, color='0.5')
axs6.axhline(y=-1, xmin=0, xmax=5, linewidth=0.5, color='0.5')
axs6.vlines(a1cko_l_fr_time-a1cko_l_fr_time[0], ymin=0.5, ymax=1.5, linewidth=0.5, color='0')
axs6.axhline(y=1, xmin=0, xmax=5, linewidth=0.1, color='0')
axs6.set_xlim(0, 5)
axs6.set_ylim(-2, 2)
axs6.set_xlabel('Time (sec)')
axs6.set_ylabel('Spikes')
axs6.get_yaxis().set_ticks([])
axs7.plot(a1cko_s_fr_time-a1cko_s_fr_time[0], a1cko_s_fr_fr, marker='.', linestyle='None',
          color='0.5')
axs7.plot(a1cko_l_fr_time-a1cko_l_fr_time[0], a1cko_l_fr_fr, marker='.', linestyle='None',
          color='0')
axs7.set_xlim(0, 5)
axs7.set_ylim(0, 300)
axs7.set_xlabel('Time (sec)')
axs7.set_ylabel('FR (Hz)')