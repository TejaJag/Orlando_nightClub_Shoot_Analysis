import tweepy
consumer_key = "S9a39MpOJyJ5P09cGrZq0ntvf"
consumer_secret = "kZRISCgWLS1NhIJBJ86LQOstB8H8KQofwnEhCYf8s3wUNe7Qht"
access_token  = "1254887108-QytWf6DU04kZy3Hb3Z5G21bRuZubqjzrzzikC1R"
access_token_secret = "HwyIbYpYsakQHlVk9vLxeeKVUD3GxyjBAiyxXFUVOywZD"
'''auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)'''
auth1 = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth1.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth1, wait_on_rate_limit="true", wait_on_rate_limit_notify="true")
ids = ["971206170", "128918733"]
user = api.get_user(971206170)
print("------------------------------")
print(user)
def get_usernames(ids):
    """ can only do lookup in steps of 100;
        so 'ids' should be a list of 100 ids
    """
    user_objs = api.lookup_users(user_ids=ids)
    for user in user_objs:
        print(user.screen_name)

#get_usernames(ids)
