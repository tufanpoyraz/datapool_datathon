
import pandas as pd


pathTufan="/home/tufan/Desktop/datathon/"

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


target=pd.DataFrame(bigTable,columns=["userid","currentbugroupname","y"])
x=[]
for i in df_target["userid"]:
    category=df_target.loc[df_target['userid'] == i]["currentbugroupname"].values
    if len(category)>0:
        for j in category:

            target.loc[(target['userid'] == i) & (target['currentbugroupname'] == j),"y"]=1


target.to_csv(pathTufan+'df_target2.csv', index = False, header=True)