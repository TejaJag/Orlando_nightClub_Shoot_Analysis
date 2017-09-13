#Loading the screenNames.json file
fo = open("C:\\Users\\teja\\Documents\\1.MS\\1.Masters\\Beckage\\screenNames.json", "r")
screen_names = fo.readlines()
print screen_names

with open('C:\\Users\\teja\\Documents\\1.MS\\1.Masters\\Beckage\\screenNames.json') as f:
    words = [word.strip() for word in f]

print words
