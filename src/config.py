# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 13:47:11 2021

@author: nishant
"""
TRAIN_DATA = 'C:/Users/nishant/LTFS Hack/input/Train/train_Data.csv'
X_TRAIN_DATA = 'C:/Users/nishant/LTFS Hack/input/Train/x_train.csv'
Y_TRAIN_DATA = 'C:/Users/nishant/LTFS Hack/input/Train/y_train.csv'
TRAIN_BUR = 'C:/Users/nishant/LTFS Hack/input/Train/train_bureau.csv'
TEST_DATA = 'C:/Users/nishant/LTFS Hack/input/Test/test_da.csv'
TEST_BUR = 'C:/Users/nishant/LTFS Hack/input/Test/test_bur.csv'
path = 'C:/Users/nishant/LTFS Hack/input/Train/'
path_test = 'C:/Users/nishant/LTFS Hack/input/Test/'
target_dict = { 'No Top-up Service' : 0 ,
        ' > 48 Months': 1,
        '36-48 Months':2,
        '24-30 Months' : 3,
        '30-36 Months' : 4,
        '18-24 Months': 5,
        '12-18 Months': 6 
        }

acct_dict = {
    'Auto Loan (Personal)':1,
    'Auto Overdraft':2,
    'Two-Wheeler Loan':3,
    'Commercial Vehicle Loan':4,
    'Commercial Equipment Loan':5,
    'Housing Loan':6,
    'Property Loan':7,
    'Loan Against Shares / Securities':8,
    'Gold Loan':9,
    'Education Loan':10,
    'Leasing':11,
    'Personal Loan':12,
    'Consumer Loan':13,
    'Loan to Professional':14,
    'Credit Card':15,
    'Charge Card':16,
    'Fleet Card':17,
    'Loan against Card':18,
    'Overdraft':19,
    'Loan Against Bank Deposits':20,
    'OD on Savings Account':21,
    'Non-Funded Credit Facility':22,
    'Business Loan General':23,
    'Business Loan Priority Sector Small Business':24,
    'Business Loan Priority Sector Agriculture':25,
    'Business Loan Priority Sector Others':26,
    'Business Non-Funded Credit Facility General':27,
    'Business Non-Funded Credit Facility-Priority Sector- Small Business':28,
    'Business Non-Funded Credit Facility-Priority Sector-Agriculture':29,
    'Business Non-Funded Credit Facility-Priority Sector-Others':30,
    'Business Loan Against Bank Deposits':31,
    'Other':32,
    'Commercial Vehicle Loan':33,
    'Telco Wireless':34,
    'Telco Broadband':35,
    'Telco Landline':36,
    'Microfinance Business Loan':37,
    'Microfinance Personal Loan':38,
    'Microfinance Housing Loan':39,
    'Microfinance Others':40,
    'Used Car Loan':41,
    'Construction Equipment Loan':42,
    'Used Tractor Loan':43,
    'Staff Loan':44,
    'Secured Credit Card':45,
    'Corporate Credit Card':46,
    'Kisan Credit Card':47
}