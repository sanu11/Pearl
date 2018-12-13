import csv
import re
file4 = open("F:/MS/Semester-4/DV/Project/Updatedatewordwise.txt","w")
arr = ["BarackObama"]
june1=["6/1/2018","6/2/2018","6/3/2018","6/4/2018","6/5/2018","6/6/2018","6/7/2018"]
june2=["6/8/2018","6/9/2018","6/10/2018","6/11/2018","6/12/2018","6/13/2018","6/14/2018"]
june3=["6/15/2018","6/16/2018","6/17/2018","6/18/2018","6/19/2018","6/20/2018","6/21/2018"]
june4=["6/22/2018","6/23/2018","6/24/2018","6/25/2018","6/26/2018","6/27/2018","6/28/2018"]
june5=["6/29/2018","6/30/2018","7/1/2018","7/2/2018","7/3/2018","7/4/2018","7/5/2018"]
june6=["7/6/2018","7/7/2018","7/8/2018","7/9/2018","7/10/2018","7/11/2018","7/12/2018"]
june7=["7/13/2018","7/14/2018","7/15/2018","7/16/2018","7/17/2018","7/18/2018","7/19/2018"]
june8=["7/20/2018","7/21/2018","7/22/2018","7/23/2018","7/24/2018","7/25/2018","7/26/2018"]
june9=["7/27/2018","7/28/2018","7/29/2018","7/30/2018","7/31/2018","8/1/2018","8/2/2018"]
june10=["8/3/2018","8/4/2018","8/5/2018","8/6/2018","8/7/2018","8/8/2018","8/9/2018"]
june11=["8/10/2018","8/11/2018","8/12/2018","8/13/2018","8/14/2018","8/15/2018","8/16/2018"]
june12=["8/17/2018","8/18/2018","8/19/2018","8/20/2018","8/21/2018","8/22/2018","8/23/2018"]
june13=["8/24/2018","8/25/2018","8/26/2018","8/27/2018","8/28/2018","8/29/2018","8/30/2018"]
june14=["8/31/2018","9/1/2018","9/2/2018","9/3/2018","9/4/2018","9/5/2018","9/6/2018"]
june15=["9/7/2018","9/8/2018","9/9/2018","9/10/2018","9/11/2018","9/12/2018","9/13/2018"]
june16=["9/14/2018","9/15/2018","9/16/2018","9/17/2018","9/18/2018","9/19/2018","9/20/2018"]
june17=["9/21/2018","9/22/2018","9/23/2018","9/24/2018","9/25/2018","9/26/2018","9/27/2018"]
june18=["9/28/2018","9/29/2018","9/30/2018"]
#Angerj1,Joyj1,Surprisej1,Fearj1,Disgustj1,Sadnessj1,Trustj1,Anticipationj1=0
l=[june1,june2,june3,june4,june5,june6,june7,june8,june9,june10,june11,june12,june13,june14,june15,june16,june17,june18]
l2=["narendramodi","BarackObama","realDonaldTrump"]
with open("F:/MS/Semester-4/DV/Project/Data sets/RNN_Weekwise1.csv", "wb") as csvfile:
    fieldnames = ['Username', 'Week','Anger', 'Joy','Surprise','Fear','Disgust','Sadness','Trust','Anticipation']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for m in l2:
        count=1
        for k in l:
            Angerj1 = 0
            Joyj1 = 0
            Surprisej1 = 0
            Fearj1 = 0
            Disgustj1 = 0
            Sadnessj1 = 0
            Trustj1 = 0
            Anticipationj1 = 0
            with open('F:/MS/Semester-4/DV/Project/Data sets/Updated_VADscores_Tweetwise.csv', 'r') as rf:
                reader = csv.reader(rf, delimiter=',')
                for row in reader:
                    if(row[1]==m):
                        temp=m
                        for i in k:
                            if(i==row[2]):
                                if(row[4]=="Anger"):
                                    Angerj1+=1
                                if (row[4] == "Joy"):
                                    Joyj1 += 1
                                if (row[4] == "Surprise"):
                                    Surprisej1 += 1
                                if (row[4] == "Fear"):
                                    Fearj1 += 1
                                if (row[4] == "Disgust"):
                                    Disgustj1 += 1
                                if (row[4] == "Sadness"):
                                    Sadnessj1 += 1
                                if (row[4] == "Trust"):
                                    Trustj1 += 1
                                if (row[4] == "Anticipation"):
                                    Anticipationj1 += 1
                writer.writerow( {'Username': temp, 'Week':count,'Anger': str(Angerj1), 'Joy': str(Joyj1), 'Surprise': str(Surprisej1),   'Fear': str(Fearj1), 'Disgust': str(Disgustj1), 'Sadness': str(Sadnessj1), 'Trust': str(Trustj1), 'Anticipation': str(Anticipationj1)})
                print (Angerj1,Joyj1,Surprisej1,Fearj1,Disgustj1,Sadnessj1,Trustj1,Anticipationj1)
            count+=1
