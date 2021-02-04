# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 18:22:42 2021

@author: nishant
"""
import pandas as pd
import numpy as np
import os
import config
from datetime import datetime
from tqdm import tqdm

def process_date(date_time_str):
        
    date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
    
    return date_time_obj

def process_reported(x):
    
    prev = 0
    curr = 0
    ans = 0
    count = 0
    for i in x.split(','):
        try :
            
            obj = datetime.strptime(i, '%Y%m%d')
            if prev == 0:
                    prev = obj
                    curr = obj
            else:
                curr = obj 
                ans += (prev-curr).days
                prev = curr
            count += 1
        except:
            ans += 0
    
    if count == 0:
        return 0
    
    return ans/count*1.0
            
       
    
def feature_date(df):
        
    df['DATE-REPORTED'] = df['DATE-REPORTED'].apply(lambda x :process_date(x))
    df['DISBURSED-DT'] = df['DISBURSED-DT'].apply(lambda x:process_date(x))
    df['REPORTED DATE - HIST'] = df['REPORTED DATE - HIST'].apply(lambda x:process_reported(x))

    df['Difference']= df['DATE-REPORTED'] - df['DISBURSED-DT'] 
    
    new_df = np.array
    flag = False
    new_columns = ['difference','hist']
    for i in tqdm(sorted(df['ID'].value_counts().keys())):
        ans = []
        t = df.loc[df['ID']==i,'Difference']
        ans.extend([np.mean(t).days])
        k = np.array(df.loc[df['ID']==i,'REPORTED DATE - HIST'])
        ans.extend([np.mean(k)])
        
        if flag == False:
            new_df = np.array(ans)
            flag = True
        else :
            new_df=np.vstack((new_df,ans))
        
        
    new_df = pd.DataFrame(new_df,columns=new_columns)
    
    
    return new_df



if __name__ == '__main__':
    df = pd.read_csv(config.TRAIN_BUR_CLEAN)
    
    new_df = feature_date(df)
    
    new_df.to_csv(os.path.join(config.path,'date_feature.csv'),index=False)