# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 13:19:20 2021

@author: nishant
"""
import pandas as pd
from sklearn import model_selection
import os
import config

if __name__ == '__main__':
    
    df=pd.read_csv(config.train)
    
    df.loc[:,'Kfold'] = -1
    
    df = df.sample(frac=1).reset_index(drop=True)
    
    targets = df['Top-up Month'].values
    
    kf = model_selection.StratifiedKFold(n_splits=5)
    
    for f,(t_,v_) in enumerate(kf.split(X=df,y=targets)):
        print(len(t_),len(v_))
        
        df.loc[v_,'Kfold'] = f
        
        
    df.to_csv(os.path.join(config.path,'strat.csv'),index=False)
