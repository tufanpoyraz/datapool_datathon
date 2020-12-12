
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
#df_visit = pd.read_csv(pathTufan+'df_visit.csv')

df_target = pd.read_csv(pathTufan+'df_target2.csv')
database_target = pd.read_csv(pathTufan+'database_target.csv')

database_target["target"]=df_target["y"]

database_target.to_csv(pathTufan+'database_target2.csv', index = False, header=True)