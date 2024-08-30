# read the data file ==========================================================
import pandas as pd
import numpy as np  
df = pd.read_csv("OutputData.csv") 
#==============================================================================
# Column1 :> SessionInd; 	// if index==1, it is practice session, else, it is test session
# Column2 :> catchInd; 	// it is 1 if it is a catch. Otherwise, it is zero
# Column3 :> threshold; 	// yellow:0.6; blue:0.4
# Column4 :> numberOfAgents; 			// number of responding agents
# Column5 :> agents' raise hand: right:2; left:1
# Column6 :> participant's raised hand. right(blue):1; left(yellow):2
# Column7 :> participant's response time
# Column8 :> responses[trialCounter,7]=congruencyFactor: congruent:1; incongruent:2
# Column9 :> the time passed from the onset of experiment until participant responses
# Column10 :> responding agents (attention: if all 8 agents respond, the value is crazy! Don't look at it)
# Column11 :> the time passes from the unset of the experiment until the fixation disappears and next trial starts
#==============================================================================
Threshold=df.iloc[:,3]
mainTrials=df[Threshold==6]     # in main trials, the ration of blue to yellow pixels is 50-50

df.iloc[:,]


#==============================================================================
EyeData = pd.read_table('Hit_Data1.txt', sep=' ')
GazeTime=np.zeros((len(EyeData),1))
GazeObject=np.zeros((len(EyeData),1))

for r1 in range(0, len(EyeData)): 
    temp0=EyeData.iloc[r1,0]
    temp1=temp0.split()
    GazeTime[r1,0]=temp1[0]
    tempObject=temp1[1]
    print(tempObject)
    match tempObject:
        case "Female01":
            GazeObject[r1,0]=1
        case "Female02":
            GazeObject[r1,0]=2
        case "Female03":
            GazeObject[r1,0]=3
        case "MixamoFemale01":
            GazeObject[r1,0]=4
        case "Male01":
            GazeObject[r1,0]=5
        case "Male02":
            GazeObject[r1,0]=6
        case "Male03":
            GazeObject[r1,0]=7
        case "MixamoMale01":
            GazeObject[r1,0]=8
        case "SmallSquare(Clone)":
            GazeObject[r1,0]=9
        case "Wall_Front":
            GazeObject[r1,0]=10
        case "Wall_Left":
            GazeObject[r1,0]=11
        case "Wall_Right":
            GazeObject[r1,0]=12
        case "Floor":
            GazeObject[r1,0]=13
        case _:
            GazeObject[r1,0]=0



