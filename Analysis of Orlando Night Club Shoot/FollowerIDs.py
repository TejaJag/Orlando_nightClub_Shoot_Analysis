from __future__ import print_function
from twitter import Twitter, OAuth, api
import pandas as pd
import sys
import os
import numpy as np


auth_token = '111684414-W66KP2eO6kIsGYmYNBFPddjUhgb0wnjCoYfKPwHo'
auth_token_secret = 'LOaBwSQIdZ53pK3RwZpfNFkkImfaZ1GVLRmmSVUT2byuW'
consumer_key = 'hsOAp2VPDYT7whSBRGQNpemuz'
consumer_secret = 'G1BEc7sqeSiQuVdfldKMZP25cIanO9zxaWRr7lbBllbZzhJ8LG'


t = Twitter(auth=OAuth(auth_token, auth_token_secret, consumer_key, consumer_secret))


with open("C:\\Users\\teja\\Desktop\\800-AdvancedMachineLearning\\Twitter\\groupB.txt","r") as myFile:
    screen_names_string = myFile.read()
    screen_names_string = screen_names_string.replace("[","")
    screen_names_string = screen_names_string.replace("]","")
    screen_names_string = screen_names_string.replace("\n","")
    screen_names_string = screen_names_string.replace("'","")
    screen_names = screen_names_string.split(',')

    Aid_file = open("C:\\Users\\teja\\Desktop\\800-AdvancedMachineLearning\\Twitter\\groupBIDs.txt","a")
    for i in range(79,len(screen_names)):
        try:
            fol = t.followers.ids(screen_name=screen_names[i])
            fol_id = fol[u'ids']
            print (fol_id,file= Aid_file)
            print ("i valueb ",i)
        except api.TwitterHTTPError as ex:
            print("i value is",i)
            print (ex.message)
            break


