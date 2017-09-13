from __future__ import print_function
import pandas as pd

data = pd.read_csv('C:\\Users\\teja\\Desktop\\800-AdvancedMachineLearning\\EECS800_LAB1\\finished_data.csv')

content = data['content']
group_a = []
group_b = []
wd1 = "OrlandoStrong"
wd2 = "ISIS"

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

Sname_file1 = open("C:\\Users\\teja\\Desktop\\800-AdvancedMachineLearning\\Twitter\\groupA.txt","w+")
Sname_file2 = open("C:\\Users\\teja\\Desktop\\800-AdvancedMachineLearning\\Twitter\\groupB.txt","w+")

print(group_a, file = Sname_file1 )
print (group_b,file = Sname_file2)
