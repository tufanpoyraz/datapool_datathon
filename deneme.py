import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd
from nltk.corpus import stopwords
from textblob import TextBlob, Word
import string


pathTufan="/home/tufan/Desktop/datathon/"
#pathBurak=?


"""df_basket = pd.read_csv(pathTufan+'df_basket.csv')
df_demo = pd.read_csv(pathTufan+'df_demo.csv')
df_fav = pd.read_csv(pathTufan+'df_fav.csv')
df_search = pd.read_csv(pathTufan+'df_search_term.csv')
df_target = pd.read_csv(pathTufan+'df_target_train.csv')
df_trx = pd.read_csv(pathTufan+'df_trx.csv')
df_visit = pd.read_csv(pathTufan+'df_visit.csv')"""
df_product = pd.read_csv(pathTufan+'df_product.csv')

df_product=df_product[:50] # denemek için dataframe in ilk kısmını alıyor

df_product["cleaned"]=df_product["title"]+" "+df_product["categoryname"] #title ile kategori birleştirip yeni sütün

df_product["cleaned2"]=df_product["cleaned"].apply(lambda x:str(x).replace("\n", "").translate(str.maketrans("", "", string.punctuation)).translate(
                    str.maketrans("", "", string.digits)).lower()) #ıvırzıvır temizleme



df_product["cleaned2"]=df_product["cleaned2"].apply(lambda x:str(x).split())
y=[]
cleaned3=[]
for i in df_product["cleaned2"]:
    for j in i:
        if len(j)<3 or j in stopwords.words("turkish"): #stopwords ve tek ve 2 harfli keliimeleri temizleme
            continue
        y.append(j)
        for n, i in enumerate(y):
            y[n] = Word(i).lemmatize() #kelime köklerine indirgeme
    cleaned3.append(y)
    y=[]
df_product["cleaned3"]=cleaned3

print("11111",df_product["cleaned"])
print("22222",df_product["cleaned2"])
print("333333",df_product["cleaned3"])

"""with pd.option_context('display.max_rows', 20, 'display.max_columns', None):
    print(df_product)"""