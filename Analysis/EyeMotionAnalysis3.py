import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import csv
from numpy import random
# =============================================================================
ColNames1 = ['TimePoint','Object','Pos']    # name of the columns of eye motion data
ColNames2 = ['SessionInd','CatchInd','Threshold','NumberOfRespondingAgents',    # name of the columns of behavioral data
            'Agents raised hand','Participant raised hand','Participant response time',
            'Congruency factor','Time1','Time2','Time3','RespondingAgents1','RespondingAgents2',
            'RespondingAgents3','RespondingAgents4','RespondingAgents5','RespondingAgents6',
            'RespondingAgents7','RespondingAgents8']
NP = 1     # number of participants
for a1 in np.arange(0,NP):
    Str1 = 'Hit_Data'   
    Str2 = str(a1+1)
    Str3 = ".txt"
    Name = Str1+Str2+Str3
    file = pd.read_csv(Name,names=ColNames1)    # read eye motion data
    
    if a1<9:
        Str1 = "P00"
    else:
        Str1 = "P0"    
    Str2 = str(a1+1)
    Str3 = "_OutputData.CSV"
    Name = Str1+Str2+Str3   
    df = pd.read_csv(Name,names=ColNames2) 
    df = df.drop(0,axis=0)
    # -------------------------------------------------------------------------
    timePoint = np.empty([len(file),1])     # initialze array for time points of gaze data
    Object = []     # initialize a list for objects that we gazed at
    Pos = np.empty([len(file),3])
    Discount = np.array([])
    fileLength = len(file)
    for a2 in np.flip(np.arange(0,fileLength)):
        if (file.iloc[a2,0].find('time_unity') >= 0):
            print(a2)
            file = file.drop([a2],axis='index')
        # tempStr = file.iloc[a2,0].split()
        # if (tempStr[0]=='time_unity'):
        #     print(a2)
        #     file = file.drop([a2],axis='index')
        #     fileLength = fileLength-1
    for a3 in np.arange(0,len(file)):
        tempStr = file.iloc[a3,0].split()     
        if (len(tempStr)>3):
            tempStr[1] = tempStr[1]+tempStr[2]
            tempStr[2] = tempStr[3]
        timePoint[a3] = tempStr[0]
        Object.append(tempStr[1])
        Pos[a3,0] = float(tempStr[2].replace("(", ""))
        Pos[a3,1] = file.iloc[a3,1]
        Pos[a3,2] = float(file.iloc[a3,2].replace(")", ""))
    # -------------------------------------------------------------------------
        
        
    # -------------------------------------------------------------------------
    Hits = np.zeros([len(df),11])
    # HitsTime = np.zeros[len(df),10]
    nAgents = df['NumberOfRespondingAgents']
    for a6 in np.arange(1,len(df)):
        # for a5 in np.arange(0,11):
        #     Hits[a6,a5] = 0
    # for a6 in np.arange(0,10):
        TrialStart = float(df.iloc[a6,8])
        TrialEnd = float(df.iloc[a6,10])
        if ((a6 == 319) & (TrialEnd <= TrialStart)):
            xxx =  np.where(timePoint >= TrialStart)
        else:
            xxx = np.where((timePoint >= TrialStart) & (timePoint <= TrialEnd))
        for a7 in np.arange(0,len(xxx[-2])):
            myNumbers = random.randint(0,nAgents[a6], size=(1,len(xxx[-2])))+1
            randomMess = random.randint(0,len(xxx[-2]), size=4)
            # randomMess = random.randint(0,len(xxx[-2]), size=random.randint(10,20))
            groups = {}
            for num1 in myNumbers[0,:]:
                if num1 not in groups:
                    groups[int(num1)] = []
                groups[int(num1)].append(int(num1))
            groupVals = np.array(sum(list(groups.values()),[]))
            # groupVals = sum(groupVals,[])
            # randomMessRange = randomMess[0:-2]
    for num2 in randomMess[::2]:
        print(num2)
        mySwip = random.randint(5,25)
        if (int(num2)+1+mySwip<len(groupVals)):
            temp1 = groupVals[int(num2):int(num2)+mySwip].copy()
            groupVals[int(num2):int(num2)+mySwip] = groupVals[int(num2)+1:int(num2)+1+mySwip]
            groupVals[int(num2)+1:int(num2)+1+mySwip] = temp1
            # hitObject = Object[xxx[-2][a7]-1]
            # print(hitObject)
            # if (len(Discount)==0):
            #     hitObject = Object[xxx[-2][a4]-1]
            # elif ((len(Discount)>=1) & (xxx[-2][a4]<Discount[0])):
            #         hitObject = Object[xxx[-2][a4]-1]
            # elif (((len(Discount)>=1) & (len(Discount)<2)) & (xxx[-2][a4]>Discount[0])):
            #     hitObject = Object[xxx[-2][a4]-2]
            # else:
            #     print("error")
            #     print(a3)
            # if hitObject == 'Female01':
            #     Hits[a3,0] = Hits[a3,0]+1
            #     # HitsTime[a3,0] = timePoint[a4]
            # elif hitObject == 'Female02':
            #     Hits[a3,1] = Hits[a3,1]+1
            # elif hitObject == 'Female03':
            #     Hits[a3,2] = Hits[a3,2]+1
            # elif hitObject == 'MixamoFemale01':
            #     Hits[a3,3] = Hits[a3,3]+1
            # elif hitObject == 'Male01':
            #     if (Pos[a4,0]>=0):
            #         Hits[a3,4] = Hits[a3,4]+1
            #     else:
            #         Hits[a3,7] = Hits[a3,7]+1
            # elif hitObject == 'Male02':
            #     Hits[a3,5] = Hits[a3,5]+1
            # elif hitObject == 'Male03':
            #     Hits[a3,6] = Hits[a3,6]+1
            # elif hitObject == 'SmallSquare(Clone)':
            #     Hits[a3,8] = Hits[a3,8]+1
            # elif hitObject == 'screen_projector':
            #     Hits[a3,9] = Hits[a3,9]+1
            # elif hitObject == 'Floor':
            #     Hits[a3,10] = Hits[a3,10]+1
    # df.to_csv(Name)