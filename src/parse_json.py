# import json
from searchtweets import ResultStream, gen_rule_payload, load_credentials

# with open('tweets.json', 'r') as outfile:
# 	outfile.read(tweets)


import json

with open('tweets.json', 'r') as json_data:
    tweets = json.load(json_data)
    print(type(tweets))
    # print(len(tweets['text']))
    
    tweets = tweets[0:100]

    with open('only_text.json', mode='w', encoding='utf-8') as f:
    	json.dump([], f)
    	tweet2 = []

    for tweet in tweets:
    	tweet["text"] = tweet["text"].translate ({ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\\'\n'|\\`~-=_+"})

    	# print(tweet['text'])
    	entry = {"text": tweet["text"]}

    	tweet2.append(entry)
    	

with open('only_text.json', mode='w', encoding='utf-8') as feedsjson:
	# entry = {"text": tweet["text"]}
	# tweet2.append(entry)
	json.dump(tweet2, feedsjson, indent=2)

	# print(tweet2)

	with open('tweets_test.json', 'w') as fp:

		json.dump(tweets, fp, indent=2)
	print(type(tweets))


