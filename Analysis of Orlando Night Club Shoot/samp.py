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


data = pd.read_csv('C:\\Users\\teja\\Desktop\\800-AdvancedMachineLearning\\EECS800_LAB1\\finished_data.csv')

#print data.ix[1].ix[1]
log = open("C:\\Users\\teja\\Desktop\\py.txt", "w+")
content = data['content']
group_a = []
group_b = []
wd1 = "hate"
wd2 = "terrorist"
#print (data.ix[1]['json_output'])
#json_input = data.ix[1]['json_output']
cnt1 = 0
cnt2 = 0
for i in range(len(data)):
    if wd1 in data.ix[i]['content']:
        if cnt1 == 10:
            True
        else:
            group_a.append(data.ix[i]['from_user_screen_name'])
            cnt1 += 1
    if wd2 in data.ix[i]['content']:
        if cnt2 == 10:
            True
        else:
            group_b.append(data.ix[i]['from_user_screen_name'])
            cnt2 += 1
user_a = group_a[1]
a_fol = t.followers.ids(screen_name=user_a)
print(group_a, file=log)
print(group_b, file=log)
print(a_fol[u'ids'], file=log)