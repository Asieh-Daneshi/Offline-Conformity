# read the data file ==========================================================
import pandas as pd  
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