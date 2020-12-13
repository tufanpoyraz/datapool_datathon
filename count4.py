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
df_ans = pd.read_csv(pathTufan+'X_ans.csv')
df_ans["0"]=df_ans["0"].astype(str)
df_ans["userid_currentbugroupname"]=df_ans["0"]+"_"+df_ans["1"]







df_sample["userid"]=df_sample["userid_currentbugroupname"].apply(lambda x:round(int(x.split("_")[0])))
df_sample["currentbugroupname"]=df_sample["userid_currentbugroupname"].apply(lambda x:x.split("_")[1])
#frames = [df_target["userid"], df_sample["userid"]]
#database["userid"] = pd.concat(frames)

print(df_sample.head(20))
database=df_sample
database.drop(columns="target",inplace=True)
print(database.head(20))

currentbugroupname=['Ayakkabı & Çanta', 'Branded Tekstil', 'FMCG' ,'Ev' ,'GAS', 'GM' ,'Elektronik',
 'Kozmetik' ,'Aksesuar & Saat & Gözlük' ,'Private Label', 'Mobilya',
 'Digital Goods']


bigTable=[]
basket_list=[]
i=0
while  i< len(database["userid"].values):
    userinfo=df_demo.loc[df_demo['userid'] == database["userid"][i]].values
    df_basket_userid=df_basket.loc[df_basket['userid'] == database["userid"][i]]
    df_fav_userid=df_fav.loc[df_fav['userid'] == database["userid"][i]]
    df_trx_userid=df_trx.loc[df_trx['userid'] == database["userid"][i]]
    df_search_userid=df_search.loc[df_search['userid'] == database["userid"][i]]



    if len(df_basket_userid)>0:
        df_basket_count = df_basket_userid.loc[df_basket_userid['currentbugroupname'] == database["currentbugroupname"][i]]["addtobasket_count"].sum()
    else:
        df_basket_count=0

    if len(df_fav_userid)>0:
        fav_count = df_fav_userid.loc[df_fav_userid['currentbugroupname'] == database["currentbugroupname"][i]]["fav_count"].sum()
    else:
        fav_count=0

    if len(df_trx_userid)>0:
        quantity = df_trx_userid.loc[df_trx_userid['currentbugroupname'] == database["currentbugroupname"][i]]["quantity"].sum()
        price = df_trx_userid.loc[df_trx_userid['currentbugroupname'] == database["currentbugroupname"][i]]["price"].sum()

    else:
        quantity=0
        price=0

    if len(df_search_userid)>0:
        search_count = df_search_userid.loc[df_search_userid['CGN'] == database["currentbugroupname"][i]]["CGN"].count()
    else:
        search_count=0



    if len(userinfo)>0: #user demonun içinde varsa bilgilerini al

        if 7<userinfo[0][2]<90: #yaşı tutuyorsa yaşı al
            bigTable.append([database["userid"][i],database["currentbugroupname"][i],userinfo[0][1],userinfo[0][2],userinfo[0][3],df_basket_count,fav_count,quantity,price,search_count])

        else:
            bigTable.append([database["userid"][i], database["currentbugroupname"][i], userinfo[0][1], None, userinfo[0][3],df_basket_count,fav_count,quantity,price,search_count])

    else:
        bigTable.append([database["userid"][i],database["currentbugroupname"][i],None,None,None,df_basket_count,fav_count,quantity,price,search_count])
    i+=1
database=pd.DataFrame(bigTable,columns=["userid","currentbugroupname","gender","age","tenure","addtobasket_count","fav_count","quantity","price","search_count"])


database.to_csv(pathTufan+'database_sample3.csv', index = False, header=True)





"""with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(database)"""