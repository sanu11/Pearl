# needs python3 only!
# there is pickle protocol pblm python3 uses 3 out of 0,1,2,3,4 by default which is incompatible with python2.
# other solution is to read files from python3 and load it using 0 as the protocol and then uses python to load them.
from emotion_predictor import EmotionPredictor
import csv

s='output_final.csv'
tweets = ['art',"social","intelligence","game","planet","career","mistake","ready","like","good","plan","deal","me","loyal","know","child"]
# i=0
# with open(s) as rf:
# 	reader=csv.reader(rf,delimiter=',')
# 	for row in reader:
# 		tweet=row[2]
# 		tweets.append(tweet)
# 		i=i+1

# noOfTweets = i
# for i in range(0,30):
# 	print (tweets[i])

# print (noOfTweets)
model = EmotionPredictor(classification='plutchik', setting='mc')

# tweets = [
#     "Watching the sopranos again from start to finish!",
#     "Finding out i have to go to the  dentist tomorrow",
#     "I want to go outside and chalk but I have no chalk",
#     "Stock market hit all time low on friday",
#     "Stock market hit all time high on friday",  
#     "I believe you",
#     "My mom wasn't mad",
#     "Do people have no Respect for themselves or you know others peoples homes",
#     "www.google.com I am happy",
# ]

result = model.predict_classes(tweets)
probabilities=model.predict_probabilities(tweets)
print (result)
print (probabilities)
print (probabilities.to_dict[0])

anger = probabilities["Anger"].values.tolist()
joy   = probabilities["Joy"].values.tolist()
fear  = probabilities["Fear"].values.tolist()
surprise = probabilities["Surprise"].values.tolist()
disgust = probabilities["Disgust"].values.tolist()
trust = probabilities["Trust"].values.tolist()
anticipation = probabilities["Anticipation"].values.tolist()
sadness = probabilities["Sadness"].values.tolist()

text = result["Tweet"].values.tolist()
emotion = result["Emotion"].values.tolist()


# print (text,emotion)
# print (result[i], type(result[i]))
# i=1
# n = len(text)
# file="classify.csv"
# with open(file,"w") as rf:
# 	fieldnames=['Id','Tweet','Emotion','Anger','Joy','Surprise','Fear','Disgust','Sadness','Trust','Anticipation']
# 	writer= csv.DictWriter(rf,fieldnames=fieldnames)
# 	for i in range(0,n):
# 		writer.writerow({'Id':i,'Tweet':text[i],'Emotion':emotion[i],'Anger':anger[i],'Joy':joy[i],'Surprise':surprise[i],'Disgust':disgust[i],'Anticipation':anticipation[i],'Trust':trust[i],'Sadness':sadness[i],'Fear':fear[i]})
# 		