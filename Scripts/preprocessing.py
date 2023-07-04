from dependencies import *

def date_modifier(df):

    # -------- Core Logic ---------- #

    # only_date = df['Local time'].split(' ')[0]
    # print(f"only date: {only_date}")
    # df['Local time'] = only_date

    # ------- Converting to numpy array alternative ------- # 

    # arr = df.to_numpy()
    # for i in range(len(arr)):
    #     arr[i][0] = arr[i][0].split(' ')[0]
    # df = pd.DataFrame(arr)


    for i in range(len(df)):
        df['Local time'][i] = df['Local time'][i].split(' ')[0]
        # print(f"only date: {only_date}")

    return df

def drop_NAVol(df):

    df=df[df['volume']!=0]
    df.reset_index(drop=True, inplace=True)
    df.isna().sum()
    df.tail()

    return df


