import pandas as pd

def ds_detail():
    df = pd.read_csv('detail.csv', parse_dates = ["Absolute Time"], index_col = "Absolute Time")
    df = df.resample('T').mean()
    df.to_csv('detailDownsampled.csv')


def ds_detail_vol():
    df = pd.read_csv('detailVol.csv', parse_dates = ["Realtime"], index_col = "Realtime")
    df = df.resample('T').mean()
    df.to_csv('detailVolDownsampled.csv')


def ds_detail_temp():
    df = pd.read_csv('detailTemp.csv', parse_dates = ["Realtime"], index_col = "Realtime")
    df = df.resample('T').mean()
    df.to_csv('detailTempDownsampled.csv')

ds_detail()
ds_detail_vol()
ds_detail_temp()