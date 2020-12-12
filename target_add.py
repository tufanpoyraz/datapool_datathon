
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
                bigTable.append([i,j,0])

"""    if str(j)=="nan":
        j="UNKNOWN"
        """

target=pd.DataFrame(bigTable,columns=["userid","currentbugroupname","y"])
x=[]
for i in df_target["userid"]:
    category=df_target.loc[df_target['userid'] == i]["currentbugroupname"].values
    if len(category)>0:
        for j in category:

            target.loc[(target['userid'] == i) & (target['currentbugroupname'] == j),"y"]=1


"""with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(target)"""


target.to_csv(pathTufan+'df_target2.csv', index = False, header=True)