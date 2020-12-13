
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
df_trx = pd.read_csv(pathTufan+'df_trx.csv')
"""
#df_demo = pd.read_csv(pathTufan+'df_demo.csv')
#df_fav = pd.read_csv(pathTufan+'df_fav.csv')
df_visit = pd.read_csv(pathTufan+'df_visit.csv')

df_product = pd.read_csv(pathTufan+'df_product.csv')
#df_target = pd.read_csv(pathTufan+'df_target_train.csv')
#df_sample = pd.read_csv(pathTufan+'sample_submission.csv')


df_visit=df_visit.sort_values('contentid')
df_product=df_product.sort_values('contentid')

print(df_visit)
#df_basket=df_basket[:1000] # denemek için dataframe in ilk kısmını alıyor

"""
with pd.option_context('display.max_rows', 100, 'display.max_columns', None):
    print(df_visit)"""
df_visit.to_csv(pathTufan+'df_visit2.csv', index = False, header=True)
