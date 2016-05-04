# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 21:51:25 2016

@author: David
"""
colorDict={'Drumhead_0':'bo','Cross_1000':'ro', 'Cross_600':'go'}
colorDict2={'Drumhead0':'bs','Cross1000':'rs', 'Cross600':'gs'}
meandict={'Drumhead0':'b+','Cross1000':'r+', 'Cross600':'g+'}

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
def returnUnique(data, column_key):
    items=data[column_key].unique()
    return items
    
def func(data, colorDict, fig, ax, meandict):
#Replace white spaceses in column names
    data.columns = [c.replace(' ', '_') for c in data.columns]
#Changes all Non-Sensicle widths
    data.Device_Width[data['Device_Type'].isin(['Drumhead', 'Other'])] = 0
#Find Unique Device Types
    uniqueDeviceTypes=returnUnique(data, 'Device_Type')
    devicetypes=[]
    for i in uniqueDeviceTypes:
        print uniqueDeviceTypes
#Create a sub-dataframe for each unique device type
        uniqueDeviceTypeData=data[data['Device_Type'].isin([i])]
        uniqueWidths=returnUnique(uniqueDeviceTypeData, 'Device_Width')
        for ii in uniqueWidths:
            print uniqueWidths
#Create a sub-dataFRame for each unique device width
            uniqueWidthData=uniqueDeviceTypeData[uniqueDeviceTypeData['Device_Width'].isin([ii])]
            d={'f':np.array(uniqueWidthData.Frequency),'Q':np.array(uniqueWidthData.Q)}
            df=pd.DataFrame(d)
            devicetypes.append([i+'_'+str(int(ii)),df])
    return devicetypes
#For harmonic studies, could go one step furthur and look at all harmonics




#Gives list of all device types

def regionsplot(data1, data2):
    fig = plt.figure()
    ax=fig.add_subplot(111)
    func(data1,colorDict1,fig,ax)
    func(data2,colorDict2,fig,ax)


def plotboth(data):
    font = { 'family' : 'Ariel',
        'weight' : 'normal',
        'size'   : 16}

    matplotlib.rc('font', **font)
    colorDict={'Drumhead_0':'bo','Cross_1000':'r+', 'Cross_600':'g+'}
    meanDict={'Drumhead_0':'bo','Cross_1000':'r+', 'Cross_600':'g+'}
    labelDict={'Drumhead_0':'bo','Cross_1000':'ro', 'Cross_600':'go'}
    mewDict={'Drumhead_0':2,'Cross_1000':3, 'Cross_600':2}
    msDict={'Drumhead_0':7,'Cross_1000':8, 'Cross_600':8}
    meanmewDict={'Drumhead_0':3,'Cross_1000':3, 'Cross_600':3}
    meanmsDict={'Drumhead_0':8,'Cross_1000':8, 'Cross_600':8}
    markeredgecolorDict={'Drumhead_0':'b','Cross_1000':'r', 'Cross_600':'g'}
    fig = plt.figure()
    ax=fig.add_subplot(111)
    sorteddata = func(data,colorDict,fig,ax, meandict)
    for i in sorteddata:
        ax.plot(i[1].f/10**6,i[1].Q, colorDict[i[0]], mew=mewDict[i[0]], ms=msDict[i[0]], label=labelDict[i[0]],markeredgecolor=markeredgecolorDict[i[0]])
#        ax.plot(i[1].f/10**6,i[1].Q, colorDict[i[0]], mew=mewDict[i[0]], ms=msDict[i[0]], label=labelDict[i[0]], markerfacecolor='none',markeredgecolor=markeredgecolorDict[i[0]])

#        ax.plot([0,i[1].f.mean()/10**6],[0,i[1].Q.mean()], linewidth=3)
        Qerr = i[1].Q.std()
        ferr = i[1].f.std()/10**6
#        ax.errorbar(i[1].f.mean()/10**6, i[1].Q.mean(), yerr=Qerr, xerr=ferr, fmt = meanDict[i[0]][1], color =meanDict[i[0]][0]  ,mew=meanmewDict[i[0]], ms=meanmsDict[i[0]], markeredgecolor=markeredgecolorDict[i[0]] )
        ax.errorbar(i[1].f.mean()/10**6, i[1].Q.mean(), yerr=Qerr, xerr=ferr, fmt ='none', color =meanDict[i[0]][0]  ,mew=meanmewDict[i[0]], ms=meanmsDict[i[0]], markeredgecolor=markeredgecolorDict[i[0]] )
        print i[0]        
        print i[1].f.mean()/10**6, ferr, i[1].Q.mean(), Qerr   
    ax.set_xlim([1*10,2.5*10])
    ax.set_ylim([40,250])
    labelfont = {'fontname':'Ariel'}
    ax.set_xlabel('Frequency (MHz)', **labelfont)
    ax.set_ylabel('Quality Factor', **labelfont)
#    plt.legend()
    fig.tight_layout()
    fig.savefig('Z:\Group\Projects\FIBed Graphene Drumhead Resonators\Measurement Data\Plots\Test.pdf', format='pdf')
"""    ax.tick_params(axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom='on',      # ticks along the bottom edge are off
    top='off',         # ticks along the top edge are off
    labelbottom='off')"""
    


def plot(dx,dy,cx,cy, drumfit, crossfit):
    plt.plot(dx/10**6,dy, 'ro', Label = 'Drumhead')
    plt.plot(dx/10**6,drumfit, 'r',lw=1.5, Label=None)
    plt.plot(cx/10**6,cy, 'b+', Label = 'Cross')
    plt.plot(cx/10**6,crossfit, 'b', lw=1.5, Label=None)
    plt.legend(loc='center')
    plt.xlabel('Frequency (MHz)')
    plt.ylabel('Vibrational Amplitude (a.u.)')
    plt.show()
