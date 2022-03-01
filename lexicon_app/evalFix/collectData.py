import pandas as pd

data = pd.read_csv("score_logCSV.csv", delimiter=":")
numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
data.select_dtypes(include=numerics)

data.to_csv("new.tsv", sep='\t')