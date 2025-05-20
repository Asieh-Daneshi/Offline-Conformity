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
    for a2 in np.arange(1,len(file)):
        tempStr = file.iloc[a2,0].split()
        if (tempStr[0]!='time_unity'):
            if (len(tempStr)>3):
                tempStr[1] = tempStr[1]+tempStr[2]
                tempStr[2] = tempStr[3]
            timePoint[a2] = tempStr[0]
            Object.append(tempStr[1])
            Pos[a2,0] = float(tempStr[2].replace("(", ""))
            Pos[a2,1] = file.iloc[a2,1]
            Pos[a2,2] = float(file.iloc[a2,2].replace(")", ""))
    if a1<9:
        Str1 = "P00"
    else:
        Str1 = "P0"    
    Str2 = str(a1+1)
    Str3 = "_OutputData.CSV"
    Name = Str1+Str2+Str3   
    df = pd.read_csv(Name,names=ColNames2)
    Hits = np.zeros([len(df),11])
    for a3 in np.arange(0,len(df)):
    # for a3 in np.arange(0,10):
        TrialStart = df.iloc[a3,8]
        TrialEnd = df.iloc[a3,10]
        if ((a3 == 319) & (TrialEnd <= TrialStart)):
            xxx =  np.where(timePoint >= TrialStart)
        else:
            xxx = np.where((timePoint >= TrialStart) & (timePoint <= TrialEnd))
        for a4 in np.arange(0,len(xxx[-2])):
            hitObject = Object[a4]
            if hitObject == 'Female01':
                Hits[a3,0] = Hits[a3,0]+1
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
                    Hits[a3,7] = Hits[a3,4]+1
            elif hitObject == 'Male02':
                Hits[a3,5] = Hits[a3,5]+1
            elif hitObject == 'Male03':
                Hits[a3,6] = Hits[a3,6]+1
            elif hitObject == 'SmallSquare(Clone)':
                Hits[a3,8] = Hits[a3,8]+1
            elif hitObject == 'screen_projector':
                Hits[a3,9] = Hits[a3,9]+1
            elif hitObject == 'Floor':
                Hits[a3,9] = Hits[a3,10]+1
            
