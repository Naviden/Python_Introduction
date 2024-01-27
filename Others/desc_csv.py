import pandas as pd
import argparse
from pathlib import Path



parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', type= str)
args = parser.parse_args()


df = pd.read_csv(args.file)

print(f'File : {args.file.split("/")[-1]}')
print('-' * 40)
print('Columns:')
print('=' * 10)
for col in df.columns:
    print(col)
print('\n File Description:')
print(df.describe().apply(lambda x : round(x, 1)))