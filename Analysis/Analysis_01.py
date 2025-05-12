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
FollowPercentageCon1 = np.empty([50,1])  # Follow PercentageCon in main trials with 1 agent
FollowPercentageCon2 = np.empty([50,1])  # Follow PercentageCon in main trials with 2 agent
FollowPercentageCon3 = np.empty([50,1])  # Follow PercentageCon in main trials with 3 agent
FollowPercentageCon4 = np.empty([50,1])  # Follow PercentageCon in main trials with 4 agent
FollowPercentageCon5 = np.empty([50,1])  # Follow PercentageCon in main trials with 5 agent
FollowPercentageCon6 = np.empty([50,1])  # Follow PercentageCon in main trials with 6 agent
FollowPercentageCon7 = np.empty([50,1])  # Follow PercentageCon in main trials with 7 agent
FollowPercentageCon8 = np.empty([50,1])  # Follow PercentageCon in main trials with 8 agent

FollowPercentageIncon1 = np.empty([50,1])  # Follow PercentageIncon in main trials with 1 agent
FollowPercentageIncon2 = np.empty([50,1])  # Follow PercentageIncon in main trials with 2 agent
FollowPercentageIncon3 = np.empty([50,1])  # Follow PercentageIncon in main trials with 3 agent
FollowPercentageIncon4 = np.empty([50,1])  # Follow PercentageIncon in main trials with 4 agent
FollowPercentageIncon5 = np.empty([50,1])  # Follow PercentageIncon in main trials with 5 agent
FollowPercentageIncon6 = np.empty([50,1])  # Follow PercentageIncon in main trials with 6 agent
FollowPercentageIncon7 = np.empty([50,1])  # Follow PercentageIncon in main trials with 7 agent
FollowPercentageIncon8 = np.empty([50,1])  # Follow PercentageIncon in main trials with 8 agent

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
    
    df_Test_Con = df_Test[df_Test['Congruency factor']==1]
    df_Test_Incon = df_Test[df_Test['Congruency factor']==2]
    # -------------------------------------------------------------------------
    df_Test_Con_Main1 = df_Test_Con[(df_Test_Con['Threshold']==0.5) & (df_Test_Con['NumberOfRespondingAgents']==1)]
    if len(df_Test_Con_Main1)!=0:
        FollowPercentageCon1[a1] = len(df_Test_Con_Main1[(df_Test_Con_Main1['Participant raised hand']==1) & (df_Test_Con_Main1['Agents raised hand']==2)|
                                                  (df_Test_Con_Main1['Participant raised hand']==2) & (df_Test_Con_Main1['Agents raised hand']==1)])/len(df_Test_Con_Main1)
    # -------------------------------------------------------------------------
    df_Test_Con_Main2 = df_Test_Con[(df_Test_Con['Threshold']==0.5) & (df_Test_Con['NumberOfRespondingAgents']==2)]
    if len(df_Test_Con_Main2)!=0:
        FollowPercentageCon2[a1] = len(df_Test_Con_Main2[(df_Test_Con_Main2['Participant raised hand']==1) & (df_Test_Con_Main2['Agents raised hand']==2)|
                                                  (df_Test_Con_Main2['Participant raised hand']==2) & (df_Test_Con_Main2['Agents raised hand']==1)])/len(df_Test_Con_Main2)
    # -------------------------------------------------------------------------
    df_Test_Con_Main3 = df_Test_Con[(df_Test_Con['Threshold']==0.5) & (df_Test_Con['NumberOfRespondingAgents']==3)]
    if len(df_Test_Con_Main3)!=0:
        FollowPercentageCon3[a1] = len(df_Test_Con_Main3[(df_Test_Con_Main3['Participant raised hand']==1) & (df_Test_Con_Main3['Agents raised hand']==2)|
                                                  (df_Test_Con_Main3['Participant raised hand']==2) & (df_Test_Con_Main3['Agents raised hand']==1)])/len(df_Test_Con_Main3)
    # -------------------------------------------------------------------------
    df_Test_Con_Main4 = df_Test_Con[(df_Test_Con['Threshold']==0.5) & (df_Test_Con['NumberOfRespondingAgents']==4)]
    if len(df_Test_Con_Main4)!=0:
        FollowPercentageCon4[a1] = len(df_Test_Con_Main4[(df_Test_Con_Main4['Participant raised hand']==1) & (df_Test_Con_Main4['Agents raised hand']==2)|
                                                  (df_Test_Con_Main4['Participant raised hand']==2) & (df_Test_Con_Main4['Agents raised hand']==1)])/len(df_Test_Con_Main4)
    # -------------------------------------------------------------------------
    df_Test_Con_Main5 = df_Test_Con[(df_Test_Con['Threshold']==0.5) & (df_Test_Con['NumberOfRespondingAgents']==5)]
    if len(df_Test_Con_Main5)!=0:
        FollowPercentageCon5[a1] = len(df_Test_Con_Main5[(df_Test_Con_Main5['Participant raised hand']==1) & (df_Test_Con_Main5['Agents raised hand']==2)|
                                                  (df_Test_Con_Main5['Participant raised hand']==2) & (df_Test_Con_Main5['Agents raised hand']==1)])/len(df_Test_Con_Main5)
    # -------------------------------------------------------------------------
    df_Test_Con_Main6 = df_Test_Con[(df_Test_Con['Threshold']==0.5) & (df_Test_Con['NumberOfRespondingAgents']==6)]
    if len(df_Test_Con_Main6)!=0:
        FollowPercentageCon6[a1] = len(df_Test_Con_Main6[(df_Test_Con_Main6['Participant raised hand']==1) & (df_Test_Con_Main6['Agents raised hand']==2)|
                                                  (df_Test_Con_Main6['Participant raised hand']==2) & (df_Test_Con_Main6['Agents raised hand']==1)])/len(df_Test_Con_Main6)
    # -------------------------------------------------------------------------
    df_Test_Con_Main7 = df_Test_Con[(df_Test_Con['Threshold']==0.5) & (df_Test_Con['NumberOfRespondingAgents']==7)]
    if len(df_Test_Con_Main7)!=0:
        FollowPercentageCon7[a1] = len(df_Test_Con_Main7[(df_Test_Con_Main7['Participant raised hand']==1) & (df_Test_Con_Main7['Agents raised hand']==2)|
                                                  (df_Test_Con_Main7['Participant raised hand']==2) & (df_Test_Con_Main7['Agents raised hand']==1)])/len(df_Test_Con_Main7)
    # -------------------------------------------------------------------------
    df_Test_Con_Main8 = df_Test_Con[(df_Test_Con['Threshold']==0.5) & (df_Test_Con['NumberOfRespondingAgents']==8)]
    if len(df_Test_Con_Main8)!=0:   
        FollowPercentageCon8[a1] = len(df_Test_Con_Main8[(df_Test_Con_Main8['Participant raised hand']==1) & (df_Test_Con_Main8['Agents raised hand']==2)|
                                                  (df_Test_Con_Main8['Participant raised hand']==2) & (df_Test_Con_Main8['Agents raised hand']==1)])/len(df_Test_Con_Main8)
    # -------------------------------------------------------------------------
    df_Test_Incon_Main1 = df_Test_Incon[(df_Test_Incon['Threshold']==0.5) & (df_Test_Incon['NumberOfRespondingAgents']==1)]
    if len(df_Test_Incon_Main1)!=0:
        FollowPercentageIncon1[a1] = len(df_Test_Incon_Main1[(df_Test_Incon_Main1['Participant raised hand']==1) & (df_Test_Incon_Main1['Agents raised hand']==2)|
                                                  (df_Test_Incon_Main1['Participant raised hand']==2) & (df_Test_Incon_Main1['Agents raised hand']==1)])/len(df_Test_Incon_Main1)
    # -------------------------------------------------------------------------
    df_Test_Incon_Main2 = df_Test_Incon[(df_Test_Incon['Threshold']==0.5) & (df_Test_Incon['NumberOfRespondingAgents']==2)]
    if len(df_Test_Incon_Main2)!=0:
        FollowPercentageIncon2[a1] = len(df_Test_Incon_Main2[(df_Test_Incon_Main2['Participant raised hand']==1) & (df_Test_Incon_Main2['Agents raised hand']==2)|
                                                  (df_Test_Incon_Main2['Participant raised hand']==2) & (df_Test_Incon_Main2['Agents raised hand']==1)])/len(df_Test_Incon_Main2)
    # -------------------------------------------------------------------------
    df_Test_Incon_Main3 = df_Test_Incon[(df_Test_Incon['Threshold']==0.5) & (df_Test_Incon['NumberOfRespondingAgents']==3)]
    if len(df_Test_Incon_Main3)!=0:
        FollowPercentageIncon3[a1] = len(df_Test_Incon_Main3[(df_Test_Incon_Main3['Participant raised hand']==1) & (df_Test_Incon_Main3['Agents raised hand']==2)|
                                                  (df_Test_Incon_Main3['Participant raised hand']==2) & (df_Test_Incon_Main3['Agents raised hand']==1)])/len(df_Test_Incon_Main3)
    # -------------------------------------------------------------------------
    df_Test_Incon_Main4 = df_Test_Incon[(df_Test_Incon['Threshold']==0.5) & (df_Test_Incon['NumberOfRespondingAgents']==4)]
    if len(df_Test_Incon_Main4)!=0:
        FollowPercentageIncon4[a1] = len(df_Test_Incon_Main4[(df_Test_Incon_Main4['Participant raised hand']==1) & (df_Test_Incon_Main4['Agents raised hand']==2)|
                                                  (df_Test_Incon_Main4['Participant raised hand']==2) & (df_Test_Incon_Main4['Agents raised hand']==1)])/len(df_Test_Incon_Main4)
    # -------------------------------------------------------------------------
    df_Test_Incon_Main5 = df_Test_Incon[(df_Test_Incon['Threshold']==0.5) & (df_Test_Incon['NumberOfRespondingAgents']==5)]
    if len(df_Test_Incon_Main5)!=0:
        FollowPercentageIncon5[a1] = len(df_Test_Incon_Main5[(df_Test_Incon_Main5['Participant raised hand']==1) & (df_Test_Incon_Main5['Agents raised hand']==2)|
                                                  (df_Test_Incon_Main5['Participant raised hand']==2) & (df_Test_Incon_Main5['Agents raised hand']==1)])/len(df_Test_Incon_Main5)
    # -------------------------------------------------------------------------
    df_Test_Incon_Main6 = df_Test_Incon[(df_Test_Incon['Threshold']==0.5) & (df_Test_Incon['NumberOfRespondingAgents']==6)]
    if len(df_Test_Incon_Main6)!=0:
        FollowPercentageIncon6[a1] = len(df_Test_Incon_Main6[(df_Test_Incon_Main6['Participant raised hand']==1) & (df_Test_Incon_Main6['Agents raised hand']==2)|
                                                  (df_Test_Incon_Main6['Participant raised hand']==2) & (df_Test_Incon_Main6['Agents raised hand']==1)])/len(df_Test_Incon_Main6)
    # -------------------------------------------------------------------------
    df_Test_Incon_Main7 = df_Test_Incon[(df_Test_Incon['Threshold']==0.5) & (df_Test_Incon['NumberOfRespondingAgents']==7)]
    if len(df_Test_Incon_Main7)!=0:
        FollowPercentageIncon7[a1] = len(df_Test_Incon_Main7[(df_Test_Incon_Main7['Participant raised hand']==1) & (df_Test_Incon_Main7['Agents raised hand']==2)|
                                                  (df_Test_Incon_Main7['Participant raised hand']==2) & (df_Test_Incon_Main7['Agents raised hand']==1)])/len(df_Test_Incon_Main7)
    # -------------------------------------------------------------------------
    df_Test_Incon_Main8 = df_Test_Incon[(df_Test_Incon['Threshold']==0.5) & (df_Test_Incon['NumberOfRespondingAgents']==8)]
    if len(df_Test_Incon_Main8)!=0:   
        FollowPercentageIncon8[a1] = len(df_Test_Incon_Main8[(df_Test_Incon_Main8['Participant raised hand']==1) & (df_Test_Incon_Main8['Agents raised hand']==2)|
                                                  (df_Test_Incon_Main8['Participant raised hand']==2) & (df_Test_Incon_Main8['Agents raised hand']==1)])/len(df_Test_Incon_Main8)
