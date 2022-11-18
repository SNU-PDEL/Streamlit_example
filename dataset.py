import pandas as pd
station_df = pd.read_csv('C:/Users/PDEL/Desktop/NCPMS_ML/NCPMS_ML/data/User/Station-Info-all-129stns.csv').loc[27:]     #### 북한 제외
station_df = station_df.reset_index(drop=True)

def get_EYear(stnID):
    year, mon = pd.read_csv('C:/Users/PDEL/Desktop/NCPMS_ML/NCPMS_ML/data/User/'+stnID + '.csv').iloc[-1,0:2]           # 관측소 ID를 이용, 가장 마지막 관측 년,월 출력, 월이 10월 미만일시 년 -1
    if mon >= 10:
        return year
    else:
        return year - 1

def get_SYear(stnID):
    year, mon = pd.read_csv('C:/Users/PDEL/Desktop/NCPMS_ML/NCPMS_ML/data/User/' + stnID + '.csv').iloc[0,0:2]
    if mon <= 3:
        return year
    else:
        return year + 1
                                                                                                                         #### 파종과 추수의 시간
station_df['EYear'] = station_df['ID'].apply(lambda x: get_EYear(x))
station_df['SYear'] = station_df['ID'].apply(lambda x: get_SYear(x))


print('a')





