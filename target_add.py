

import pandas as pd


pathTufan="/home/tufan/Desktop/datathon/"

df_target = pd.read_csv(pathTufan+'df_target2.csv')
database_target = pd.read_csv(pathTufan+'database_target.csv')

database_target["target"]=df_target["y"]

database_target.to_csv(pathTufan+'database_target2.csv', index = False, header=True)