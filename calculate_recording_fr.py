# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 16:33:50 2015

@author: Lindsay

This module calculates firing rates from recordings, or fits the firing rate
curves (commented).
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from scipy.optimize import curve_fit
from scipy.interpolate import interp1d

LIF_RESOLUTION = 0.1
DURATION = 6000

def spike_time_to_trace(spike_time):
    """
    Transfer spike time to spike trace.

    Parameters
    ----------
    spike_time : 1d-array
        The time points of all the spikes in msec.

    Returns
    -------
    spike_trace : 2d-array
        [0] = time increments in the total duration.
        [1] = 1 if there is a spike at this time, 0 otherwise.
    """
    spike_trace = np.zeros([int(DURATION/LIF_RESOLUTION)+1, 2])
    spike_trace[:, 0] = np.arange(0, DURATION+LIF_RESOLUTION, LIF_RESOLUTION)
    spike_trace[(spike_time / LIF_RESOLUTION).astype(int), 1] = 1
    return spike_trace

def func_exp(x, a, b, c, d):
    y = a * np.exp(b * x) + c * np.exp(d*x)
    return y


def get_sse(xfit, scale, func, x, y):
    params = xfit * scale
    ynew = func(params, x)
    residual = ynew - y
    sse = (residual ** 2).sum()
    print(params, sse)
    return sse


if __name__ == '__main__':
#    spike_time = np.genfromtxt('./Yoshi recordings data/'
#                               'spike_time_disp2_run2.csv', delimiter=',')
    spike_time = np.genfromtxt('./figure files/data/'
                               'ap3_disp2_gen_spike.csv', delimiter=',')
    spike_trace = spike_time_to_trace(spike_time*1000)
    inst_fr = np.r_[0, 1/np.diff(spike_time)]
    inst_fr_index = spike_trace[:,1].nonzero()[0]
    inst_fr_time = inst_fr_index * LIF_RESOLUTION / 1000
    fig0, axs0 = plt.subplots()
    axs0.plot(inst_fr_time, inst_fr, marker='.', linestyle='None')
# %% Choose a point to start fitting: disp2
    # recordings
#    inst_fr_time = inst_fr_time[1:-9]
#    inst_fr = inst_fr[1:-9]
    # recordings
#    inst_fr_time = inst_fr_time[3:]
#    inst_fr = inst_fr[3:]
    # New approach 1
#    inst_fr_time = inst_fr_time[13:]
#    inst_fr = inst_fr[13:]
    # New approach 2
#    inst_fr_time = inst_fr_time[12:]
#    inst_fr = inst_fr[12:]
    # New approach 3
    inst_fr_time = inst_fr_time[13:]
    inst_fr = inst_fr[13:]

# %% Choose a point to start fitting: disp3
    # recordings
#    inst_fr_time = inst_fr_time[4:-8]
#    inst_fr = inst_fr[4:-8]
    # recordings
#    inst_fr_time = inst_fr_time[4:]
#    inst_fr = inst_fr[4:]
    # New approach 1
#    inst_fr_time = inst_fr_time[20:]
#    inst_fr = inst_fr[20:]
    # New approach 2
#    inst_fr_time = inst_fr_time[19:]
#    inst_fr = inst_fr[19:]
    # New approach 3
#    inst_fr_time = inst_fr_time[21:]
#    inst_fr = inst_fr[21:]
#%% Fitting fr curve
    popt, pcov = curve_fit(func_exp, inst_fr_time, inst_fr, p0=[100, -1, 10, -1])
    fig, axs = plt.subplots()
    a, b, c, d = popt
    fit_fr = a*np.exp(inst_fr_time*b) + c*np.exp(inst_fr_time*d)
    axs.plot(inst_fr_time, inst_fr, color='0.5')
    axs.plot(inst_fr_time, fit_fr, color='0')
    print(a)
    print(-1/b)
    print(c)
    print(-1/d)
#    np.savetxt('fit_rec_disp4_run3_time.csv', inst_fr_time)
#    np.savetxt('fit_rec_disp4_run3_fr.csv', fit_fr)


#%% calculate fr
#    max_index = 3901 # disp2 run2
    max_index = 4352 # disp4 run3
    ramp_index = spike_trace[0:max_index,1].nonzero()[0]
    ramp_spike_time = spike_trace[ramp_index, 0]
    ramp_fr = np.mean(1000/np.diff(ramp_spike_time))
    # Get early-hold fr
    early_index = spike_trace[max_index:max_index+5000,1].nonzero()[0]
    early_spike_time = spike_trace[early_index, 0]
    early_fr = np.mean(1000/np.diff(early_spike_time))
    # Get late-hold fr
    late_index = spike_trace[2000/LIF_RESOLUTION:4500/LIF_RESOLUTION,1].nonzero()[0]
    late_spike_time = spike_trace[late_index, 0]
    late_fr = np.mean(1000/np.diff(late_spike_time))
    print('ramp fr = ', ramp_fr)
    print('early hold fr = ', early_fr)
    print('late hold fr = ', late_fr)
#%% Plot fr ratio
#    fr_ratio = np.genfromtxt('D:/GradResearch/LIFImprovement/Documents/'
#                             'firing rates ratio.csv', delimiter=',')
#    fig, axs = plt.subplots()
#    x = np.arange(1,4)
#    axs.plot(x, fr_ratio[0,], color='0.5', linestyle='--')
#    axs.plot(x, fr_ratio[1,], color='0', linestyle='--')
##    axs.plot(x, fr_ratio[2,], color='0.5', linestyle=':')
##    axs.plot(x, fr_ratio[3,], color='0', linestyle=':')
#    for i in range(4):
#        axs.plot(x, fr_ratio[i+4,], color='0.5')
#    for j in range(4):
#        axs.plot(x, fr_ratio[j+8,], color='0')