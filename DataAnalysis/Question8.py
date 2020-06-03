import pandas as pd
import matplotlib.pyplot as plt


DataDosyasi=pd.read_csv('C:/Users/gorke/anaconda3/US_Accidents_Dec19.csv')
DataDosyasi.head()

df_bool = DataDosyasi.groupby(['Turning_Loop','Severity'])['ID'].count()
df_bool = df_bool.unstack('Turning_Loop')

plt.tight_layout()
df_bool.plot(kind='pie',subplots=True,autopct='%.1f%%',pctdistance=1.4,figsize=(10,10),title = 'Turning Loop')
