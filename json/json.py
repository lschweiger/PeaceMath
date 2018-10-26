#!/usr/bin/env python3

"""
-------------------------------------------------------------------------------
MIT License Copyright (c) 2018 Launy Schweiger
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
-------------------------------------------------------------------------------
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
    new=[]
    def __init__(self):
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
            remove=out['perspectives'][0]['style']
            print(remove)
            
            for i in remove:
                #print(i)
                if (i==""): print(i)
                #print(i)
                #new=new.append(i)
        #print(remove)
    def Sort():
        Json.sortposition=sorted(Json.position.items(),key=operator.itemgetter(0))

def main():
    Json.Import()
    Json.Sort()
if __name__=='__main__':
    main()
    #print(Json.sortposition)
    #print(Json.factors)
    #print(Json.connections)
