#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 18:57:22 2018

@author: launy
"""

import json
import operator


class Json:
    factors={}
    connections={}
    tolist=[]
    position={}
    locations=[]
    sortposition={}
    def __init__(self):
        self.data = data
        self.Import()
    def Import():
        with open("kumu.json", "r") as read:
            out=json.load(read)
            From=len(out['connections'])
            for i in out['elements']:
                Json.factors[i['attributes']['label']]=i['_id']
    
