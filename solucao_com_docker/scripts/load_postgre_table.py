#### SETUP
import pandas as pd
from glob import glob
from tqdm import tqdm
import utils
from sqlalchemy import create_engine


csv_path = 'C:\\Users\\Windows\\Documents\\BaseDosDados\\Data\\csv'

files = glob(csv_path+'/*csv')

df_ans = pd.read_csv(files[0])

for file in files[1:]:
    df = pd.read_csv(file)
    if (df.columns == df_ans.columns).all():
        df_ans = pd.concat([df_ans, df], ignore_index=True)
        print(file.split('\\')[-1], ' has been appended')
    else:
        print(file.split('\\')[-1], ' has different columns')

conn_string = 'postgresql://postgres:kaldorfacts@localhost:5432/basedosdados_dev'

conn = create_engine(conn_string)


df_ans.to_sql('ans_operadoras', conn, if_exists='replace', index=False)