import csv,io
import operator
from emotion_predictor import EmotionPredictor
from tempfile import NamedTemporaryFile
import shutil
model = EmotionPredictor(classification='plutchik', setting='mc')
file='PlutchikClassify.csv'
# had to add mode = 'w' else error
tempfile = NamedTemporaryFile(delete=False,mode='wt')

with open(file, "r+") as rf,tempfile:
	reader = csv.reader(rf, delimiter=',')
	writer = csv.writer(tempfile, delimiter=',')
	for tweetRow in reader:
		# emotions
		# print (tweetRow)
		if(tweetRow[0]=="id"):
			continue
		words=[]
		emotions={}
		if(tweetRow[17]=="-"):	
			word = tweetRow[13]
			words.append(word)
			# print (words)
			result = model.predict_classes(words)
			probabilities=model.predict_probabilities(words)

			anger = probabilities["Anger"].values.tolist()
			joy   = probabilities["Joy"].values.tolist()
			fear  = probabilities["Fear"].values.tolist()
			surprise = probabilities["Surprise"].values.tolist()
			disgust = probabilities["Disgust"].values.tolist()
			trust = probabilities["Trust"].values.tolist()
			anticipation = probabilities["Anticipation"].values.tolist()
			sadness = probabilities["Sadness"].values.tolist()
			
			emotions["Anger"]=anger[0]
			emotions["joy"]=joy[0]
			emotions["fear"]=fear[0]
			emotions["surprise"]=surprise[0]
			emotions["disgust"]=disgust[0]
			emotions["trust"]=trust[0]
			emotions["anticipation"]=anticipation[0]
			emotions["sadness"]=sadness[0]
			# print (emotions)
			sorted_emotions = sorted(emotions.items(), key=operator.itemgetter(1),reverse=True)
			total=0
			majorEmotions=[]
			for i in range(0,9):
				total+=sorted_emotions[i][1]
				majorEmotions.append(sorted_emotions[i])
				if(total>=0.6):
					break
				elif(i==3):
					break;
			# print(word)
			# print(majorEmotions)

			# add emtions to string
			emotions=""
			for emotion in majorEmotions:
				emotions+=emotion[0]+"-"

			tweetRow.append(emotions)
			# tempfile.write(tweetRow)
		else:
			tweetRow.append(tweetRow[17])
		
		tweetStr = ('"%s"') % '", "'.join(tweetRow)
		# print (tweetStr)
		# byte like object is required
		writer.writerow(tweetRow)
shutil.move(tempfile.name, file)




