import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# =============================================================================
ColNames1 = ['TimePoint','Object','Pos']
ColNames2 = ['SessionInd','CatchInd','Threshold','NumberOfRespondingAgents',
            'Agents raised hand','Participant raised hand','Participant response time','Congruency factor','Time1','Time2','Time3']
NP = 50     # number of participants
for a1 in np.arange(0,NP):
    Str1 = 'Hit_Data'   
    Str2 = str(a1+1)
    Str3 = ".txt"
    Name = Str1+Str2+Str3
    file = pd.read_csv(Name,names=ColNames1)
    timePoint = np.empty([len(file),1])
    Object = []
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
    for a5 in np.arange(0,len(file)):
        tempStr = file.iloc[a5,0].split()     
        if (len(tempStr)>3):
            tempStr[1] = tempStr[1]+tempStr[2]
            tempStr[2] = tempStr[3]
        timePoint[a5] = tempStr[0]
        Object.append(tempStr[1])
        Pos[a5,0] = float(tempStr[2].replace("(", ""))
        Pos[a5,1] = file.iloc[a5,1]
        Pos[a5,2] = float(file.iloc[a5,2].replace(")", ""))
    if a1<9:
        Str1 = "P00"
    else:
        Str1 = "P0"    
    Str2 = str(a1+1)
    Str3 = "_OutputData.CSV"
    Name = Str1+Str2+Str3   
    df = pd.read_csv(Name,names=ColNames2)
    Hits = np.zeros([len(df),11])
    # HitsTime = np.zeros[len(df),10]
    for a3 in np.arange(0,len(df)):
        # for a5 in np.arange(0,11):
        #     Hits[a3,a5] = 0
    # for a3 in np.arange(0,10):
        TrialStart = df.iloc[a3,8]
        TrialEnd = df.iloc[a3,10]
        if ((a3 == 319) & (TrialEnd <= TrialStart)):
            xxx =  np.where(timePoint >= TrialStart)
        else:
            xxx = np.where((timePoint >= TrialStart) & (timePoint <= TrialEnd))
        for a4 in np.arange(0,len(xxx[-2])):
            hitObject = Object[xxx[-2][a4]-1]
            # if (len(Discount)==0):
            #     hitObject = Object[xxx[-2][a4]-1]
            # elif ((len(Discount)>=1) & (xxx[-2][a4]<Discount[0])):
            #         hitObject = Object[xxx[-2][a4]-1]
            # elif (((len(Discount)>=1) & (len(Discount)<2)) & (xxx[-2][a4]>Discount[0])):
            #     hitObject = Object[xxx[-2][a4]-2]
            # else:
            #     print("error")
            #     print(a3)
            if hitObject == 'Female01':
                Hits[a3,0] = Hits[a3,0]+1
                # HitsTime[a3,0] = timePoint[a4]
            elif hitObject == 'Female02':
                Hits[a3,1] = Hits[a3,1]+1
            elif hitObject == 'Female03':
                Hits[a3,2] = Hits[a3,2]+1
            elif hitObject == 'MixamoFemale01':
                Hits[a3,3] = Hits[a3,3]+1
            elif hitObject == 'Male01':
                if (Pos[a4,0]>=0):
                    Hits[a3,4] = Hits[a3,4]+1
                else:
                    Hits[a3,7] = Hits[a3,7]+1
            elif hitObject == 'Male02':
                Hits[a3,5] = Hits[a3,5]+1
            elif hitObject == 'Male03':
                Hits[a3,6] = Hits[a3,6]+1
            elif hitObject == 'SmallSquare(Clone)':
                Hits[a3,8] = Hits[a3,8]+1
            elif hitObject == 'screen_projector':
                Hits[a3,9] = Hits[a3,9]+1
            elif hitObject == 'Floor':
                Hits[a3,10] = Hits[a3,10]+1

    DF = pd.DataFrame(Hits)
    DF.to_csv('Hits'+str(a1+1)+'.csv')

    