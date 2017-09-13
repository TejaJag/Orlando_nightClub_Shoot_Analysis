#import xlsxwriter

#workbook = xlsxwriter.Workbook('mutual_hashtags.xlsx')
#worksheet = workbook.add_worksheet()
hashtags = [] # stores list of all users' hash tags
usertags = [] # used for storing single user hash tags
with open('C:\\Users\\teja\\Documents\\1.MS\\1.Masters\\RA\\hasgtagsTestFile.csv') as f:
    usertags = [word.strip() for word in f]
usertags[1].strip("\'")
print usertags[1]
usertags[1] = usertags[1].split(",")

usertags[1][0] = usertags[1][0].replace("\"","")
print usertags[1][0]


