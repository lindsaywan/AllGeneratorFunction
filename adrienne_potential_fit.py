# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 00:22:47 2015

@author: Lindsay

This module fits the potential data by Adrienne Dubin from Merkel cell
potential recordings.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize


def func_exp(params, x):
    a, b, c = params
    y = a * np.exp(b * x) + c
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
    # Merkel cell voltage traces
    traces = np.loadtxt('./Adrienne recordings data/Organized data/'
                        'Merkel cell potential/Vol_614D 028 mechano in CC.csv',
                        delimiter=',')
    stimul = np.loadtxt('./Adrienne recordings data/Organized data/'
                        'Merkel cell potential/'
                        'Disp_614D 028 mechano in CC.csv', delimiter=',')
    # %% Examine the data
    t = traces[:, 0]
    v = traces[:, 1:]
    s = stimul[:, 1:]
    fit_num = 0
    mc_pot_rcd = v[:, fit_num]
    fig, axs = plt.subplots()
    volt_plot = axs.plot(t, v, c='0')
    volt_plot = axs.plot(t, v[:, fit_num], c='0')
    fig2, axs2 = plt.subplots()
    stimul_plot = axs2.plot(t, s, c='0.7')
    stimul_plot = axs2.plot(t, s[:, fit_num], c='0')
    # %% Set parameters and fit the curves
    fs = 5e-5  # in sec, sampling frequency
    # starting points
#    fit_start = np.array([0.05, 0.05, 0.07, 0.07, 0.05, 0.046, 0.044])  # 621A 004
    fit_start = np.array([0.05, 0.05, 0.06, 0.056, 0.05, 0.058, 0.048])  # 614D 028
#    fit_start = np.array([0.05, 0.05, 0.06, 0.06, 0.048, 0.06, 0.05, 0.056, 0.061])  # 614C 018
    fit_end = 0.13 # in sec
    fit_start_index = (fit_start/fs).astype(int)
    fit_end_index = round(fit_end/fs)
    # Merkel cell voltage x0
    x0 = np.array((10, -10, -60))
    # Neuron current x0
    bounds = ((0, None), (None, 0), (-91, 0))
    # %% Curve fit in main cell
    fit_params_list = []
    for i, trace in enumerate(traces.T[1:]):
        time_interval = t[fit_start_index[i]:fit_end_index] - fit_start[i]
        voltage = trace[fit_start_index[i]:fit_end_index]
        result = minimize(get_sse, x0, args=(func_exp, time_interval, voltage),
                          method='SLSQP', bounds=bounds)
        fit_params_list.append(result.x)
    fit_params_array = np.array(fit_params_list)
    # Plot multiple fit curves
    fig3, axs3 = plt.subplots()
    plot_from = 0
    for j in range(plot_from, v.shape[1]-1):
        a,b,c = fit_params_array[j, :]
        time_interval = t[fit_start_index[j]:fit_end_index] - fit_start[j]
        fit_trace = a*np.exp(time_interval*b)+c
        fit_plot = axs3.plot(t, v[:, j], c='0.7')
        fit_plot = axs3.plot(time_interval+fit_start[j], fit_trace, c='k')
        axs3.set_xticks(np.arange(min(t), max(t), 0.1))
        axs3.set_yticks(np.arange(-60, 20, 20))
    fig3.tight_layout()
#    np.savetxt('voltage_fit.csv', fit_trace, delimiter=',')
#    np.savetxt('voltage_fit_time.csv', time_interval+fit_start[j], delimiter=',')
