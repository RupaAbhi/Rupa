import pandas as pd
data ={'Country':['Beligim', 'India', 'Brazil'],
'Capital':['Brussels', 'New Delhi', 'Brasilia'],
'Population': [11190846,13033171035,207847528]}
df=pd.DataFrame(data,columns=['Country', 'Capital','Population'])
print (df)
