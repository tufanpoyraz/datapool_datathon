
import pandas as pd


pathTufan="/home/tufan/Desktop/datathon/"
#pathBurak=?

df_target = pd.read_csv(pathTufan+'database_target2.csv')[:1000]



for i in df_target.index:

    if df_target["price"][i]==0 and df_target["quantity"][i]==0 and df_target["fav_count"][i]==0 and df_target["addtobasket_count"][i]==0 and df_target["search_count"][i]==0:
        df_target.drop(index=i,inplace=True)
        print(i)


#df_target.to_csv(pathTufan+'database_target5.csv', index = False, header=True)

with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(df_target.describe())