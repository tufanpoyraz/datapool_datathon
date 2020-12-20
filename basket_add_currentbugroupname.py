

import pandas as pd



pathTufan="/home/tufan/Desktop/datathon/"

df_basket = pd.read_csv(pathTufan+'df_basket.csv')
df_product = pd.read_csv(pathTufan+'df_product.csv')


#df_basket=df_basket[:1000] # denemek için dataframe in ilk kısmını alıyor



x=[]
for i in df_basket["contentid"]:
    category=df_product.loc[df_product['contentid'] == i]["currentbugroupname"].values
    if len(category) != 0:
        x.append(category[0])
    else:
        df_basket.drop(df_basket.loc[df_basket['contentid'] == i].index,inplace=True)
df_basket["currentbugroupname"]=x

df_basket.to_csv(pathTufan+'df_basket2.csv', index = False, header=True)
