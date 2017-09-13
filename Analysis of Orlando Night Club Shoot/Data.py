
from twitter import Twitter, OAuth
import pandas as pd
import sys
import os
import numpy as np

'''
auth_token = '1254887108-QytWf6DU04kZy3Hb3Z5G21bRuZubqjzrzzikC1R'
auth_token_secret = 'HwyIbYpYsakQHlVk9vLxeeKVUD3GxyjBAiyxXFUVOywZD'
consumer_key = 'oIIzLH84ZUokXxhY6XhGK8ZQB'
consumer_secret = 'TLWXHS8yjBsZ0VJXGShB3qD2ELqUfSekMnFiZMjUGdYkOVmWKw'


t = Twitter(auth=OAuth(auth_token, auth_token_secret, consumer_key, consumer_secret))
'''

data = pd.read_csv('C:\\Users\\teja\\Desktop\\800-AdvancedMachineLearning\\EECS800_LAB1\\finished_data.csv')

#print data.ix[1].ix[1]

content = data['content']
group_a = []
group_b = []
wd1 = "OrlandoStrong"
wd2 = "ISIS"
#print (data.ix[1]['json_output'])
#json_input = data.ix[1]['json_output']
cnt1 = 0
cnt2 = 0
for i in range(len(data)):
    if wd1 in data.ix[i]['content']:
        if cnt1 >= 100:
            True
        else:
            group_a.append(data.ix[i]['from_user_screen_name'])
            cnt1 += 1
    if wd2 in data.ix[i]['content']:
        if cnt2 >= 100:
            True
        else:
            group_b.append(data.ix[i]['from_user_screen_name'])
            cnt2 += 1

print(len(group_a))
print(len(group_b))
print group_a[50], " ,", group_a[2]
#print( group_b[99], ",", group_b[2])
'''
c = np.zeros((10, 10), dtype=np.int)
for i in range(10):
    user_a = group_a[i]
    for j in range(10):
        count = 0
        user_b = group_b[j]
        a_fol = t.followers.ids(screen_name=user_a)
        b_fol = t.followers.ids(screen_name=user_b)
        a_fol_ids = a_fol[u'ids']
        b_fol_ids = b_fol[u'ids']
        for iad in a_fol_ids:
            try:
                # if e.index(iad):
                if iad in b_fol_ids:
                    # c.append(iad)
                    count += 1
            except:
                True
        c[i][j] = count
print c
'''
#Commenting the code of mutual followers for the whole data
'''
for i in range(len(group_a)):
    user_a = group_a[i]
    for j in range(len(group_b)):
        count = 0
        user_b = group_b[j]
        a_fol = t.followers.ids(screen_name=user_a)
        b_fol = t.followers.ids(screen_name=user_b)
        a_fol_ids = a_fol[u'ids']
        b_fol_ids = b_fol[u'ids']
        for iad in a_fol_ids:
            try:
                # if e.index(iad):
                if iad in b_fol_ids:
                    # c.append(iad)
                    count += 1
            except:
                True
        c[i][j] = count
print c
'''







'''
json_acceptable_string = json_input.replace("'", "\"")
json_acceptable_string = json_acceptable_string.replace("#", "\#")


print json_acceptable_string
out_str = json.loads(json_acceptable_string)


for i in range(len(data)):
    if wd1 in data.ix[i]['content']:
        json_input = data.ix[i]['json_output']
        json_acceptable_string = json_input.replace("'", "\"")
        out_str = json.loads(json_acceptable_string)
        group_a.append(out_str['screen_name'])

print len(group_a)'''

