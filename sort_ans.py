
import pandas as pd



pathTufan="/home/tufan/Desktop/datathon/"
#pathBurak=?

df_ans = pd.read_csv(pathTufan+'X_ans.csv')


df_sample = pd.read_csv(pathTufan+'sample_submission.csv')


df_ans["0"]=df_ans["0"].astype(str)
df_ans["userid_currentbugroupname"]=df_ans["0"]+"_"+df_ans["1"]
for i in df_ans["userid_currentbugroupname"]:

    target=df_ans.loc[(df_ans['userid_currentbugroupname'] == i) ]["target"].values[0]
    df_sample.loc[(df_sample['userid_currentbugroupname'] == i),"target"]=target



print(df_sample)

df_sample.to_csv(pathTufan+'sample_submission2.csv', index = False, header=True)

