#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 12:04:06 2018

@author: launy
"""
import data
from indigoclass_V_3efix import *
from indigo_V_3efix import *
rang=5
storev=[0] * rang
storec=[0] * rang

class CG:
    def __init__(self):
        self.data = data
    def loop(pass_data):
        pass_data.jvalue = 0.0
        pass_data.jfix=3
        for i in range(rang):
            zzz.recalculate(pass_data)
            App.sumpn(pass_data)
            storec[i]=pass_data.jvalue
            storev[i]=pass_data.avg
            plt.close()
            if(i!=rang-1):
                zzz.resetIC()
                pass_data.jvalue += 0.01
           
