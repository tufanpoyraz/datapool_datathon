
import pandas as pd



pathTufan="/home/tufan/Desktop/datathon/"

df_fav = pd.read_csv(pathTufan+'df_fav.csv')

df_product = pd.read_csv(pathTufan+'df_product.csv')

x=[]
for i in df_fav["contentid"]:
    category=df_product.loc[df_product['contentid'] == i]["currentbugroupname"].values

    if len(category) != 0:
        x.append(category[0])
    else:
        df_fav.drop(df_fav.loc[df_fav['contentid'] == i].index,inplace=True)
df_fav["currentbugroupname"]=x

df_fav.to_csv(pathTufan+'df_fav2.csv', index = False, header=True)
