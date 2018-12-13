import csv 
import pandas

#outputFile = open("PlutchikClassifyOLD.csv","wb")
file1 = open("VADscores_6.txt","w")
file1.write("Id,Username,Date,Tweet,Emotion,Anger,Joy,Surprise,Fear,Disgust,Sadness,Trust,Anticipation,SadnessV,SadnessA,SadnessD,SadnessCount,AnticipationV,AnticipationA,AnticipationD,AnticipationCount,DisgustV,DisgustA,DisgustD,DisgustCount,SurpriseV,SurpriseA,SurpriseD,SupriseCount,AngerV,AngerA,AngerD,AngerCount,JoyV,JoyA,JoyD,JoyCount,FearV,FearA,FearD,FearCount,TrustV,TrustA,TrustD,TrustCount")
file1.write("\n")
#outputFile.write("\n")

#df=pd.read_csv("PlutchikClassifyOLD.csv")

with open('PlutchikClassifyFinal.csv', 'r') as rf:
    # read tweets
    reader = csv.reader(rf, delimiter=',')
    # for every tweet
    # id,username,date,tweet,emotion,anger,joy,surprise,fear,disgust,sadness,trust,anticipation,word,valence,arousa,dominance,emotions
    # flag=1
    emotionDict={"anger":[0.0,0.0,0.0,0.0],"joy":[0.0,0.0,0.0,0.0],"trust":[0.0,0.0,0.0,0.0],"anticipation":[0.0,0.0,0.0,0.0],"sadness":[0.0,0.0,0.0,0.0],"fear":[0.0,0.0,0.0,0.0],"surprise":[0.0,0.0,0.0,0.0],"disgust":[0.0,0.0,0.0,0.0]}
    next(reader)
    temp = '1'
    count=0
    flag=0
    username=""
    date=""
    tweet=""
    tweetEmotion=""

    anger=""
    surprise=""
    disgust=""
    joy=""
    sadness=""
    fear=""
    anticipation=""
    trust=""

    for tweetRow in reader:
        # get values from tweets.csv
        id1 = tweetRow[0]
        # if(id1 != temp):
        #     file1.write(str(id1)+","+ str(tweetRow[1])+"," + str(tweetRow[2])+","+str(tweetRow[3])+","+ str(tweetRow[4])+",")
        #     for emotion in emotionDict:
        #         print emotion
        #         if(emotionDict[emotion][3]!=0):
        #             emotionDict[emotion][0] = emotionDict[emotion][0]/emotionDict[emotion][3]
        #             emotionDict[emotion][1] = emotionDict[emotion][1]/emotionDict[emotion][3]
        #             emotionDict[emotion][2] = emotionDict[emotion][2]/emotionDict[emotion][3]
        #         file1.write(str(emotionDict[emotion][0]) + "," + str(emotionDict[emotion][1]) + "," + str(emotionDict[emotion][2])+","+ str(emotionDict[emotion][3])+",")
        #     file1.write("\n")          

        if (temp != id1):
            file1.write(str(temp)+","+ str(username)+"," + str(date)+","+str(tweet)+","+ str(tweetEmotion)+","+str(anger)+','+str(joy)+','+str(surprise)+','+str(fear)+','+str(disgust)+','+str(sadness)+','+str(trust)+','+str(anticipation)+",")
            for emotion in emotionDict:
                print temp
                if(emotionDict[emotion][3]!=0):
                    emotionDict[emotion][0] = emotionDict[emotion][0]/emotionDict[emotion][3]
                    emotionDict[emotion][1] = emotionDict[emotion][1]/emotionDict[emotion][3]
                    emotionDict[emotion][2] = emotionDict[emotion][2]/emotionDict[emotion][3]
                file1.write(str(emotionDict[emotion][0]) + "," + str(emotionDict[emotion][1]) + "," + str(emotionDict[emotion][2])+","+ str(emotionDict[emotion][3])+",")
        
            file1.write("\n")
            #print ("\n")
            print temp,username,date,emotionDict,anger,anticipation




        temp = id1  
        while temp == id1:
            username = tweetRow[1]
            date = tweetRow[2]
            tweet = tweetRow[3]
            tweetEmotion = tweetRow[4]
            anger=tweetRow[5]
            joy=tweetRow[6]
            surprise=tweetRow[7]
            fear=tweetRow[8]
            disgust=tweetRow[9]
            sadness=tweetRow[10]
            trust=tweetRow[11]
            anticipation=tweetRow[12]

            count+=1
            emotions=tweetRow[17].split('-')
            # print emotions
            del emotions[-1]
            emotions = [emotion.lower() for emotion in emotions]
            # print emotions, id1
            for emotion in emotions:
                # print emotion
                if(emotion!="positive" and emotion!= "negative"):
                    # print tweetRow[16]
                    #print "hi",tweetRow[14]
                    emotionDict[emotion][0]+=float(tweetRow[14])
                    emotionDict[emotion][1]+=float(tweetRow[15])
                    emotionDict[emotion][2]+=float(tweetRow[16])
                    # count
                    emotionDict[emotion][3]+=1
            tweetRow = next(reader)
            # input to file        file1.write(str(id1)+","+ str(tweetRow[1])+"," + str(tweetRow[2])+","+str(tweetRow[3])+","+ str(tweetRow[4])+",")
            temp=tweetRow[0]
       

            # print previous emotionDict to file
        file1.write(str(id1)+","+ str(username)+"," + str(date)+","+str(tweet)+","+ str(tweetEmotion)+","+str(anger)+','+str(joy)+','+str(surprise)+','+str(fear)+','+str(disgust)+','+str(sadness)+','+str(trust)+','+str(anticipation)+",")
        for emotion in emotionDict:
            # print emotion
            if(emotionDict[emotion][3]!=0):
                emotionDict[emotion][0] = emotionDict[emotion][0]/emotionDict[emotion][3]
                emotionDict[emotion][1] = emotionDict[emotion][1]/emotionDict[emotion][3]
                emotionDict[emotion][2] = emotionDict[emotion][2]/emotionDict[emotion][3]
            file1.write(str(emotionDict[emotion][0]) + "," + str(emotionDict[emotion][1]) + "," + str(emotionDict[emotion][2])+","+ str(emotionDict[emotion][3]) +",")
        file1.write("\n")
        print temp,username,date,emotionDict,anger,anticipation
        #print ("\n")
        

        #NEW TWEET
        emotionDict={"anger":[0,0,0,0],"joy":[0,0,0,0],"trust":[0,0,0,0],"anticipation":[0,0,0,0],"sadness":[0,0,0,0],"fear":[0,0,0,0],"surprise":[0,0,0,0],"disgust":[0,0,0,0]}
        emotions=tweetRow[17].split('-');
        del emotions[-1]
        emotions = [emotion.lower()  for emotion in emotions]
        for emotion in emotions:
            # print emotion,"hi",tweetRow[14]
            if(emotion!="positive" and emotion!= "negative"):
                emotionDict[emotion][0]+=float(tweetRow[14])
                emotionDict[emotion][1]+=float(tweetRow[15])
                emotionDict[emotion][2]+=float(tweetRow[16])
                # count
                emotionDict[emotion][3]+=1

        temp=tweetRow[0]
        username = tweetRow[1]
        date = tweetRow[2]
        tweet = tweetRow[3]
        tweetEmotion = tweetRow[4]

        anger=tweetRow[5]
        joy=tweetRow[6]
        surprise=tweetRow[7]
        fear=tweetRow[8]
        disgust=tweetRow[9]
        sadness=tweetRow[10]
        trust=tweetRow[11]
        anticipation=tweetRow[12]
        




