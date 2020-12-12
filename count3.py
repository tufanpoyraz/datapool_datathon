import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd
from nltk.corpus import stopwords
from textblob import TextBlob, Word
import string

#nltk.download('stopwords')
#nltk.download('wordnet')


pathTufan="/home/tufan/Desktop/datathon/"
#pathBurak=?


df_basket = pd.read_csv(pathTufan+'df_basket2.csv')
"""
df_search = pd.read_csv(pathTufan+'df_search_term.csv')
df_visit = pd.read_csv(pathTufan+'df_visit.csv')
"""
df_demo = pd.read_csv(pathTufan+'df_demo.csv')
df_fav = pd.read_csv(pathTufan+'df_fav2.csv')
df_trx = pd.read_csv(pathTufan+'df_trx2.csv')

df_product = pd.read_csv(pathTufan+'df_product.csv')
df_target = pd.read_csv(pathTufan+'df_target_train.csv')
df_sample = pd.read_csv(pathTufan+'sample_submission.csv')
df_search = pd.read_csv(pathTufan+'df_search3.csv')







#df_sample["userid"]=df_sample["userid_currentbugroupname"].apply(lambda x:x.split("_")[0])
#frames = [df_target["userid"], df_sample["userid"]]
#database["userid"] = pd.concat(frames)

database=pd.DataFrame(df_target["userid"].unique(),columns=["userid"])

print(database)

currentbugroupname=['Ayakkabı & Çanta', 'Branded Tekstil', 'FMCG' ,'Ev' ,'GAS', 'GM' ,'Elektronik',
 'Kozmetik' ,'Aksesuar & Saat & Gözlük' ,'Private Label', 'Mobilya', 'UNKNOWN',
 'Digital Goods']


bigTable=[]
basket_list=[]
for i in database["userid"]:
    userinfo=df_demo.loc[df_demo['userid'] == i].values
    df_basket_userid=df_basket.loc[df_basket['userid'] == i]
    df_fav_userid=df_fav.loc[df_fav['userid'] == i]
    df_trx_userid=df_trx.loc[df_trx['userid'] == i]
    df_search_userid=df_search.loc[df_search['userid'] == i]

    for j in currentbugroupname:

        if len(df_basket_userid)>0:
            df_basket_count = df_basket_userid.loc[df_basket_userid['currentbugroupname'] == j]["addtobasket_count"].sum()
        else:
            df_basket_count=0

        if len(df_fav_userid)>0:
            fav_count = df_fav_userid.loc[df_fav_userid['currentbugroupname'] == j]["fav_count"].sum()
        else:
            fav_count=0

        if len(df_trx_userid)>0:
            quantity = df_trx_userid.loc[df_trx_userid['currentbugroupname'] == j]["quantity"].sum()
            price = df_trx_userid.loc[df_trx_userid['currentbugroupname'] == j]["price"].sum()

        else:
            quantity=0
            price=0

        if len(df_search_userid)>0:
            search_count = df_search_userid.loc[df_search_userid['CGN'] == j]["CGN"].count()
        else:
            search_count=0



        if len(userinfo)>0: #user demonun içinde varsa bilgilerini al

            if 7<userinfo[0][2]<90: #yaşı tutuyorsa yaşı al
                bigTable.append([i,j,userinfo[0][1],userinfo[0][2],userinfo[0][3],df_basket_count,fav_count,quantity,price,search_count])

            else:
                bigTable.append([i, j, userinfo[0][1], None, userinfo[0][3],df_basket_count,fav_count,quantity,price,search_count])

        else:
            bigTable.append([i,j,None,None,None,df_basket_count,fav_count,quantity,price,search_count])

database=pd.DataFrame(bigTable,columns=["userid","currentbugroupname","gender","age","tenure","addtobasket_count","fav_count","quantity","price","search_count"])


database.to_csv(pathTufan+'database_target.csv', index = False, header=True)





with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(database)