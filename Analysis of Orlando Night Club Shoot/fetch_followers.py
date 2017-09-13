import twitter, time, json
import numpy


# Load config from JSON
with open('config.json') as data_file:
    json = json.load(data_file)

# Connect to Twitter API
api = twitter.Api(consumer_key=json['twitter']['consumer_key'],
                      consumer_secret=json['twitter']['consumer_secret'],
                      access_token_key=json['twitter']['access_token_key'],
                      access_token_secret=json['twitter']['access_token_secret'])
# Print payload to verify Twitter access is working
print api.VerifyCredentials()

# Write list of followers to a followers.txt file
def writeFollowersToFile(followers, username):
    # Write name of selected user
    with open("followers.txt", "a") as myfile:
        myfile.write('Followers for {0}:\n\n'.format(username))
    # Write list of followers
    for friend in followers:
        with open("followers.txt", "a") as myfile:
            myfile.write('{0}\n'.format(friend))
    print 'Done writing to file.'

with open('C:\\Users\\teja\\Documents\\1.MS\\1.Masters\\RA\\screenNamesTestFile.json') as f:
    words = [word.strip() for word in f]
# Get all followers from users in array
friends = []
users = []
for name in words:
    sec = api.GetSleepTime('/followers/list') + 2 # Wait 2 seconds more to make sure rate-limit is avoided
    print 'Will wait {0} sec to avoid rate-limit'.format(sec)
    time.sleep(sec)
    print 'Fetching followers for {0}...'.format(name)
    # Uncomment the next line to instead fetch from the /followers/list API (takes much longer)
    #friends = api.GetFollowers(screen_name=name, skip_status=True, count=200, include_user_entities=False)
    try:
        friends = api.GetFollowerIDs(screen_name=name)
        users.append(friends)
        #------------------------commented by me the below 2 lines----------------------
        #print 'Writing the {0} followers of {1} to file...'.format(len(friends), name)
        #writeFollowersToFile(friends, name)
    except:
        print 'Writing the {0} followers of {1} to file...'.format(len(friends), name)
        # ------------------------commented by me the below 2 lines----------------------
        #with open("followers.txt", "a") as myfile:
         #   myfile.write('Followers for {0} doesn\'t exist(A/C doesnt exist\n\n'.format(name))

print users[0][1]
print '----'
print users[1]
print len(users)