from twitter import Twitter, OAuth
import sys
import os

auth_token = '111684414-W66KP2eO6kIsGYmYNBFPddjUhgb0wnjCoYfKPwHo'
auth_token_secret = 'LOaBwSQIdZ53pK3RwZpfNFkkImfaZ1GVLRmmSVUT2byuW'
consumer_key = 'hsOAp2VPDYT7whSBRGQNpemuz'
consumer_secret = 'G1BEc7sqeSiQuVdfldKMZP25cIanO9zxaWRr7lbBllbZzhJ8LG'


'''
auth_token = '1254887108-QytWf6DU04kZy3Hb3Z5G21bRuZubqjzrzzikC1R'
auth_token_secret = 'HwyIbYpYsakQHlVk9vLxeeKVUD3GxyjBAiyxXFUVOywZD'
consumer_key = 'oIIzLH84ZUokXxhY6XhGK8ZQB'
consumer_secret = 'TLWXHS8yjBsZ0VJXGShB3qD2ELqUfSekMnFiZMjUGdYkOVmWKw'
'''



if len(sys.argv) != 3:
    print 'Usage:\n\n' + os.path.basename(sys.argv[0]) + ' screenname1 screenname2';

user_a = sys.argv[1]
user_b = sys.argv[2]
t = Twitter(auth=OAuth(auth_token, auth_token_secret, consumer_key, consumer_secret))
a = t.followers.ids(screen_name=user_a)
b = t.followers.ids(screen_name=user_b)
print a
print b
'''
user_a = sys.argv[1]
user_b = sys.argv[2]

a = t.followers.ids(screen_name=user_a)
b = t.followers.ids(screen_name=user_b)
c = []
d = a[u'ids']
e = b[u'ids']
print "hell",a[u'ids']
print "heaven",e
for iad in d:
    try:
        #if e.index(iad):
        if iad in e:
            print iad
            c.append(iad)
    except:
        True
print "cccc",c
print '\n' + user_a, 'has', len(d), 'follower'
print user_b, 'has', len(e), 'follower'
print user_a, 'and', user_b, 'have', len(c), 'followers in common'

if len(c) > 100:
    c = c[:100]
    print '\nfirst 100 common followers are:'
elif len(c) > 0:
    print '\nthese are the common followers:'
info1 = t.users.lookup(user_id=','.join(map(str, d)))
info2 = t.users.lookup(user_id=','.join(map(str, e)))
inf1 = []
for u in info1:
    inf1.append(u['screen_name'])
print ', '.join(inf1)
inf2 = []
for p in info2:
    inf2.append(p['screen_name'])
print ', '.join(inf2)

if len(c) > 0:
    common_info = t.users.lookup(user_id=','.join(map(str, c)))
    common = []
    for u in common_info:
        common.append(u['screen_name'])

    print ', '.join(common)

print
'''