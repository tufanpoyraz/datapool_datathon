import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd
from nltk.corpus import stopwords
from textblob import TextBlob, Word
import string

#nltk.download('stopwords')
#nltk.download('wordnet')


pathTufan="/home/tufan/Desktop/datathon/"

df_product = pd.read_csv(pathTufan+'df_product.csv')


df_product["cleaned"]=df_product["title"]+" "+df_product["categoryname"] #title ile kategori birleştirip yeni sütün

df_product["cleaned"]=df_product["cleaned"].apply(lambda x:str(x).replace("\n", "").translate(str.maketrans("", "", string.punctuation)).translate(
                    str.maketrans("", "", string.digits)).lower()) #ıvırzıvır temizleme



df_product["cleaned"]=df_product["cleaned"].apply(lambda x:str(x).split())
y=[]
cleaned3=[]
for i in df_product["cleaned"]:
    for j in i:
        if len(j)<3 or j in stopwords.words("turkish"): #stopwords ve tek ve 2 harfli keliimeleri temizleme
            continue
        y.append(j)
        for n, i in enumerate(y):
            y[n] = Word(i).lemmatize() #kelime köklerine indirgeme

    cleaned3.append(" ".join(y))
    y=[]
df_product["cleaned"]=cleaned3



df_product.to_csv(pathTufan+'df_product2.csv', index = False, header=True)


