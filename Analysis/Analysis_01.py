import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math as mt
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
    # Here, I check if the participant is an outlier or not (based on practice session)
    # Performance[a1] = len(df_Train[((df_Train['Threshold']==0.6) & (df_Train['Participant raised hand']==2)) | 
    #                                ((df_Train['Threshold']==0.4) & (df_Train['Participant raised hand']==1))])/ len(df_Train)
    
    # Here, I check if the participant is an outlier or not (based on catch trials)
    Performance[a1] = len(df_Test_Catch[((df_Test_Catch['Threshold']==0.6) & (df_Test_Catch['Participant raised hand']==2)) | 
                                   ((df_Test_Catch['Threshold']==0.4) & (df_Test_Catch['Participant raised hand']==1))])/ len(df_Test_Catch)
# =============================================================================
# -----------------------------------------------------------------------------
# =============================================================================
FollowPercentage = np.empty([50,1])  # Follow percentage in main trials
FollowPercentage1 = np.empty([50,1])  # Follow percentage in main trials with 1 agent
FollowPercentage2 = np.empty([50,1])  # Follow percentage in main trials with 2 agent
FollowPercentage3 = np.empty([50,1])  # Follow percentage in main trials with 3 agent
FollowPercentage4 = np.empty([50,1])  # Follow percentage in main trials with 4 agent
FollowPercentage5 = np.empty([50,1])  # Follow percentage in main trials with 5 agent
FollowPercentage6 = np.empty([50,1])  # Follow percentage in main trials with 6 agent
FollowPercentage7 = np.empty([50,1])  # Follow percentage in main trials with 7 agent
FollowPercentage8 = np.empty([50,1])  # Follow percentage in main trials with 8 agent
Outliers = np.where(Performance<=0.75)
for a1 in np.delete(np.arange(0,50),Outliers):
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
    df_Test = df[df['SessionInd']==2]
    df_Test_Catch = df_Test[df_Test['Threshold']!=0.5]
    df_Test_Main = df_Test[df_Test['Threshold']==0.5]
    FollowPercentage[a1] = len(df_Test_Main[(df_Test_Main['Participant raised hand']==1) & (df_Test_Main['Agents raised hand']==2)|
                                            (df_Test_Main['Participant raised hand']==2) & (df_Test_Main['Agents raised hand']==1)])/len(df_Test_Main)
    # -------------------------------------------------------------------------
    df_Test_Main1 = df_Test[(df_Test['Threshold']==0.5) & (df_Test['NumberOfRespondingAgents']==1)]
    if len(df_Test_Main1)!=0:
        FollowPercentage1[a1] = len(df_Test_Main1[(df_Test_Main1['Participant raised hand']==1) & (df_Test_Main1['Agents raised hand']==2)|
                                                  (df_Test_Main1['Participant raised hand']==2) & (df_Test_Main1['Agents raised hand']==1)])/len(df_Test_Main1)
    # -------------------------------------------------------------------------
    df_Test_Main2 = df_Test[(df_Test['Threshold']==0.5) & (df_Test['NumberOfRespondingAgents']==1)]
    if len(df_Test_Main2)!=0:
        FollowPercentage2[a1] = len(df_Test_Main2[(df_Test_Main2['Participant raised hand']==1) & (df_Test_Main2['Agents raised hand']==2)|
                                                  (df_Test_Main2['Participant raised hand']==2) & (df_Test_Main2['Agents raised hand']==1)])/len(df_Test_Main2)
    # -------------------------------------------------------------------------
    df_Test_Main3 = df_Test[(df_Test['Threshold']==0.5) & (df_Test['NumberOfRespondingAgents']==1)]
    if len(df_Test_Main3)!=0:
        FollowPercentage3[a1] = len(df_Test_Main3[(df_Test_Main3['Participant raised hand']==1) & (df_Test_Main3['Agents raised hand']==2)|
                                                  (df_Test_Main3['Participant raised hand']==2) & (df_Test_Main3['Agents raised hand']==1)])/len(df_Test_Main3)
    # -------------------------------------------------------------------------
    df_Test_Main4 = df_Test[(df_Test['Threshold']==0.5) & (df_Test['NumberOfRespondingAgents']==1)]
    if len(df_Test_Main4)!=0:
        FollowPercentage4[a1] = len(df_Test_Main4[(df_Test_Main4['Participant raised hand']==1) & (df_Test_Main4['Agents raised hand']==2)|
                                                  (df_Test_Main4['Participant raised hand']==2) & (df_Test_Main4['Agents raised hand']==1)])/len(df_Test_Main4)
    # -------------------------------------------------------------------------
    df_Test_Main5 = df_Test[(df_Test['Threshold']==0.5) & (df_Test['NumberOfRespondingAgents']==1)]
    if len(df_Test_Main5)!=0:
        FollowPercentage5[a1] = len(df_Test_Main5[(df_Test_Main5['Participant raised hand']==1) & (df_Test_Main5['Agents raised hand']==2)|
                                                  (df_Test_Main5['Participant raised hand']==2) & (df_Test_Main5['Agents raised hand']==1)])/len(df_Test_Main5)
    # -------------------------------------------------------------------------
    df_Test_Main6 = df_Test[(df_Test['Threshold']==0.5) & (df_Test['NumberOfRespondingAgents']==1)]
    if len(df_Test_Main6)!=0:
        FollowPercentage6[a1] = len(df_Test_Main6[(df_Test_Main6['Participant raised hand']==1) & (df_Test_Main6['Agents raised hand']==2)|
                                                  (df_Test_Main6['Participant raised hand']==2) & (df_Test_Main6['Agents raised hand']==1)])/len(df_Test_Main6)
    # -------------------------------------------------------------------------
    df_Test_Main7 = df_Test[(df_Test['Threshold']==0.5) & (df_Test['NumberOfRespondingAgents']==1)]
    if len(df_Test_Main7)!=0:
        FollowPercentage7[a1] = len(df_Test_Main7[(df_Test_Main7['Participant raised hand']==1) & (df_Test_Main7['Agents raised hand']==2)|
                                                  (df_Test_Main7['Participant raised hand']==2) & (df_Test_Main7['Agents raised hand']==1)])/len(df_Test_Main7)
    # -------------------------------------------------------------------------
    df_Test_Main8 = df_Test[(df_Test['Threshold']==0.5) & (df_Test['NumberOfRespondingAgents']==1)]
    if len(df_Test_Main8)!=0:   
        FollowPercentage8[a1] = len(df_Test_Main8[(df_Test_Main8['Participant raised hand']==1) & (df_Test_Main8['Agents raised hand']==2)|
                                                  (df_Test_Main8['Participant raised hand']==2) & (df_Test_Main8['Agents raised hand']==1)])/len(df_Test_Main8)
