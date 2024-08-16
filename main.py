import pandas as pd

nintendoGames_df = pd.read_csv('Data/NintendoGames.csv') #Loads Dataframe

nintendoGames_df.dropna(inplace=True)
nintendoGames_df = nintendoGames_df[['title','meta_score','user_score','platform','genres']]
nintendoGames_df.drop_duplicates(inplace=True)
nintendoGames_df = nintendoGames_df[nintendoGames_df.platform != "iOS"]
nintendoGames_df = nintendoGames_df.query(f'not title.str.contains("Wave")', engine='python')
nintendoGames_df = nintendoGames_df.query(f'not title.str.contains("DLC")', engine='python')
nintendoGames_df = nintendoGames_df.query(f'not title.str.contains("Edition")', engine='python')
print(nintendoGames_df)