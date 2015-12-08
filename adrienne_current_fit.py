# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 00:22:47 2015

@author: Lindsay

This module fits the current data from Adrienne Dubin's neuron current
recordings.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize


def func_exp(params, x):
    a, b = params
    y = a * np.exp(b * x)
    return y


def get_sse(params, func, x, y):
    ynew = func(params, x)
    residual = ynew - y
    sse = (residual ** 2).sum()
    return sse


def multi_curve_fit(x, y, x0, bounds):
    fit_params_list = []
    for i, yi in enumerate(y.T):
        result = minimize(get_sse, x0, args=(func_exp, x, yi),
                          method='SLSQP', bounds=bounds)
        fit_params_list.append(result.x)
    fit_params_array = np.array(fit_params_list)
    x0_new = np.median(fit_params_array, axis=0)
    fit_params_list_new = []
    for i, yi in enumerate(y.T):
        result = minimize(get_sse, x0_new, args=(func_exp, x, yi),
                          method='SLSQP', bounds=bounds)
        fit_params_list_new.append(result.x)
    fit_params_array_new = np.array(fit_params_list_new)
    fit_params_final = np.median(fit_params_array_new, axis=0)
    return fit_params_final

if __name__ == '__main__':
    # Neuron current traces
    traces = np.loadtxt('./Adrienne recordings data/Organized data/'
                        'Neuron Current/Cur_4092014P102RA_2dprocesses.csv',
                        delimiter=',')
    stimul = np.loadtxt('./Adrienne recordings data/Organized data/'
                        'Neuron Current/Disp_4092014P102RA_2dprocesses.csv',
                        delimiter=',')
    # %% Examine the data
    t = traces[:, 0]
    v = traces[:, 1:]
    s = stimul[:, 1:]
    fit_num = 0
    fig, axs = plt.subplots()
    volt_plot = axs.plot(t, v, c='0.7')
    volt_plot = axs.plot(t, v[:, fit_num:], c='0')
    fig2, axs2 = plt.subplots()
    stimul_plot = axs2.plot(t, s, c='0')
    stimul_plot = axs2.plot(t, s[:, fit_num], c='0')
    # %% Set parameters and fit the curves
    fs = 5e-5  # in sec, sampling frequency
    crop_start = 0.07  # in sec
    crop_end = 0.1
    fit_start_index = (np.ones(v.shape[1])*crop_start/fs).astype(int)
    fit_end_index = (np.ones(v.shape[1])*crop_end/fs).astype(int)
    for k in range(fit_num, v.shape[1]):
        fit_start_index[k] = fit_start_index[k] + \
                             np.argmin(v[fit_start_index[k]:fit_end_index[k],
                                         k])
    threshold = np.zeros(v.shape[1])
    thres_start = 0.06
    thres_end = 0.07
    thres_start_index = (int)(thres_start/fs)
    thres_end_index = (int)(thres_end/fs)
    for m in range(0, v.shape[1]):
        threshold[m] = np.mean(v[thres_start_index:thres_end_index, m])
    fit_start = fit_start_index * fs
    # Neuron current x0
    x0 = np.array((-100, -100))
    bounds = ((None, 0), (None, 0))
    fit_params_list = []
    for i, trace in enumerate(traces.T[1:]):
        time_interval = t[fit_start_index[i]:fit_end_index[i]] - fit_start[i]
        voltage = trace[fit_start_index[i]:fit_end_index[i]] - threshold[i]
        result = minimize(get_sse, x0, args=(func_exp, time_interval, voltage),
                          method='SLSQP', bounds=bounds)
        fit_params_list.append(result.x)
    fit_params_array = np.array(fit_params_list)
    # plot fit traces
    fig3, axs3 = plt.subplots()
    plot_from = 0
    for j in range(plot_from, v.shape[1]-1):
        a, b = fit_params_array[j, :]
        time_interval = t[fit_start_index[j]:fit_end_index[i]] - fit_start[j]
        fit_trace = a*np.exp(time_interval*b) + threshold[j]
        fit_plot = axs3.plot(t, v[:, j], c='0.7')
        fit_plot = axs3.plot(time_interval+fit_start[j], fit_trace, c='k')
    axs3.set_xlim(0.07, 0.12)
    axs3.set_ylim(-1200, -600)
#    np.savetxt('current_fit.csv', fit_trace, delimiter=',')
#    np.savetxt('current_fit_time.csv', time_interval+fit_start[j],
#    delimiter=',')
