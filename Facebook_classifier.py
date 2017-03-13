import facebook
import json
import itertools
import re
import requests
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
 
token ='EAACEdEose0cBALaNuqiIQkP6Nf1V4peay5sKkBUTYmVEmrvMGMwDrKhzXJQYl9wx46udE1BHuzi6mQiR54vO1ugAzrRGglPat2mPgHz0AHcGTF9rVyEoZAmwzXyJj5DcCbClhoj7ugm0wK7D9ADK6VND6z32hsjFxrKmcjwZDZD'

graph = facebook.GraphAPI(token)
profile = graph.get_object("me")
#friends = graph.get_connections("message", "feed")



print("#######################################################################################################################")
print(' ')
print('				WELCOME TO FACEBOOK CLASSIFIER, CLASSIFY YOUR COMMENTS AND STATUS')
print(' ')
print("				Building the classifier...")
print(' ')

print("please wait......")
print("please wait......")
print("please wait......")
 
def word_feats(words):
    return dict([(word, True) for word in words])
 
negids = movie_reviews.fileids('neg')
posids = movie_reviews.fileids('pos')
 
negfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'neg') for f in negids]
posfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'pos') for f in posids]
 
negcutoff = len(negfeats)
poscutoff = len(posfeats)
ng = "negative samples: "
ps = "positive samples: "
print("%s %d" % (ng, negcutoff))
print("%s %d" % (ps, poscutoff))
#print("positive: "+poscutoff)
 
trainfeats = negfeats[:850] + posfeats[:850]
testfeats = negfeats[850:] + posfeats[850:]
print('train on %d instances, test on %d instances' % (len(trainfeats), len(testfeats)))
print("Using NaiveBayesClassifier and Training it.")
print("please wait......")
classifier = NaiveBayesClassifier.train(trainfeats)
print("Checking the accuracy .... ")
print('accuracy:', nltk.classify.util.accuracy(classifier, testfeats))
print(classifier.show_most_informative_features())
#print("Printing the result for prediction for your given phrase.")
print(' ')
#string  = "Sun is blessing in this cool weather."
#prediction = classifier.classify(word_feats(string))
#print("Your given input is: %s and Prediction is" %string)
#print("Prediction is: %s" %prediction)
print(' ')
print("#######################################################################################################################")
print(' ')


print("				Getting your Facebook 'status updates'")
print("				please wait ....")
print("\n \n  ")
S = "STATUS"
P1 = "PREDICTION"
print("%50s : %4s " %(S,P1))
print("\n \n  ")
feed = graph.get_connections(profile['id'], 'feed')
#print(posts)

Jstr2 = json.dumps(feed)
JDict2 = json.loads(Jstr2)
countFeed = 0
for i in JDict2['data']:
    try:
        allPosts = i['message']
        countFeed += 1
        print("%55s : %4s" %(allPosts, (classifier.classify(word_feats(allPosts)))))
       # print("Prediction is: %s"%(classifier.classify(word_feats(allPosts))))


        #for a in allPosts:  
            
          #  print(a)
    except (KeyError):
        continue       
            

    except (UnicodeEncodeError):
        pass
print("\n \n  ")
print("Total Number of Status Classified: %d" %(countFeed))
print("#######################################################################################################################")
print(' ')
print('				Getting your Facebook Comments')
print("				please wait ....")
print("\n \n  ")
C = "COMMENTS"
P = "PREDICTION"
print("%55s : %4s" %(C,P))
print("\n \n  ")

posts = graph.get_connections(profile['id'], 'posts')

Jstr = json.dumps(posts)
JDict = json.loads(Jstr)

count = 0
for i in JDict['data']:
    #allID = i['id']
    try:
        allComments = i['comments']

        for a in allComments['data']:  
            count += 1
            print("%50s : %4s"%(a['message'],(classifier.classify(word_feats(a['message']))))) 


    except (UnicodeEncodeError):
        pass

    except (KeyError):
        continue       

print("\n \n  ")
print("Total Number of Comments classified: %d" %(count))

print("#######################################################################################################################")
print(' ')
print(" 						The End!! Hope so you are satisfied!! 										")