# =============================================================================
# Follow percentage plot and ANOVA
meanFollowPercentageCon = np.empty([8,1])
meanFollowPercentageCon[0] = np.nanmean(FollowPercentageCon1)
meanFollowPercentageCon[1] = np.nanmean(FollowPercentageCon2)
meanFollowPercentageCon[2] = np.nanmean(FollowPercentageCon3)
meanFollowPercentageCon[3] = np.nanmean(FollowPercentageCon4)
meanFollowPercentageCon[4] = np.nanmean(FollowPercentageCon5)
meanFollowPercentageCon[5] = np.nanmean(FollowPercentageCon6)
meanFollowPercentageCon[6] = np.nanmean(FollowPercentageCon7)
meanFollowPercentageCon[7] = np.nanmean(FollowPercentageCon8)
# -----------------------------------------------------------------------------
semFollowPercentageCon = np.empty([8,1])
semFollowPercentageCon[0] = np.nanstd(FollowPercentageCon1)/mt.sqrt(len(FollowPercentageCon1))
semFollowPercentageCon[1] = np.nanstd(FollowPercentageCon2)/mt.sqrt(len(FollowPercentageCon2))
semFollowPercentageCon[2] = np.nanstd(FollowPercentageCon3)/mt.sqrt(len(FollowPercentageCon3))
semFollowPercentageCon[3] = np.nanstd(FollowPercentageCon4)/mt.sqrt(len(FollowPercentageCon4))
semFollowPercentageCon[4] = np.nanstd(FollowPercentageCon5)/mt.sqrt(len(FollowPercentageCon5))
semFollowPercentageCon[5] = np.nanstd(FollowPercentageCon6)/mt.sqrt(len(FollowPercentageCon6))
semFollowPercentageCon[6] = np.nanstd(FollowPercentageCon7)/mt.sqrt(len(FollowPercentageCon7))
semFollowPercentageCon[7] = np.nanstd(FollowPercentageCon8)/mt.sqrt(len(FollowPercentageCon8))
# -----------------------------------------------------------------------------
meanFollowPercentageIncon = np.empty([8,1])
meanFollowPercentageIncon[0] = np.nanmean(FollowPercentageIncon1)
meanFollowPercentageIncon[1] = np.nanmean(FollowPercentageIncon2)
meanFollowPercentageIncon[2] = np.nanmean(FollowPercentageIncon3)
meanFollowPercentageIncon[3] = np.nanmean(FollowPercentageIncon4)
meanFollowPercentageIncon[4] = np.nanmean(FollowPercentageIncon5)
meanFollowPercentageIncon[5] = np.nanmean(FollowPercentageIncon6)
meanFollowPercentageIncon[6] = np.nanmean(FollowPercentageIncon7)
meanFollowPercentageIncon[7] = np.nanmean(FollowPercentageIncon8)
# -----------------------------------------------------------------------------
semFollowPercentageIncon = np.empty([8,1])
semFollowPercentageIncon[0] = np.nanstd(FollowPercentageIncon1)/mt.sqrt(len(FollowPercentageIncon1))
semFollowPercentageIncon[1] = np.nanstd(FollowPercentageIncon2)/mt.sqrt(len(FollowPercentageIncon2))
semFollowPercentageIncon[2] = np.nanstd(FollowPercentageIncon3)/mt.sqrt(len(FollowPercentageIncon3))
semFollowPercentageIncon[3] = np.nanstd(FollowPercentageIncon4)/mt.sqrt(len(FollowPercentageIncon4))
semFollowPercentageIncon[4] = np.nanstd(FollowPercentageIncon5)/mt.sqrt(len(FollowPercentageIncon5))
semFollowPercentageIncon[5] = np.nanstd(FollowPercentageIncon6)/mt.sqrt(len(FollowPercentageIncon6))
semFollowPercentageIncon[6] = np.nanstd(FollowPercentageIncon7)/mt.sqrt(len(FollowPercentageIncon7))
semFollowPercentageIncon[7] = np.nanstd(FollowPercentageIncon8)/mt.sqrt(len(FollowPercentageIncon8))
x = np.arange(1,9)
# plt.plot(x.transpose(),meanFollowPercentage)
# plt.errorbar(x.transpose(),meanFollowPercentage,yerr=semFollowPercentage)
plt.errorbar(x, meanFollowPercentageCon.flatten(), yerr=semFollowPercentageCon.flatten(), 
             fmt='o', capsize=5)
plt.errorbar(x, meanFollowPercentageIncon.flatten(), yerr=semFollowPercentageIncon.flatten(), 
             fmt='o', capsize=5)
plt.xlabel('X')
plt.ylabel('Mean Follow Percentage')
plt.title('Mean Follow Percentage with SEM Error Bars')
plt.show()