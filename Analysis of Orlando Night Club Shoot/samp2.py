'''This file is to find the follower ids in any number of batches inorder to not to reach the maximum API limit '''
from __future__ import print_function

#print("test", file=log)
#print("hello", file=log)
from twitter import Twitter, OAuth
import pandas as pd
import sys
import os
import numpy as np


auth_token = '1254887108-QytWf6DU04kZy3Hb3Z5G21bRuZubqjzrzzikC1R'
auth_token_secret = 'HwyIbYpYsakQHlVk9vLxeeKVUD3GxyjBAiyxXFUVOywZD'
consumer_key = 'oIIzLH84ZUokXxhY6XhGK8ZQB'
consumer_secret = 'TLWXHS8yjBsZ0VJXGShB3qD2ELqUfSekMnFiZMjUGdYkOVmWKw'



t = Twitter(auth=OAuth(auth_token, auth_token_secret, consumer_key, consumer_secret))

sn = ['MariaTevesGonz', 'Rayp1971']
#log = open("C:\\Users\\teja\\Desktop\\aeight.txt", "w+")
fn = ['beight','bnine']
logf = "C:\\Users\\teja\\Desktop\\_.txt"
count = 0
for s in sn:
    fname = logf.replace("_",fn[count])
    count += 1
    log = open(fname,"w+")
    a_fol = t.followers.ids(screen_name=s)
    print(a_fol[u'ids'], file=log)