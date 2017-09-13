import numpy as np

'''
with open("C:\\Users\\teja\\Desktop\\azero.txt","r") as my_file:
    a_ids = my_file.read()

print a_ids
a_ids = a_ids.replace("[","")
a_ids = a_ids.replace("]","")
a_ids_ls=a_ids.replace("\n","")
a_ids_ls = a_ids.split(',')
a_ids_ls = map(long,a_ids_ls)
print a_ids_ls
'''

stri = "C:\\Users\\teja\\Desktop\\_.txt"
fn1 = ['azero','aone', 'atwo', 'athree', 'afour', 'afive', 'asix', 'aseven', 'aeight']
fn2 = ['bzero','bone', 'btwo', 'bthree', 'bfour', 'bfive', 'bsix', 'bseven', 'beight', 'bnine']
c = np.zeros((len(fn1), len(fn2)), dtype=np.int)
for i in range(len(fn1)):
    f1 = stri.replace("_", fn1[i])
    with open(f1, "r") as my_file:
        a_ids = my_file.read()

    a_ids = a_ids.replace("[", "")
    a_ids = a_ids.replace("]", "")
    a_ids_ls = a_ids.replace("\n", "")
    a_ids_ls = a_ids.split(',')
    a_ids_ls = map(long, a_ids_ls)
    for j in range(len(fn2)):
        count = 0
        f2 = stri.replace("_",fn2[j])
        with open(f2, "r") as my_file:
            b_ids = my_file.read()

        b_ids = b_ids.replace("[", "")
        b_ids = b_ids.replace("]", "")
        b_ids_ls = b_ids.replace("\n", "")
        b_ids_ls = b_ids.split(',')
        b_ids_ls = map(long, b_ids_ls)

        for iad in a_ids_ls:
            try:
                if iad in b_ids_ls:
                    count +=1
            except:
                True
        c[i][j]= count

print c