import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# =============================================================================
ColNames = ['TimePoint','Object','Pos']

NP = 50     # number of participants
for a1 in np.arange(0,1):
    Str1 = 'Hit_Data'   
    Str2 = str(a1+1)
    Str3 = ".txt"
    Name = Str1+Str2+Str3
    file = pd.read_csv(Name,names=ColNames)
    timePoint = np.empty([len(file),1])
    Object = []
    Pos = np.empty([len(file),3])
    for a2 in np.arange(1,len(file)):
        tempStr = file.iloc[a2,0].split()
        if (len(tempStr)>3):
            tempStr[1] = tempStr[1]+tempStr[2]
            tempStr[2] = tempStr[3]
        timePoint[a2] = tempStr[0]
        Object.append(tempStr[1])
        Pos[a2,0] = float(tempStr[2].replace("(", ""))
        Pos[a2,1] = file.iloc[1,1]
        Pos[a2,2] = float(file.iloc[1,2].replace(")", ""))
    