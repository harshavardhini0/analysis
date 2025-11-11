import pandas as pd
import numpy as np
df = pd.read_csv("C:\\Users\\vardh\\STUDENTS_DATA.CSV")
#EDA
print(df)
print("=== INFO ===")
print(df.info())
print("\n=== DESCRIBE ===")
print(df.describe())
print("=== TOP ROWS ===")
print(df.head())
print("=== BOTTOM ROWS ===")
print(df.tail())
print("=== SHAPE ===")
print(df.shape)

#sorting(by math score descending)
print("\n=== SORTED DATA ===")
sorted_df = df.sort_values(by='MATH_SCORE', ascending=False)
print(sorted_df)

#creating new column using existing columns
print("\n=== DATA WITH NEW COLUMN ===")
df['Average_Score'] = np.round((df['MATH_SCORE']+ df['SCIENCE']+df['ENGLISH'])/3,2)
print(df)

#grouping by operation
print("\n=== GROUPED BY GENDER ===")
grouped_df = df.groupby('GENDER')[['MATH_SCORE','SCIENCE','ENGLISH','Average_Score']].mean()
print(grouped_df)

#new dataframe using selected features
new_df  = df[['NAME','GENDER','Average_Score']]
print("\n=== NEW DATAFRAME ===")
print(new_df)

