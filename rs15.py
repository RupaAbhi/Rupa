import pandas as pd
data = pd.read_csv(r'c:\pythoncode\gaints.csv')
df = pd.DataFrame(data, columns=['CEO','established'])
print(df)