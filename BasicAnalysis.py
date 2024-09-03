# read the data file ==========================================================
import pandas as pd
import numpy as np  
df = pd.read_csv("OutputData.csv") 
# =============================================================================
# Column1 :> SessionInd; 	// if index==1, it is practice session, else, it is test session
# Column2 :> catchInd; 	// it is 1 if it is a catch. Otherwise, it is zero
# Column3 :> threshold; 	// yellow:0.6; blue:0.4
# Column4 :> numberOfAgents; 			// number of responding agents
# Column5 :> agents' raised hand: right:2; left:1
# Column6 :> participant's raised hand. right(blue):1; left(yellow):2
# Column7 :> participant's response time
# Column8 :> congruencyFactor: congruent:1; incongruent:2
# Column9 :> the time passed from the onset of experiment until participant responses
# Column10 :> responding agents (attention: if all 8 agents respond, the value is crazy! Don't look at it)
# Column11 :> the time passes from the unset of the experiment until the fixation disappears and next trial starts
# =============================================================================
SessionInd=df.iloc[:,0]         # if 2, then test session
Threshold=df.iloc[:,2]          # if 0.5, then main trials, else practice or catch trials
MainTrials=df[(SessionInd==2) & (Threshold ==0.5)]  # only main trials, 80% of trials are main trials
AllInd=df.index.values.tolist()                         # indices of all trials
MainInd=MainTrials.index.values.tolist()               # indices of main trials
for a1 in range(0, len(MainTrials)):
    MainTrials.loc[MainInd[a1],'Onset']=df.iloc[MainInd[a1]-1,10]   
    # "Onset" is the onset time of each trial (column 11)
    # "time from the onset of experiment" is the time passed since the experiment started until the participant responds or we report "missed trial" (column 8)
# =============================================================================
EyeData = pd.read_table('Hit_Data1.txt', sep=' ')
GazeTime=np.zeros((len(EyeData),1))
GazeObject=np.zeros((len(EyeData),1))

# In this loop, I organize the times and the objects that the participant has gazed on 
# time will be in "GazeTime" array, and objects will be in "GazeObject" array
for r1 in range(0, len(EyeData)): 
    temp0=EyeData.iloc[r1,0]
    temp1=temp0.split()
    GazeTime[r1,0]=temp1[0]
    tempObject=temp1[1]
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

# =============================================================================
# *****************************************************************************
# *******     Finding the time of gaze on each object at each trial     *******
# *****************************************************************************
GazeObjectTime=np.zeros((len(MainTrials),14))       # includes all the objects in the scene and the time that participants have spent gazing at each 
for a1 in range(0, len(MainTrials)):
    GazeTimeTrial=GazeTime[(GazeTime >= MainTrials.iloc[a1,11]) & (GazeTime <= (MainTrials.iloc[a1,11]+MainTrials.iloc[a1,6]))]
    GazeObjectTrial=GazeObject[(GazeTime >= MainTrials.iloc[a1,11]) & (GazeTime <= (MainTrials.iloc[a1,11]+MainTrials.iloc[a1,6]))]
    for a2 in range(1, len(GazeTimeTrial)-1):
        a3=a2
        while((GazeObjectTrial[a2]==GazeObjectTrial[a3-1]) & (a3>0)):
            a3=a3-1
        if ((GazeObjectTrial[a2+1]!=GazeObjectTrial[a2]) | (a2+1==len(GazeTimeTrial)-1)):

            GazeObjectTime[a1,int(GazeObjectTrial[a2])]=GazeObjectTime[a1,int(GazeObjectTrial[a2])]+(GazeTimeTrial[a2]-GazeTimeTrial[a3])
# =============================================================================
# *****************************************************************************
# ******************     Responding agents in each trial     ******************
# *****************************************************************************
RespondingAgents=np.zeros((len(MainTrials),9))       # includes all the objects in the scene and the time that participants have spent gazing at each 
for a1 in range(0, len(MainTrials)):
    if (MainTrials.iloc[a1,3]==8):
        RespondingAgents[a1,1]=1
        RespondingAgents[a1,2]=1
        RespondingAgents[a1,3]=1
        RespondingAgents[a1,4]=1
        RespondingAgents[a1,5]=1
        RespondingAgents[a1,6]=1
        RespondingAgents[a1,7]=1
        RespondingAgents[a1,8]=1
    else:
        tempList=list(map(int, str(int(MainTrials.iloc[a1,9]))))
        for a2 in range(0, len(tempList)):
            RespondingAgents[a1,tempList[a2]]=1
# =============================================================================
# *****************************************************************************
# Finfing the relation between responding agents and time spent gazing on them in each trial
# *****************************************************************************
GazeOnAgents=np.zeros((len(MainTrials),8))       # includes all the objects in the scene and the time that participants have spent gazing at each 
for a1 in range(0, len(MainTrials)):
    # GazeObjectTime:
    # column2 :> Female01
    # column3 :> Female02
    # column4 :> Female03
    # column5 :> MixamoFemale01
    # column6 :> Male01
    # column7 :> Male02
    # column8 :> Male03
    # column9 :> MixamoMale01
    tempAgents=RespondingAgents[a1,:]
    nonZeros=np.nonzero(tempAgents)[0]
    for a2 in range(0, len(nonZeros)):
        GazeOnAgents[a1,nonZeros[a2]-1]=GazeOnAgents[a1,nonZeros[a2]-1]+GazeObjectTime[a1,nonZeros[a2]]
        
# =============================================================================
sumGaze=GazeOnAgents.sum(axis=1)        # total time gazed on responding agents in each trial
# =============================================================================  
# Congruency |  Raised Hand  | Raised Color |
# -------------------------------------------
#     1      |       1       |   yellow     |
#     1      |       2       |    blue      |
#     2      |       1       |    blue      | 
#     2      |       2       |   yellow     |
# -------------------------------------------
# 
AgentsResponseColorBool=((MainTrials.iloc[:,4]-MainTrials.iloc[:,7])==0)
AgentsResponseColor=AgentsResponseColorBool.replace({True: 1, False: 0})    # yellow=1; blue=0
ParticipantsResponseColor=MainTrials.iloc[:,5]-1       # right(blue):0; left(yellow):1

FollowBool=(ParticipantsResponseColor==AgentsResponseColor)
Follow=FollowBool.replace({True: 1, False: 0})      # follow=1; not follow=0

FollowPercentage=Follow.sum(axis=0)/len(Follow)*100          # Total following percentage for each participant
# =============================================================================
# In this part, I figure out the relevance between the time gazed on responding agents and following or not!
FollowGazeTime=Follow*sumGaze
NotFollowGazeTime=(1-Follow)*sumGaze
averageFollowGazeTime=FollowGazeTime.mean(axis=0)       # average gaze time on responding agents in "Follow trials"
averageNotFollowGazeTime=NotFollowGazeTime.mean(axis=0) # average gaze time on responding agents in "Not follow trials"

# =============================================================================
GazeOnScreen=GazeObjectTime[:,10]
FollowOnScreen=Follow*GazeOnScreen
NotFollowOnScreen=(1-Follow)*GazeOnScreen
averageFollowOnScreenTime=FollowOnScreen.mean(axis=0)       # average gaze time on screen in "Follow trials"
averageNotFollowOnScreenTime=NotFollowOnScreen.mean(axis=0) # average gaze time on screen in "Not follow trials"