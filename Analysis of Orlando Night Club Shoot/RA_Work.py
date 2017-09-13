from __future__ import  print_function
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import pandas as pd
import sys

ps = PorterStemmer()
sentiment = open("C:\\Users\\teja\\Documents\\1.MS\\1.Masters\\Semester-2\\800-AdvancedMachineLearning\\Twitter\\sentiments1000_byProf.csv", "w+")
ip_file = pd.read_csv('C:\\Users\\teja\\Documents\\1.MS\\1.Masters\\Semester-2\\800-AdvancedMachineLearning\\Twitter\\1000TweetsOrlandoStrong.csv')
names = ip_file['from_user_screen_name']
content = ip_file['content']
word_file = open(sys.argv[1])
scores = {}  # initialize an empty dictionary
for line in word_file:
    term, score = line.split("\t")
    scores[term] = int(score)
for i in range(len(content)):
    twt = content.ix[i]
    #print(twt)
    twt = twt.decode('ascii', 'ignore')
    twt = twt.encode('ascii', 'ignore')

    ter = twt.split(" ")
    summ = 0
    for a in ter:
        # print a
        #include the below commented line inorder to stem the words
        #a  = ps.stem(a)
        if a in scores:
            summ = summ + scores.get(a)
    print (summ, file = sentiment)

'''
words = ["eating","crawling","crying","hit","hello","eater"]
for w in words:
    print (ps.stem(w))
'''