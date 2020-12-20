
import pandas as pd



pathTufan="/home/tufan/Desktop/datathon/"

df_trx = pd.read_csv(pathTufan+'df_trx.csv')

df_product = pd.read_csv(pathTufan+'df_product.csv')

x=[]
for i in df_trx["contentid"]:
    category=df_product.loc[df_product['contentid'] == i]["currentbugroupname"].values

    if len(category) != 0:
        x.append(category[0])
    else:
        x.append(None)
df_trx["currentbugroupname"]=x

df_trx.to_csv(pathTufan+'df_trx2.csv', index = False, header=True)
