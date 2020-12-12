
import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd
from nltk.corpus import stopwords
from textblob import TextBlob, Word
import string



pathTufan="/home/tufan/Desktop/datathon/"
#pathBurak=?

#df_basket = pd.read_csv(pathTufan+'df_basket.csv')
"""
df_search = pd.read_csv(pathTufan+'df_search_term.csv')
"""
#df_demo = pd.read_csv(pathTufan+'df_demo.csv')
#df_fav = pd.read_csv(pathTufan+'df_fav.csv')
#df_visit = pd.read_csv(pathTufan+'df_visit.csv')
df_trx = pd.read_csv(pathTufan+'df_trx.csv')

df_product = pd.read_csv(pathTufan+'df_product.csv')
#df_target = pd.read_csv(pathTufan+'df_target_train.csv')
#df_sample = pd.read_csv(pathTufan+'sample_submission.csv')


#df_basket=df_basket[:1000] # denemek için dataframe in ilk kısmını alıyor



x=[]
for i in df_trx["contentid"]:
    category=df_product.loc[df_product['contentid'] == i]["currentbugroupname"].values
    #print(i,category)

    if len(category) != 0:
        x.append(category[0])
    else:
        x.append(None)
df_trx["currentbugroupname"]=x

df_trx.to_csv(pathTufan+'df_trx2.csv', index = False, header=True)
