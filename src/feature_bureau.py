# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 11:52:24 2021

@author: nishant
"""
import pandas as pd
import numpy as np
import config
import os
from tqdm import tqdm
import help_feature

def featurise(df):
    
    
    
    df = help_feature.process(df)
    
    new_columns = ['Mode_Self_indicator','Mode_Match_Type','Mode_Acct_Type','Mode_Contributor_type','Mode_ownership','Mode_account_status',
                   'Mode_installment_freq','Median_Disbursed_Amt','Mean_Disbursed_Amt','Median_Intsallment_amt','Mean_Intsallment_amt',
                   'Median_curr_bal','Mean_curr_bal','Median_overdue_amt','Mean_overdue_amt','Median_curr_bal_hist'
                   ,'Mean_curr_bal_hist','Median_amt_due_hist','Mean_amt_due_hist','Median_amt_paid_hist','Mode_amt_paid_hist',
                   'Median_tenure','Mean_Tenure'
                   ]
    new_df = np.array
    
    flag = False
    
    for i in tqdm(sorted(df['ID'].value_counts().keys())):
        
        ans = []
        mode_col = ['SELF-INDICATOR','MATCH-TYPE','ACCT-TYPE','CONTRIBUTOR-TYPE','OWNERSHIP-IND','ACCOUNT-STATUS','INSTALLMENT-FREQUENCY']
        
        for col in mode_col :
            ans.extend([df.loc[df['ID']==i,col].value_counts().keys()[0]])
        
        mean_and_median_col = ['DISBURSED-AMT/HIGH CREDIT','INSTALLMENT-AMT','CURRENT-BAL','OVERDUE-AMT','CUR BAL - HIST',
                               'AMT OVERDUE - HIST','AMT PAID - HIST','TENURE']
        
        for col in mean_and_median_col :
            
             k = np.array(df.loc[df['ID']==i,col])
             ans.extend([np.median(k)])
             ans.extend([np.mean(k)])
             
        if flag == False:
            new_df = np.array(ans)
            flag = True
        else :
            new_df=np.vstack((new_df,ans))
        
        
        
    new_df = pd.DataFrame(new_df,columns=new_columns)


    return new_df 




if __name__ == '__main__':
    
    df =pd.read_csv(config.TRAIN_BUR_CLEAN)
    
    new_df = featurise(df)
    
    new_df.to_csv(os.path.join(config.path,'feature_bur.csv'),index=False)
    