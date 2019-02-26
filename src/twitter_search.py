from searchtweets import ResultStream, gen_rule_payload, load_credentials
import json
import requests

premium_search_args = load_credentials("~/.twitter_keys.yaml",
                                       yaml_key="search_tweets_premium",
                                       env_overwrite=False)


rule = gen_rule_payload("Superbowl Tom Brady",
						from_date="2019-02-02T23:59", #UTC - converted for superbowl date and game time
                        to_date="2019-02-03T03:00")
print(rule)

from searchtweets import collect_results

# tweets = collect_results(rule, 
#                          max_results=100, 
#                          result_stream_args=premium_search_args)
                         


rs = ResultStream(rule_payload=rule,
                  max_results=100,
                  max_pages=1,
                  **premium_search_args)

print(rs)
tweets = list(rs.stream())
print(type(tweets))
[print(tweet.all_text + str(tweet.created_at_datetime)) for tweet in tweets[0:10]];


# [print(tweet.all_text, end='\n\n') for tweet in tweets[0:10]];




with open('tweets.json', 'w') as outfile:
    json.dump(tweets, outfile, indent=2)
