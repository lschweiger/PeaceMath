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
    
            for j in range(0,From):
                for k in range(0,From):
                    if((out['connections'][j]['from'])==out['connections'][k]['from']):
                        Json.tolist.append(out['connections'][k]['to'])
                        Json.connections[out['connections'][j]['from']]=Json.tolist
                Json.tolist=[]
            for l in range(0,(len(out['maps'][0]['elements']))):
                Json.locations.append(out['maps'][0]['elements'][l]['position'])
                Json.position[out['maps'][0]['elements'][l]['element']]=Json.locations[l]
            Json.locations=[]
    def Sort():
        Json.sortposition=sorted(Json.position.items(),key=operator.itemgetter(0))

def main():
    Json.Import()
    Json.Sort()
if __name__=='__main__':
    main()
    print(Json.sortposition)
    print(Json.factors)
    print(Json.connections)