import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
# =============================================================================
ColNames1 = ['TimePoint','Object','Pos']    # name of the columns of eye motion data
ColNames2 = ['SessionInd','CatchInd','Threshold','NumberOfRespondingAgents',    # name of the columns of behavioral data
            'Agents raised hand','Participant raised hand','Participant response time','Congruency factor','Time1','Time2','Time3']
NP = 50     # number of participants
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
    nAgents = df['NumberOfRespondingAgents']
    RespondingAgents = np.zeros([320,8])
    for a2 in np.arange(0,320):
        RespondingAgents[a2,0:int(nAgents[a2])] = random.sample(range(1,9),int(nAgents[a2]))
