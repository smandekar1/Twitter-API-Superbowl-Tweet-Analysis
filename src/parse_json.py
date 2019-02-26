# import json
from searchtweets import ResultStream, gen_rule_payload, load_credentials
from collections import Counter
from stop_words import get_stop_words


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
	
	json.dump(tweet2, feedsjson, indent=2)

	# print(tweet2)

	with open('tweets_test.json', 'w') as fp:

		json.dump(tweets, fp, indent=2)
	print(type(tweets))


with open('only_text.json', mode='r', encoding='utf-8') as words_file:

	d = []

	for tweet in tweets:
		entry = tweet["text"].split()
		entry_lower = [x.lower() for x in entry]
		d += entry_lower	
		# d.append(entry)

	# with open('stopwords.txt') as fp:
	# 	stopwords = set(fp.readlines())
	# 	stopwords = stopwords.strip()
	# # stopwords = open('stopwords.txt').readlines()	
	# # stopwords = set(line.strip() for line in open('stopwords.txt'))
	stop_words = get_stop_words('english')
	added_words = ['rt', 't','https', 'people', 'co', 'people', 'la', 'el']
	stop_words = added_words + stop_words
	print("stopwords \n------------------------------------------------------------------------------", stop_words)
	
	# stopwords = nltk.download('stopwords')
	# # stopwords = stopwords.words('english')
	# print(stopwords.words('english')[620:680])
	# for word in d:
	# 	if word.lower() in stopwords:
	# 		del word
	e = []
	for word in d:
		if word not in stop_words:
			e.append(word)
	

	print(type(d))
	print(type(stop_words))
	# print(d)

	counted = Counter(e).most_common(1000)
	# counted = [x.decode('utf-8','ignore').encode("utf-8") for x in counted]
	
	# counted=counted.decode('utf-8','ignore').encode("utf-8")
	# [x.encode('utf-8') for x in tmp]
	print("--------------\n", counted)
	print(type(counted))

	with open("football.txt", "w", encoding="utf-8") as ofile:
		for k,v in counted:
				if k.isalnum():
					ofile.write(" " + k)
	
	# with open("football.txt", "w") as ofile:

	# 	for x in counted:
	# 		if (x[0] is String):
	# 		  	ofile.write(" " + k)



					# 		if k.decode('utf-8'):