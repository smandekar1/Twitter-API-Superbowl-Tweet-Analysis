# import json
from searchtweets import ResultStream, gen_rule_payload, load_credentials

# with open('tweets.json', 'r') as outfile:
# 	outfile.read(tweets)


import json

with open('tweets.json', 'r') as json_data:
    tweets = json.load(json_data)
    # print(type(tweets))
    # print(d)
    # print(type(tweets['id']))
    # for tweet in tweets:
    # print(tweets['id'])

tweets = tweets[0:2]

	

	# = tweet['text'].read().replace(' ', '')
	
	# print(tweet)

	if tweet.get('retweeted_status'):
	
		
		for tweet in tweets:

			tweet["text"] = tweet["text"].translate ({ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\\'\n'|\\`~-=_+"})

			tweet = tweet["text"]
    # for change in json_data["Changes"]:
    #     # strip the contents of trailing white spaces (new line)
    #     change["Name"] = change["Name"].strip()

	with open("out.json", "w") as fout:
		fout.write(json.dumps(tweets, indent=2))	












		# tweet = tweet['text']
		# tweet1 = 'asdf;lkajfafds'
		# tweet2 = tweet1.replace('a','zzzz')		
		# print(tweet2)
		# for char in tweet1:
		# 	print(char)
		# 	if char is 'a':
				
		# 		char = 'zzzz'
		# 		print(char)
		
		# with open("out.json", "w") as fout:
  #   		fout.write(json.dumps(json_data))

		# print(tweet1)
		# print(tweet)
		# for char in 	# print(char)
		# 	if char is 'a':
		# 		char.replace('a', 'z')
		# 	print(char)
		
		# print(tweet.get(['retweeted_status']['favorite_count']))

	# if 'retweeted_status' in tweet and 15 < tweet['retweeted_status']['favorite_count'] < 5000:
		# print(tweet['text'] + tweet['created_at']+ "favorite_count: " + str(tweet['retweeted_status']['favorite_count']) + "\n")

	# print(tweet['retweeted_status']['favorite_count']) - works

	# print(tweet['user']['location']) - works

	# print(tweet['id']) - works 	



