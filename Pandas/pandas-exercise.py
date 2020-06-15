import pandas as pd


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns',None)
pd.set_option('display.width',None)

pokemon_df=pd.read_csv('Pokemon_Gen_1-8.csv')
pokemon_generation = pokemon_df.loc[0:20,['#','Name','Generation']]
print(pokemon_generation)

#print(pokemon_df[['#','Name','Generation']])
