# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 13:46:33 2021

@author: nishant
"""

import pandas as pd
import config
import os
   
df = pd.read_csv(config.TRAIN_DATA)
df = df.sample(frac=1).reset_index(drop=True)

y_train = df['Top-up Month']
y_train = y_train.apply(lambda x:config.target_dict[x])
x_train = df.drop(columns=['Top-up Month'])

y_train.to_csv(os.path.join(config.path,'y_train.csv'),index=False)
x_train.to_csv(os.path.join(config.path,'x_train.csv'),index=False) 