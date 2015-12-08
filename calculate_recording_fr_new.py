# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 17:02:40 2015

@author: Lindsay
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 16:33:50 2015

@author: Lindsay

This module calculates firing rates from recordings, or fits the firing rate
curves (commented).
"""

import numpy as np
import matplotlib.pyplot as plt

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


if __name__ == '__main__':
    new_time = np.arange(0, 10, 6.25e-5)
    spike = np.genfromtxt('./figure files/data/NaturePaperGraphsData/'
                                  'Piezo2CONT_cs_2.csv', delimiter=',')[:, 0]
    fr_index = spike.nonzero()[0]
    fr_time = new_time[fr_index]
    fr_fr = np.r_[0, 1/np.diff(fr_time)]
    fig0, axs0 = plt.subplots()
    axs0.plot(fr_time, fr_fr, marker='.', linestyle='None')
    max_index = fr_fr.argmax()
    ramp_fr = np.mean(fr_fr[0:max_index])
    before_early = fr_time[fr_time <=fr_time[max_index]+0.5]
    early_index = before_early.argmax()
    early_fr = np.mean(fr_fr[max_index:early_index+1])
    late_prd = fr_time[((fr_time[0]+2)<fr_time)*(fr_time<(fr_time[0]+4.5))]
    late_start_index = np.where(fr_time==late_prd[0])[0][0]
    late_end_index = np.where(fr_time==late_prd[-1])[0][0]
    late_fr = np.mean(fr_fr[late_start_index:late_end_index])
    print('ramp fr = ', ramp_fr)
    print('early hold fr = ', early_fr)
    print('late hold fr = ', late_fr)
    np.savetxt("P2CONT_rec_disp2_gen_inst_fr_time.csv", fr_time, delimiter=",")
    np.savetxt("P2CONT_rec_disp2_gen_spike.csv", fr_time, delimiter=",")
    np.savetxt("P2CONT_rec_disp2_gen_inst_fr_fr.csv", fr_fr, delimiter=",")
    np.savetxt("P2CONT_rec_disp2_normal_fr.csv", fr_fr, delimiter=",")
