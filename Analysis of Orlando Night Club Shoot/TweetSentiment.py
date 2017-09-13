from __future__ import print_function
import sys
import json
import ast
from pprint import pprint


def hw():
    print ('Hello, world!')


def lines(fp):
    print (str(len(fp.readlines())))


def pri(y):
    print(y)


def main():
    #sent_file = open(sys.argv[1])
    #tweet_file = open(sys.argv[2])
    # hw()
    # lines(sent_file)
    # lines(tweet_file)
    # data=[]
    sname = open("C:\\Users\\teja\\Desktop\\800-AdvancedMachineLearning\\Twitter\\screenname1000.csv", "w+")
    tweets = open("C:\\Users\\teja\\Desktop\\800-AdvancedMachineLearning\\Twitter\\tweets1000.csv", "w+")
    sentiment = open("C:\\Users\\teja\\Desktop\\800-AdvancedMachineLearning\\Twitter\\sentiments1000.csv", "w+")
    word_file = open(sys.argv[1])
    scores = {}  # initialize an empty dictionary
    for line in word_file:
        term, score = line.split("\t")
        scores[term] = int(score)

        # print scores.items()

    new = open(sys.argv[2])
    for line in new:
        in1 = line.index("u'screen_name'")
        in2 = line.index("u'", in1+17)
        print(in1, in2)
        name = line[in1+17:in2-2]
        print ("name:", name)
        print (name, file=sname)
        line = line.replace("#", " ")

        # Extracting the tweet content from the json output string
        ind1 = line.index("u'text'")
        ind2 = line.index("u'is_quote_status'")
        twt = line[ind1+10:ind2-2]
        print (twt, file=tweets)

        print ("data:",twt)
        summ = 0
        l2 = twt.encode('ascii', 'ignore')
        print(l2)
        ter = l2.split(" ")
        # print(ter)
        for a in ter:
        # print a
            if a in scores:
                    summ = summ + scores.get(a)
        print (summ, file=sentiment)



            # l3="hi i am ujjwal"
            # print (l3)
            # word=l3.split(" ")
            # print word


if __name__ == '__main__':
    main()