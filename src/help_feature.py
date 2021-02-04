# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 13:54:56 2021

@author: nishant
"""
import pandas as pd
import numpy as np
import config
import locale
locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' )          

def process_list(string_list):
    ans = 0
    count = 0
    for i in string_list.split(','):
        try:
           ans += int(i)
           count += 1
        except:
           ans += 0
    
    if count==0:
       return 0
   
    
    return ans/(count)*1.0

def process(df):
    
    df['INSTALLMENT-AMT'] = df['INSTALLMENT-AMT'].apply(lambda x : x if x.find('/')==-1 else x[:x.find('/')])
    df.loc[df['INSTALLMENT-AMT']=='Unknown','INSTALLMENT-AMT'] = '0' 
    
    
    columns_with_str = ['DISBURSED-AMT/HIGH CREDIT','INSTALLMENT-AMT','CURRENT-BAL','OVERDUE-AMT'] 
       
    for col in columns_with_str:
        df[col] = df[col].apply(lambda x:locale.atoi(x))
    
    col_with_hist = ['CUR BAL - HIST','AMT OVERDUE - HIST','AMT PAID - HIST' ]
    
    for col in col_with_hist:
        df[col] = df[col].apply(lambda x:process_list(x))
    
    



    return df




