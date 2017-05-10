from pycorenlp import StanfordCoreNLP
nlp = StanfordCoreNLP('http://localhost:9000')

tweets = [
"haha lol owned dad!!!! u may think its nice that u get a fathers day once a year, but there is a son day every week",
"I don't know, dude. Probably science & shit. Worst answer I ever gave in a job interview. :(",
"Saw a coworker washing a banana in the sink and wondering what she did with it.",
"It's so cold this morning I had to separate my dogs poop into two separate bags and use them as hand warmers.",
"Every time I tie my shoe I feel like I'm giving a faraway sniper the go signal.",
"While they're a lot of fun on Halloween, did you know most jack-o-lanterns end up at the pound? Please. Next year, carve a puppy."
]

def processTweet(tweet):
    input = tweet
    input = ''.join(c for c in input if c not in '!.?')
    input = input.lower()
    res = nlp.annotate(input,
                       properties={
                           'annotators': 'sentiment',
                           'outputFormat': 'json',
                           'timeout': 1000,
                       })
    totalSentiment = 0
    for s in res["sentences"]:
        totalSentiment+=int(s["sentimentValue"])
        print"%d: '%s': %s %s" % (
            s["index"],
            " ".join([t["word"] for t in s["tokens"]]),
            s["sentimentValue"], s["sentiment"])
    print "TotalSent:%d" % totalSentiment
    return totalSentiment

def getRatio(a):
    sumPos = 0.0
    sumNeg = 0.0
    for sentiment in a:
        sumNeg+=(sentiment==0 or sentiment==1)
        sumPos+=(sentiment==3 or sentiment==4)
    return sumPos/sumNeg

sentimentArr = []
for t in tweets:
    sentimentArr.append(processTweet(t))
print "Sentiment ratio for %d tweets: %f" % (len(tweets), getRatio(sentimentArr))

