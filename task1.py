import pandas as pd
import re
import os


def task1():

    path = os.path.abspath('')
    files= os.listdir(path) #list all the file in the directory

    #individual dataframe to store data on iteration
    detail = pd.DataFrame()
    detailVol = pd.DataFrame()
    detailTemp = pd.DataFrame()


    for file in files:
        
        if file.endswith('.xlsx'):
            xl = pd.ExcelFile(file)
            xl.sheet_names
            for sheet in xl.sheet_names:
                if re.match('^Detail_67_', sheet):
                    df = xl.parse(sheet_name = sheet)
                    detail = detail.append(df, ignore_index=True)
                if re.match('^DetailVol_67_', sheet):
                    df = xl.parse(sheet_name = sheet)
                    detailVol = detailVol.append(df, ignore_index=True)
                if re.match('^DetailTemp_67_', sheet):
                    df = xl.parse(sheet_name = sheet)
                    detailTemp = detailTemp.append(df, ignore_index=True)

    #convert dataframe to csv files
    detail.to_csv('detail.csv')
    detailVol.to_csv('detailVol.csv')
    detailTemp.to_csv('detailTemp.csv')
                
task1()