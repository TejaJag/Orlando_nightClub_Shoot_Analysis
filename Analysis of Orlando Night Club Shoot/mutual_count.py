import numpy as np

i,j,lines = 0,0,0
c=[]
flag,flag2 = 0,0
with open("C:\\Users\\teja\\Desktop\\800-AdvancedMachineLearning\\Twitter\\groupABIDs.txt","r") as f1:

        for line1 in f1:
            #print("flag:",flag)
            flag += 1
            lines += 1
            Aids = line1
            Aids = Aids.replace("[","")
            Aids = Aids.replace("]","")
            Aids_list = Aids.split(',')
            Aids_list = map(long, Aids_list)
            with open("C:\\Users\\teja\\Desktop\\800-AdvancedMachineLearning\\Twitter\\groupABIDs.txt", "r") as f2:
                for line2 in f2:
                    #print("flag2:",flag2)
                    flag2 += 1
                    Bids = line2
                    Bids = Bids.replace("[","")
                    Bids = Bids.replace("]","")
                    Bids_list = Bids.split(',')
                    Bids_list = map(long, Bids_list)
                    count = 0
                    for iad in Aids_list:
                        try:
                            if iad in Bids_list:
                                count += 1
                        except:
                            True
                    c.append(count)
print("no of lines",lines)
print(len(c))
#print(c)
arr = np.array(c)
arr.shape = (155,155)

print (arr.shape)

for i in range(155):
    arr[i][i] = 0

print(arr)
print ("mean is(group A B) :", np.mean(arr))

'''
with open("C:\\Users\\teja\\Desktop\\800-AdvancedMachineLearning\\Twitter\\groupAIDs.txt","r") as f1:
    with open("C:\\Users\\teja\\Desktop\\800-AdvancedMachineLearning\\Twitter\\groupAIDs.txt","r") as f2:
        for line1 in f1:
            Aids = line1
            Aids = Aids.replace("[","")
            Aids = Aids.replace("]","")
            Aids_list = Aids.split(',')
            Aids_list = map(long, Aids_list)
            for line2 in f2:
                Bids = line2
                Bids = Bids.replace("[","")
                Bids = Bids.replace("]","")
                Bids_list = Bids.split(',')
                Bids_list = map(long, Bids_list)
                for iad in Aids_list:
                    try:
                        if iad in Bids_list:
                            count += 1
                    except:
                        True
                c
'''