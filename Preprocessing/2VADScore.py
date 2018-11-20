import csv
import re
outputFile = open("PlutchikClassify.csv","w")
outputFile.write("id,username,date,tweet,emotion,anger,joy,surprise,fear,disgust,sadness,trust,anticipation,word,valence,arousa,dominance,emotions")
outputFile.write("\n")
with open('tweets.csv', 'r') as rf:
    # read tweets
    reader = csv.reader(rf, delimiter=',')
    # for every tweet
    # id,username,date,tweet,sentimentvalue,category,emotion,anger,joy,surprise,fear,disgust,sadness,trust,anticipation
    for tweetRow in reader:
        # get values from tweets.csv
        id1 = tweetRow[0]
        username = tweetRow[1]
        date = tweetRow[2]
        tweet = tweetRow[3]
        emotion = tweetRow[6]
        anger = tweetRow[7]
        joy = tweetRow[8]
        surprise = tweetRow[9]
        fear = tweetRow[10]
        disgust = tweetRow[11]
        sadness = tweetRow[12]
        trust = tweetRow[13]
        anticipation = tweetRow[14]
       
        # get words
        tweetWords = tweet.split()
        count = len(tweetWords)


        # open lexicon dict that has VAD values for words.
        with open('VADLexicon.csv', 'r') as vadFile:
            reader1 = csv.reader(vadFile, delimiter=',')
            # for every word in lexicon see if that word is there in tweet. So if so use its VAD score and write it to file.
            temp = ""
            for line in reader1:
                # word 
                dictWord= line[0]       
                # if word from dict present in tweet
                if dictWord in tweetWords:
                    # get VAD values 
                    # print("hiii")
                    # print("hi",temp,dictWord)
                    if dictWord == temp:
                        continue
                    stri= re.search('[a-zA-Z]+',line[1])
                    if(stri != None):
                        valence=line[2]
                        dominance = line[3]
                        arousal = line[4]
                    else:
                        valence = line[1]
                        dominance = line[2]
                        arousal = line[3]
                    emotions=""
                    flag=0
                    temp = dictWord
                    # print (temp)
                    
                    with open('PlutchikLexicon.csv', 'r') as plutchikFile:
                        reader2 = csv.reader(plutchikFile, delimiter=',')
                        for line2 in reader2:
                            if dictWord == line2[0]:
                                if(line2[2]=='1'):
                                    # print(dictWord,line2[0])
                                    flag=1
                                    emotions+=line2[1]+ "-"
                    if (flag==0):
                        emotions="-"

                    # print (emotions)
                    outputFile.write(id1+","+ username + ","+date+","+tweet+"," + emotion+","+anger+","+joy\
                        +","+surprise+","+fear+","+disgust+","+sadness+","+trust+","+anticipation \
                      +","+dictWord +","+valence + "," + arousal + "," + dominance + ","+ emotions)
                    outputFile.write("\n")