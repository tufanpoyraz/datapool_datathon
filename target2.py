
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

df_target = pd.read_csv(pathTufan+'df_target_train.csv')




target=pd.DataFrame(df_target["userid"].unique(),columns=["userid"])

currentbugroupname=['Ayakkabı & Çanta', 'Branded Tekstil', 'FMCG' ,'Ev' ,'GAS', 'GM' ,'Elektronik',
 'Kozmetik' ,'Aksesuar & Saat & Gözlük' ,'Private Label', 'Mobilya', 'UNKNOWN',
 'Digital Goods']


bigTable=[]
basket_list=[]
for i in target["userid"]:
    for j in currentbugroupname:
                bigTable.append([i,j])


target=pd.DataFrame(bigTable,columns=["userid","currentbugroupname"])
x=[]
print(target)
for i,j in df_target.values:
    if str(j)=="nan":
        j="UNKNOWN"
    for k,l in target.values:
        if i==k and j==l:
            x.append(1)
            break
    x.append(0)



target["y"]=x
target.to_csv(pathTufan+'df_target2.csv', index = False, header=True)