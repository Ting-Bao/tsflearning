import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
#https://stackoverflow.com/questions/16981921/relative-imports-in-python-3

from tsf_band_analysis.realign_band_plot_returndata import *

args = get_command_line_input()

def largest_negative_elements(arr):
    # Filter elements less than 0
    negative_elements = arr[arr < 0]
    
    # Sort the negative elements in ascending order
    sorted_negative_elements = np.sort(negative_elements)
    sorted_negative_elements = sorted_negative_elements[::-1]
    
    # Take the first ten elements
    largest_ten_negative_elements = sorted_negative_elements[:10]
    
    return largest_ten_negative_elements

def main():
    twcase = ["5.08", "4.4", "3.89", "3.48", "3.149657", "2.875895", "2.645908", "2.449977", "2.281060", "2.133930", "2.004628", "1.890099"]
    # twcase = twcase[:2]
    ranges = [0.2] * 6 + [0.1] * 6

    count_max = 10 # max number of bands to be averaged 
    appointed_band = [0,1,2,3,4,5] # 0-based, from near-fermi, the band to be compared

    compare_err = np.zeros(shape=(len(appointed_band)+1,len(twcase)),dtype=np.float64)
    compare_err_sperate = np.zeros(shape=(count_max//2, len(twcase)),dtype=np.float64)
    # appointed_band + mean

    load = False
    save_path = './tsf_band_analysis/compare_band_figs_train8/'
    if load == True:
        compare_err = np.load(os.path.join(save_path,'compare_err.npy'))
        compare_err_sperate = np.load(os.path.join(save_path,'compare_err_sperate.npy'))
        print('load compare_err.npy')
    else:
        for i in np.arange(len(twcase)):
            tw = twcase[i]
            twname = f'{round(float(tw), 2):.2f}'
            range = ranges[i]    
            args.path1 = f'./mote2_all_dft/{tw}'
            args.path2 = f'./0528_models_train8/{tw}'
            args.output = f'./tsf_band_analysis/compare_band_figs/'
            args.range = range
            args.name = twname
            band_data = compare_band(args) # openmx + nn
            band_data = [np.sort(i, axis=0) for i in band_data]
            opmx_band = band_data[0]
            nn_band = band_data[1]
            assert len(opmx_band[0]) == len(nn_band[0]), 'kpoints not match!'
            num_k = len(opmx_band[0])
            opmx_sort = np.zeros(shape=(count_max, num_k),dtype=np.float64)
            nn_sort = np.zeros(shape=(count_max, num_k),dtype=np.float64)
            for j in np.arange(num_k):
                opmx_sort[:,j] = largest_negative_elements(opmx_band[:,j])
                nn_sort[:,j] = largest_negative_elements(nn_band[:,j])

            # err of each band when aligned valance top
            for j in appointed_band:
                compare_err[j,i] += np.mean(np.abs(opmx_sort[j] - nn_sort[j]))
            
            # mean err
            compare_err[-1,i] += np.mean(np.abs(opmx_sort - nn_sort))

            # err of each band when aligned seperately, spin ignored
            for j in np.arange(0,count_max,2):
                no_spin_index = int(j//2)
                offset = np.mean(opmx_sort[j]) - np.mean(nn_sort[j])
                # spin has two bands
                high_err = np.mean(np.abs(opmx_sort[j] - nn_sort[j] - offset))
                low_err = np.mean(np.abs(opmx_sort[j+1] - nn_sort[j+1] - offset))
                compare_err_sperate[no_spin_index,i] += (high_err + low_err)/2
        
        # to meV
        compare_err *= 1000 # meV
        compare_err_sperate *= 1000 # meV
        np.save(os.path.join(save_path,'compare_err.npy'), compare_err)
        np.save(os.path.join(save_path,'compare_err_sperate.npy'), compare_err_sperate)

    
    # plot valance top aligned
    colors = ['royalblue','gray','orange','red']
    #colors = ['red', 'gray']
    
    x = [float(i) for i in twcase]

    if False:
        fig, ax = plt.subplots()
        plt.figure(figsize=(8, 6))
        font_size = 15
        band1_err = (compare_err[0] + compare_err[1])/2
        band2_err = (compare_err[2] + compare_err[3])/2
        band3_err = (compare_err[4] + compare_err[5])/2
        plt.plot(x, band1_err, 'o-', label='band1') # consider spin degeneracy
        plt.plot(x, band2_err, 'o-', label='band2')
        plt.plot(x, band3_err, 'o-', label='band3')
        plt.plot(x, compare_err[-1], 'o-', label='mean')
        plt.legend(loc='upper right', fontsize = font_size)
        plt.xticks([round(i,2) for i in x],rotation=45, fontsize = font_size)
        plt.yticks(fontsize = font_size)
        plt.xlabel('twist angle', fontsize = font_size)
        plt.ylabel('error (meV)', fontsize = font_size)
        plt.ylim(0.2, 1.8)
        plt.title('band error (valance top aligned)', fontsize = 1.5* font_size)
        plt.savefig(f'{save_path}/band_error_aligntop.png',dpi=300)
        plt.close()

    # plot sperately aligned
    if True:
        plt.figure(figsize=(6,6))
        font_size = 15
        label_size = 15
        ax = plt.gca()
        ax.xaxis.set_ticks_position('both')
        ax.yaxis.set_ticks_position('both')
        ax.tick_params(axis='both', which='major', direction = 'in',length=3,width=1,labelsize=label_size)
        #x = [float(i) for i in twcase]
        # x = np.arange(len(x))
        band1_err = compare_err_sperate[0]
        band2_err = compare_err_sperate[1]
        band3_err = compare_err_sperate[2]
        mean_err = np.mean(compare_err_sperate, axis=0)
        plt.plot(x, band1_err, 'o--',linewidth = 3, markersize=8,alpha = 0.7, label=r'1${}^{st}$ band',color=colors[0] ) # consider spin degeneracy
        plt.plot(x, band2_err, 'o--',linewidth = 3, markersize=8,alpha = 0.7, label=r'2${}^{nd}$ band',color=colors[1])
        plt.plot(x, band3_err, 'o--',linewidth = 3, markersize=8,alpha = 0.7, label=r'3${}^{rd}$ band',color=colors[2])
        plt.plot(x, mean_err, 'o-',linewidth = 3, markersize=10, label='Averaged',color=colors[3])
        plt.legend(loc='upper right',fontsize=font_size)
        plt.xlabel(r'Twist angle (${}^\circ$)',fontsize=label_size)
        plt.ylabel('Band MAE (meV)',fontsize=label_size)
        plt.xticks(x,[f'{round(float(i),2):.2f}' for i in x], rotation=90, fontsize=font_size)
        plt.yticks(np.arange(0.25,2.25,0.25),fontsize=font_size)
        plt.ylim(0.25, 2.0)
        # plt.title('band error (sperately aligned)',fontsize=1.5* font_size)    

        ax.xaxis.set_ticks_position('both')
        # ax.yaxis.set_ticks_position('left')
        ax.tick_params(axis='x', which='major', direction = 'in',length=3,width=1,labelsize=label_size-3)
        # ax.ticklabel_format(style='sci', scilimits=(-1,2), axis='y')
        ax.tick_params(axis='y', which='major', direction = 'in',length=3,width=1,labelsize=label_size)
    
        plt.tight_layout()
        plt.savefig(f'{save_path}/band_error_alignsperately.png',dpi=300)
        plt.savefig(f'{save_path}/band_error_alignsperately.pdf',dpi=300)
        plt.savefig(f'{save_path}/band_error_alignsperately.svg',dpi=300) 
        plt.close()


    # plot each band aligned seperately


if __name__ == '__main__':
    main()