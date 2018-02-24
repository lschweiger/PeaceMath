#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 12:04:06 2018

@author: launy
"""
import data
from indigoclass_V_3efix import *
from indigo_V_3efix import *
import matplotlib.pyplot as plt
rang=14
#rang=100
storev=[0] * rang
storec=[0] * rang

class CG:
    def __init__(self):
        self.data = data
    def loop(pass_data):
        pass_data.hold=1
        pass_data.jvalue = 0.86
        pass_data.jfix=0
        
        for i in range(rang):
            #zzz.recalculate(pass_data) make the gui recalculate 
            zzz.recalculate(pass_data)
            #App.sumpn(pass_data) runs the sumpn from indigoclass
            App.sumpn(pass_data)
            #print(pass_data.avgneg)
            #print(pass_data.avgpos)
            #stores values of every run, so it can be used in graphing
            storec[i]=pass_data.jvalue
            storev[i]=pass_data.avg
            #plt.close() will close all opened figures, so as not to cloter the screen
            plt.close()
            if(i!=rang-1):
                #resets z[-1] to ic for next recalcution and increments constants held 
                zzz.resetIC()
                pass_data.jvalue += 0.01
           
class plot:
    def plot(x,y):
       plt.plot(x,y,color='k',marker='o',markerfacecolor='r')
       plt.show()
run=CG.loop(pass_data)