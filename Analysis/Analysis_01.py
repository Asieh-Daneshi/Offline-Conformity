import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# =============================================================================
# Column1: SessionInd; Practice:1, Test=2
# Column2: CatchInd; Catch=1, Main=0
# Column3: Threshold; 0.5: Main trials, 0.6: dominant color is yellow, 0.4: dominant color is blue
# Column4: NumberOfRespondingAgents; 
# Column5: Agents' raised hand; Right:2, Left:1
# Column6: Participant's raised hand; Right:Blue:1, Left:Yellow:2
# Column7: Participant's response time
# Column8: Congruency factor; Congruent:1, Incongruent:2
# =============================================================================
ColNames = ['SessionInd','CatchInd','Threshold','NumberOfRespondingAgents',
            'Agents raised hand','Participant raised hand','Participant response time','Congruency factor','Time1','Time2','Time3']
Performance = np.empty([50,1])  # Performance on Train session
for a1 in np.arange(0,50):
    if a1<9:
        Str1 = "P00"
    else:
        Str1 = "P0"    
    Str2 = str(a1+1)
    Str3 = "_OutputData.CSV"
    Name = Str1+Str2+Str3
    df = pd.read_csv(Name,names=ColNames)
    # Here, I remove column 'CatchInd', because it is not correct (It is always 1). 
    # Instead, I use the threshold to distiguish catch trials. When it is not 0.5, it is a catch trial.
    df = df.drop('CatchInd', axis=1)
    # df_Train = df.iloc[0:20,:]
    # df_Test = df.iloc[20:319,:]
    df_Train = df[df['SessionInd']==1]
    df_Test = df[df['SessionInd']==2]
    df_Test_Catch = df_Test[df_Test['Threshold']!=0.5]
    df_Test_Main = df_Test[df_Test['Threshold']==0.5]
    
    # -------------------------------------------------------------------------
    # Here, I check if the participant is an outlier or not
    Performance[a1] = len(df_Train[((df_Train['Threshold']==0.6) & (df_Train['Participant raised hand']==2)) | 
                                   ((df_Train['Threshold']==0.4) & (df_Train['Participant raised hand']==1))])/ len(df_Train)
Outliers = Performance<=0.75