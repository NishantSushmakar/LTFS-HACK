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

#Train
#encoder = LabelEncoder()
#encoder.fit(X)
#numpy.save('classes.npy', encoder.classes_)


#Test
#encoder = LabelEncoder()
#encoder.classes_ = numpy.load('classes.npy')


def preprocess_bur(df):
    
    
    
    
    column_to_handle = ['DATE-REPORTED','DISBURSED-DT','CREDIT-LIMIT/SANC AMT','CLOSE-DT','LAST-PAYMENT-DATE','INSTALLMENT-AMT',
                        'INSTALLMENT-FREQUENCY','OVERDUE-AMT','WRITE-OFF-AMT','ASSET_CLASS','REPORTED DATE - HIST'
                        ,'DPD - HIST','CUR BAL - HIST','AMT OVERDUE - HIST','AMT PAID - HIST','TENURE']
    
    for col in column_to_handle:
        df[df[col].isna()==True] = -1
    
    # LabelEncoders
    
    columns_to_le = ['SELF-INDICATOR','MATCH-TYPE','ACCT-TYPE','CONTRIBUTOR-TYPE','OWNERSHIP-IND','ACCOUNT-STATUS']
    
    
    for col in columns_to_le: 
        le = LabelEncoder()
        df[df[col]!=-1][col]= le.fit_transform(df[df[col]!=-1][col])
        print(col)
        np.save(os.path.join(config.path,f'{col}.npy'),le.classes_)
    
    
    return df






if __name__ == '__main__':
    
   df = pd.read_csv(config.TRAIN_BUR)
   df = preprocess_bur(df)
   df.to_csv(os.path.join(config.path,'bureau_clean.csv'),index=False)