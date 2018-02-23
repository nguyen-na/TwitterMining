from __future__ import print_function
from twitter import Status
import twitter
import re

CONSUMER_KEY = 'XXXXX'
# CONSUMER_KEY = os.getenv("CONSUMER_KEY", None)
CONSUMER_SECRET = 'XXXXX'
# CONSUMER_SECRET = os.getenv("CONSUMER_SECRET", None)
ACCESS_TOKEN = 'XXXXX'
# ACCESS_TOKEN = os.getenv("ACCESS_TOKEN", None)
ACCESS_TOKEN_SECRET = 'XXXX'
# ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET", None)


# Create an Api instance.
api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN,
                  access_token_secret=ACCESS_TOKEN_SECRET)

SEARCH_TERMS = str(input('What would you like to search?'))

tweets = api.GetSearch(term = SEARCH_TERMS, count = 100, result_type = 'recent', lang = 'en')
tweets = [_.text for _ in tweets]

wordList = [re.sub("[^\w]", " ",  s).split() for s in tweets]

combinedWordList = [val for sublist in wordList for val in sublist]
combinedWordList = [_.lower() for _ in combinedWordList]

index = 0
usedWords = [re.sub("[^\w]", " ",  SEARCH_TERMS).split(), 'a', 'I', 'rt', 'show', 'and', 'not', 'any', 'if', 'you', 'is', 'the', 'what', 'this', 'also']

countPerWord = []
for word in combinedWordList:
    count = 1
    if (any(word in _ for _ in usedWords)):
        index +=1
    else:
            for i in range(index,len(combinedWordList)):
                if word == combinedWordList[i]:
                    count+=1
            # print(word + ' ' + str(count))
            usedWords.append(word)
            countPerWord.append(count)
            index +=1

usedWords = usedWords[14:(len(usedWords)-1)]

CountsandWords = dict(zip(usedWords,countPerWord))

for key, value in sorted(CountsandWords.items(), key=lambda t: t[1], reverse=True):
    print("%s %s" %(key, value))
