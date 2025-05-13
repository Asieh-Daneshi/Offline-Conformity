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
NP = 50         # number of participants
Performance = np.empty([NP,1])  # Performance on Train session
for a1 in np.arange(0,NP):
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
FollowPercentage = np.empty([NP,1])  # Follow percentage in main trials
for a1 in np.arange(1,9):
    Name1 = 'FollowPercentageCon'+str(a1)
    globals()[Name1] = np.empty([NP,1])    # Follow PercentageCon in main trials with a1 agent
    globals()[Name1][:]=np.nan
    Name2 = 'FollowPercentageIncon'+str(a1)
    globals()[Name2] = np.empty([NP,1])    # Follow PercentageIncon in main trials with a1 agent
    globals()[Name2][:]=np.nan

Outliers = np.where(Performance<=0.75)
for a1 in np.delete(np.arange(0,NP),Outliers[0]):
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
    
    df_Test_Con = df_Test[df_Test['Congruency factor']==1]
    df_Test_Incon = df_Test[df_Test['Congruency factor']==2]
    # -------------------------------------------------------------------------
    # calculating follow percentage for all participants
    for a2 in np.arange(1,9):
        temp1 = df_Test_Con[(df_Test_Con['Threshold']==0.5) & (df_Test_Con['NumberOfRespondingAgents']==a2)]
        if len(temp1) != 0:
            name3 = 'FollowPercentageCon'+str(a2)
            globals()[name3][a1] = len(temp1[(temp1['Participant raised hand']==1) & (temp1['Agents raised hand']==2)|
                                                      (temp1['Participant raised hand']==2) & (temp1['Agents raised hand']==1)])/len(temp1)
        # -------------------------------------------------------------------------
        temp2 = df_Test_Incon[(df_Test_Incon['Threshold']==0.5) & (df_Test_Incon['NumberOfRespondingAgents']==a2)]
        if len(temp2) != 0:
            name4 = 'FollowPercentageIncon'+str(a2)
            globals()[name4][a1] = len(temp2[(temp2['Participant raised hand']==1) & (temp2['Agents raised hand']==2)|
                                                      (temp2['Participant raised hand']==2) & (temp2['Agents raised hand']==1)])/len(temp2)
# =============================================================================
# Follow percentage plot and ANOVA
# =============================================================================
# mean and sem follow percentage across participants
meanFollowPercentageCon = np.empty([8,1])
semFollowPercentageCon = np.empty([8,1])
meanFollowPercentageIncon = np.empty([8,1])
semFollowPercentageIncon = np.empty([8,1])
for a1 in np.arange(0,8):
    meanFollowPercentageCon[a1] = np.nanmean(globals()['FollowPercentageCon'+str(a1+1)])
    semFollowPercentageCon[a1] = np.nanstd(globals()['FollowPercentageCon'+str(a1+1)])/mt.sqrt(len(globals()['FollowPercentageCon'+str(a1+1)]))
    meanFollowPercentageIncon[a1] = np.nanmean(globals()['FollowPercentageIncon'+str(a1+1)])
    semFollowPercentageIncon[a1] = np.nanstd(globals()['FollowPercentageIncon'+str(a1+1)])/mt.sqrt(len(globals()['FollowPercentageIncon'+str(a1+1)]))
# =============================================================================
# bar plot with errorbar
# =============================================================================
NumAgents = np.arange(1,9)      # number of responding agents
plt.bar(NumAgents-0.2,meanFollowPercentageCon.flatten(),width=0.4,facecolor='#219EBC',edgecolor='#023047')
plt.errorbar(NumAgents-0.2,meanFollowPercentageCon.flatten(), yerr=semFollowPercentageCon.flatten(), 
             fmt='o', capsize=5, color='#023047')
plt.bar(NumAgents+0.2,meanFollowPercentageIncon.flatten(),width=0.4,facecolor='#FFB703',edgecolor='#FB8500')
plt.errorbar(NumAgents+0.2, meanFollowPercentageIncon.flatten(), yerr=semFollowPercentageIncon.flatten(), 
             fmt='o', capsize=5, color='#FB8500')
plt.xlabel('Number of Responding Agents')
plt.ylabel('Mean Follow Percentage')
plt.title('Mean Follow Percentage with SEM Error Bars')
plt.show()
# =============================================================================
NPR = NP -len(Outliers[0])     # number of remaining participants fater removing outliers
# Participants
ParticipantNumber = np.repeat(np.arange(1,NPR+1),16)
# number of responding agents
NA = np.arange(1,9)
NumberOfAgents = np.tile(NA,NPR*2)
# congruency (congruent=1; incongruent=0)
Con = np.concatenate((np.ones([8]),np.zeros([8])),axis=0)
Congruency = np.tile(Con,NPR)
FollowPercentageAll = np.transpose(np.stack([FollowPercentageCon1,FollowPercentageIncon1,FollowPercentageCon2,FollowPercentageIncon2,
                                             FollowPercentageCon3,FollowPercentageIncon3,FollowPercentageCon4,FollowPercentageIncon4,
                                             FollowPercentageCon5,FollowPercentageIncon5,FollowPercentageCon6,FollowPercentageIncon6,
                                             FollowPercentageCon7,FollowPercentageIncon7,FollowPercentageCon8,FollowPercentageIncon8],axis=0), (1, 0, 2)).reshape(-1,1)
FollowPercentage = np.delete(FollowPercentageAll,np.where(np.isnan(FollowPercentageAll))[0])
df_long = pd.DataFrame(np.transpose([ParticipantNumber,Congruency,NumberOfAgents,FollowPercentage]),columns=['ParticipantNumber','Congruency','NumberOfAgents','FollowPercentage'])
# =============================================================================
# ANOVA (1): Follow percentage
import pingouin as pg
anova_follow1 = pg.rm_anova(dv='FollowPercentage', 
                           within=['Congruency', 'NumberOfAgents'], 
                           subject='ParticipantNumber', 
                           data=df_long, 
                           detailed=True)

print(anova_follow1)
# =============================================================================
# ANOVA (2): Follow percentage
import statsmodels.api as sm
from statsmodels.stats.anova import AnovaRM

model = AnovaRM(data=df_long, depvar='FollowPercentage', subject='ParticipantNumber',
                within=['Congruency', 'NumberOfAgents'])
anova_follow2 = model.fit()
print(anova_follow2)
# =============================================================================
# LMM: Follow percentage
import statsmodels.api as sm
from statsmodels.formula.api import mixedlm

model = mixedlm("FollowPercentage ~ Congruency * NumberOfAgents", 
                df_long, 
                groups=df_long["ParticipantNumber"])
result = model.fit()
print(result.summary())