# =============================================================================
# Follow percentage plot and ANOVA
meanFollowPercentage = np.empty([8,1])
meanFollowPercentage[0] = np.nanmean(FollowPercentage1)
meanFollowPercentage[1] = np.nanmean(FollowPercentage2)
meanFollowPercentage[2] = np.nanmean(FollowPercentage3)
meanFollowPercentage[3] = np.nanmean(FollowPercentage4)
meanFollowPercentage[4] = np.nanmean(FollowPercentage5)
meanFollowPercentage[5] = np.nanmean(FollowPercentage6)
meanFollowPercentage[6] = np.nanmean(FollowPercentage7)
meanFollowPercentage[7] = np.nanmean(FollowPercentage8)
# -----------------------------------------------------------------------------
semFollowPercentage = np.empty([8,1])
semFollowPercentage[0] = np.nanstd(FollowPercentage1)/mt.sqrt(len(FollowPercentage1))
semFollowPercentage[1] = np.nanstd(FollowPercentage2)/mt.sqrt(len(FollowPercentage2))
semFollowPercentage[2] = np.nanstd(FollowPercentage3)/mt.sqrt(len(FollowPercentage3))
semFollowPercentage[3] = np.nanstd(FollowPercentage4)/mt.sqrt(len(FollowPercentage4))
semFollowPercentage[4] = np.nanstd(FollowPercentage5)/mt.sqrt(len(FollowPercentage5))
semFollowPercentage[5] = np.nanstd(FollowPercentage6)/mt.sqrt(len(FollowPercentage6))
semFollowPercentage[6] = np.nanstd(FollowPercentage7)/mt.sqrt(len(FollowPercentage7))
semFollowPercentage[7] = np.nanstd(FollowPercentage8)/mt.sqrt(len(FollowPercentage8))

x = np.arange(1,9)
# plt.plot(x.transpose(),meanFollowPercentage)
# plt.errorbar(x.transpose(),meanFollowPercentage,yerr=semFollowPercentage)
plt.errorbar(x, meanFollowPercentage.flatten(), yerr=semFollowPercentage.flatten(), 
             fmt='o', capsize=5)
plt.xlabel('X')
plt.ylabel('Mean Follow Percentage')
plt.title('Mean Follow Percentage with SEM Error Bars')
plt.show()