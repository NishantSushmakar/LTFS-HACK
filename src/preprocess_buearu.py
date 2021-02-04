# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 13:46:10 2021

@author: nishant
"""
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import config
import os
from tqdm import tqdm
from sklearn.impute import SimpleImputer
#Train
#encoder = LabelEncoder()
#encoder.fit(X)
#numpy.save('classes.npy', encoder.classes_)


#Test
#encoder = LabelEncoder()
#encoder.classes_ = numpy.load('classes.npy')


def preprocess_bur(df):
    
    print('Process Tenure')
    ans = []
    for i in tqdm(sorted(df['ID'].value_counts().keys())):
        
        imp_freq = SimpleImputer(missing_values=np.nan, strategy='median')
        t = list(imp_freq.fit_transform(np.array(df.loc[df['ID']==i,'TENURE']).reshape(-1,1)).reshape(-1))
        if len(t)>0 :
            ans.extend(t)
        else :
            t = [np.NaN]*len(df[df['ID']==i]['TENURE'])
            ans.extend(t)
    tenure_df = pd.DataFrame(ans,columns=['TENURE'])
    df = df.drop(columns=['TENURE'])
    df = pd.concat([df,tenure_df],axis=1)    
    
   
    
    print('Most Frequent')
    columns_to_handle = ['DATE-REPORTED','DISBURSED-DT','CURRENT-BAL','OVERDUE-AMT','WRITE-OFF-AMT',
                         'ASSET_CLASS','REPORTED DATE - HIST','DPD - HIST','CUR BAL - HIST','AMT OVERDUE - HIST'
                         ,'AMT PAID - HIST','TENURE']
    
    for col in columns_to_handle:
        k = df[col].value_counts().keys()[0]
        df.loc[df[col].isna(),col] = k
    
    
    print('Unknown')
    column_for_unknowns = ['CLOSE-DT','LAST-PAYMENT-DATE','CREDIT-LIMIT/SANC AMT','INSTALLMENT-AMT','INSTALLMENT-FREQUENCY'] 
   
    for col in column_for_unknowns:
        df.loc[df[col].isna(),col] = 'Unknown'
    
    
    df.loc[(df['ASSET_CLASS']=='1')|(df['ASSET_CLASS']=='01')|(df['ASSET_CLASS']=='2'),'ASSET_CLASS']='other'
    
    
    # LabelEncoders
    print("Label Encoder")
    
    columns_to_le = ['SELF-INDICATOR','MATCH-TYPE','ACCT-TYPE','CONTRIBUTOR-TYPE','OWNERSHIP-IND',
                     'ACCOUNT-STATUS','INSTALLMENT-FREQUENCY','ASSET_CLASS']
    
    
    for col in columns_to_le: 
        try:
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col])
            print(col)
            np.save(os.path.join(config.path,f'{col}.npy'),le.classes_)
        except:
            print('Error')
            print(df[col].value_counts())
            
            
            
            
    
    
    return df






if __name__ == '__main__':
    
   df = pd.read_csv(config.TRAIN_BUR)
   df = preprocess_bur(df)
   df.to_csv(os.path.join(config.path,'bureau_clean.csv'),index=False)