import pandas as pd

nintendoGames_df = pd.read_csv('Data/NintendoGames.csv') #Loads Dataframe
nintendoGames_df.dropna(inplace=True)
nintendoGames_df = nintendoGames_df[['title','meta_score','user_score','platform','genres']]
nintendoGames_df.drop_duplicates(inplace=True)
nintendoGames_df = nintendoGames_df[nintendoGames_df.platform != "iOS"]
nintendoGames_df = nintendoGames_df.query(f'not title.str.contains("Wave")', engine='python')
nintendoGames_df = nintendoGames_df.query(f'not title.str.contains("DLC")', engine='python')
nintendoGames_df = nintendoGames_df.query(f'not title.str.contains("Edition")', engine='python')
nintendoGames_df['user_score'] = nintendoGames_df['user_score'].multiply(10)
#nintendoGames_df['user_score'] = ['user_score'].astype(int)
#Cleans and removes unnecessary data from dataframe

nintendoGames_df = nintendoGames_df.reset_index(drop=True) #Resets index so row numbers make sense

ActionGames = nintendoGames_df[nintendoGames_df["genres"].str.contains('Action\'')]
act_meta_avg = ActionGames.loc[:, 'meta_score'].mean()
act_meta_avg = round(act_meta_avg, 0)
act_user_avg = ActionGames.loc[:,'user_score'].mean()
act_user_avg = round(act_user_avg,0)
act_dict = {'title':'Average', 'meta_score':act_meta_avg, 'user_score':act_user_avg, 'platform':'Nintendo', 'genres':['Action']}
ActionGames = ActionGames._append(act_dict, ignore_index = True)

ActionAdventureGames = nintendoGames_df[nintendoGames_df["genres"].str.contains('Action A')]

ArcadeGames = nintendoGames_df[nintendoGames_df["genres"].str.contains('Arcade')]

FantasyGames = nintendoGames_df[nintendoGames_df["genres"].str.contains('Fantasy')]

PartyGames = nintendoGames_df[nintendoGames_df["genres"].str.contains('Party')]

PlatformerGames = nintendoGames_df[nintendoGames_df["genres"].str.contains('Platformer')]

RacingGames = nintendoGames_df[nintendoGames_df["genres"].str.contains('Racing')]

RoguelikeGames = nintendoGames_df[nintendoGames_df["genres"].str.contains('Roguelike')]

RolePlayingGames = nintendoGames_df[nintendoGames_df["genres"].str.contains('Role-Playing')]

SimulationGames = nintendoGames_df[nintendoGames_df["genres"].str.contains('Simulation')]

StrategyGames = nintendoGames_df[nintendoGames_df["genres"].str.contains('Strategy')]
strat_avg = StrategyGames.loc[:, 'meta_score'].mean()
strat_dict = {'title':'Average', 'meta_score':strat_avg, 'user_score':strat_avg, 'platform':'Nintendo', 'genres':['Strategy']}
StrategyGames = StrategyGames._append(strat_dict, ignore_index = True)

print(ActionGames)
 
