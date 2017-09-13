from __future__ import print_function
import pandas as pd

data = pd.read_csv('C:\\Users\\teja\\Desktop\\800-AdvancedMachineLearning\\EECS800_LAB1\\finished_data.csv')
content = data['content']

wd1 = "ISIS"
wd2 = "ISIS"

Tweets_file1 = open("C:\\Users\\teja\\Desktop\\800-AdvancedMachineLearning\\Twitter\\tweets1000.json","w+")

count = 0
'''
for i in range(len(data)):
    if (wd1 or wd2 in data.ix[i]['content']) and data.ix[i]['retweeted_status'] != "THIS IS A RETWEET --> DOUBLE-CHECK JSON":
        count += 1
        if count <= 100:
            print(data.ix[i]['json_output'], file=Tweets_file1)
        else:
            break
'''
for i in range(len(data)):
    if data.ix[i]['retweeted_status'] != "THIS IS A RETWEET --> DOUBLE-CHECK JSON":
        count += 1
        if count <= 1000:
            print(data.ix[i]['json_output'], file=Tweets_file1)
        else:
            break







