# import json
from searchtweets import ResultStream, gen_rule_payload, load_credentials

# with open('tweets.json', 'r') as outfile:
# 	outfile.read(tweets)


import json

with open('tweets.json') as json_data:
    tweets = json.load(json_data)
    # print(type(tweets))
    # print(d)
    # print(type(tweets['id']))
    # for tweet in tweets:
    # print(tweets['id'])

for tweet in tweets[0:100]:


	# for cow in tweet['retweeted_status']:
	# # 	for status in ['retweeted_status']['favorite_count']:
	# # 		status = int(status)
	# 		print(cow['lang'])
	# # 	print(str(cow['favorite_count']))


	# 	print(cow['source'])
		# print(cow['favorite_count'])
		# print(['retweeted_status'])
	# print(tweet['retweeted_status':{'favorite_count'}])
	# if 'retweeted_status' in tweet:
	if tweet.get('retweeted_status'):
		# print(tweet.get(['retweeted_status']['favorite_count']))

	# if 'retweeted_status' in tweet and 15 < tweet['retweeted_status']['favorite_count'] < 5000:
		print(tweet['text'] + tweet['created_at']+ "favorite_count: " + str(tweet['retweeted_status']['favorite_count']) + "\n")

	# print(tweet['retweeted_status']['favorite_count']) - works

	# print(tweet['user']['location']) - works

	# print(tweet['id']) - works 	



#is a list going in.  