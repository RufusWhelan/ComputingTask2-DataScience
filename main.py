import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#Loading and Cleaning
try:
    nintendoGames_df = pd.read_csv('Data/NintendoGames.csv')

except:
    print("File could not be loaded.")
nintendoGames_df.dropna(inplace=True)
nintendoGames_df = nintendoGames_df[['title','meta_score','user_score','platform','genres']]
nintendoGames_df.drop_duplicates(inplace=True)
nintendoGames_df = nintendoGames_df[nintendoGames_df.platform != "iOS"]
nintendoGames_df = nintendoGames_df.query(f'not title.str.contains("Wave")', engine='python')
nintendoGames_df = nintendoGames_df.query(f'not title.str.contains("DLC")', engine='python')
nintendoGames_df = nintendoGames_df.query(f'not title.str.contains("Edition")', engine='python')
nintendoGames_df['user_score'] = nintendoGames_df['user_score'].multiply(10)
nintendoGames_df = nintendoGames_df.reset_index(drop=True) #Resets index so row numbers make sense
ogNintendoGames_df = nintendoGames_df
#

ActionGames = nintendoGames_df[nintendoGames_df["genres"].str.contains('Action\'')]
act_meta_avg = ActionGames.loc[:, 'meta_score'].mean()
act_meta_avg = round(act_meta_avg, 0)
act_user_avg = ActionGames.loc[:,'user_score'].mean()
act_user_avg = round(act_user_avg,0)
act_dict = {'title':'Average', 'meta_score':act_meta_avg, 'user_score':act_user_avg, 'platform':'Nintendo', 'genres':['Action']}
ActionGames = ActionGames._append(act_dict, ignore_index = True)

ActionAdventureGames = nintendoGames_df[nintendoGames_df["genres"].str.contains('Action A')]
actA_meta_avg = ActionAdventureGames.loc[:, 'meta_score'].mean()
actA_meta_avg = round(actA_meta_avg, 0)
actA_user_avg = ActionAdventureGames.loc[:,'user_score'].mean()
actA_user_avg = round(actA_user_avg,0)
actA_dict = {'title':'Average', 'meta_score':actA_meta_avg, 'user_score':actA_user_avg, 'platform':'Nintendo', 'genres':['Action Adventure']}
ActionAdventureGames = ActionGames._append(actA_dict, ignore_index = True)

FantasyGames = nintendoGames_df[nintendoGames_df["genres"].str.contains('Fantasy')]
ftsy_meta_avg = FantasyGames.loc[:, 'meta_score'].mean()
ftsy_meta_avg = round(ftsy_meta_avg, 0)
ftsy_user_avg = FantasyGames.loc[:,'user_score'].mean()
ftsy_user_avg = round(ftsy_user_avg,0)
ftsy_dict = {'title':'Average', 'meta_score':ftsy_meta_avg, 'user_score':ftsy_user_avg, 'platform':'Nintendo', 'genres':['Fantasy']}
FantasyGames = FantasyGames._append(ftsy_dict, ignore_index = True)

PartyGames = nintendoGames_df[nintendoGames_df["genres"].str.contains('Party')]
prty_meta_avg = PartyGames.loc[:, 'meta_score'].mean()
prty_meta_avg = round(prty_meta_avg, 0)
prty_user_avg = PartyGames.loc[:,'user_score'].mean()
prty_user_avg = round(prty_user_avg,0)
prty_dict = {'title':'Average', 'meta_score':prty_meta_avg, 'user_score':prty_user_avg, 'platform':'Nintendo', 'genres':['Party']}
PartyGames = PartyGames._append(prty_dict, ignore_index = True)

PlatformerGames = nintendoGames_df[nintendoGames_df["genres"].str.contains('Platformer')]
plfmr_meta_avg = PlatformerGames.loc[:, 'meta_score'].mean()
plfmr_meta_avg = round(plfmr_meta_avg, 0)
plfmr_user_avg = PlatformerGames.loc[:,'user_score'].mean()
plfmr_user_avg = round(plfmr_user_avg,0)
plfmr_dict = {'title':'Average', 'meta_score':plfmr_meta_avg, 'user_score':plfmr_user_avg, 'platform':'Nintendo', 'genres':['Platformer']}
PlatformerGames = PlatformerGames._append(plfmr_dict, ignore_index = True)

RacingGames = nintendoGames_df[nintendoGames_df["genres"].str.contains('Racing')]
rce_meta_avg = RacingGames.loc[:, 'meta_score'].mean()
rce_meta_avg = round(rce_meta_avg, 0)
rce_user_avg = RacingGames.loc[:,'user_score'].mean()
rce_user_avg = round(rce_user_avg,0)
rce_dict = {'title':'Average', 'meta_score':rce_meta_avg, 'user_score':rce_user_avg, 'platform':'Nintendo', 'genres':['Racing']}
RacingGames = RacingGames._append(rce_dict, ignore_index = True)

RolePlayingGames = nintendoGames_df[nintendoGames_df["genres"].str.contains('Role-Playing')]
rpg_meta_avg = RolePlayingGames.loc[:, 'meta_score'].mean()
rpg_meta_avg = round(rpg_meta_avg, 0)
rpg_user_avg = RolePlayingGames.loc[:,'user_score'].mean()
rpg_user_avg = round(rpg_user_avg,0)
rpg_dict = {'title':'Average', 'meta_score':rpg_meta_avg, 'user_score':rpg_user_avg, 'platform':'Nintendo', 'genres':['Role-Playing']}
RolePlayingGames = RolePlayingGames._append(rpg_dict, ignore_index = True)

SimulationGames = nintendoGames_df[nintendoGames_df["genres"].str.contains('Simulation')]
sim_meta_avg = SimulationGames.loc[:, 'meta_score'].mean()
sim_meta_avg = round(sim_meta_avg, 0)
sim_user_avg = SimulationGames.loc[:,'user_score'].mean()
sim_user_avg = round(sim_user_avg,0)
sim_dict = {'title':'Average', 'meta_score':sim_meta_avg, 'user_score':sim_user_avg, 'platform':'Nintendo', 'genres':['Simulation']}
SimulationGames = SimulationGames._append(sim_dict, ignore_index = True)

StrategyGames = nintendoGames_df[nintendoGames_df["genres"].str.contains('Strategy')]
strat_meta_avg = StrategyGames.loc[:, 'meta_score'].mean()
strat_meta_avg = round(strat_meta_avg, 0)
strat_user_avg = StrategyGames.loc[:,'user_score'].mean()
strat_user_avg = round(strat_user_avg,0)
strat_dict = {'title':'Average', 'meta_score':strat_meta_avg, 'user_score':strat_user_avg, 'platform':'Nintendo', 'genres':['Strategy']}
simulationGames = SimulationGames._append(strat_dict, ignore_index = True)

averagesList = [act_dict, actA_dict, ftsy_dict, prty_dict, plfmr_dict, rce_dict, rpg_dict, sim_dict, strat_dict]
genreAverages_df = pd.DataFrame(averagesList)

def ogData():
    print(ogNintendoGames_df)
    try:
        reset = int(input("type 1 to return to start: "))
        if reset == 1:
            mainloop()
        else:
            print('teehee Try again\n')
    except:
        print('teehee That\'s not a number! :( What would Mr Groome say?\n')

def genres():
    print("""
    Please select a genre:
    1 - Action
    2 - Action-Adventure
    3 - Fantasy
    4 - Party
    5 - Platformer
    6 - Racing
    7 - Role-Playing
    8 - Simulation
    9 - Strategy
    10 - Back
    11 - teehee special surprise.      
    """)
    try:
        choiceGenre = int(input('Select Number: '))

        if choiceGenre == 1:
            print(ActionGames)
        elif choiceGenre == 2:
            print(ActionAdventureGames)
        elif choiceGenre == 3:
            print(FantasyGames)
        elif choiceGenre == 4:
            print(PartyGames)
        elif choiceGenre == 5:
            print(PlatformerGames)
        elif choiceGenre == 6:
            print(RacingGames)
        elif choiceGenre == 7:
            print(RolePlayingGames)
        elif choiceGenre == 8:
            print(SimulationGames)
        elif choiceGenre == 9:
            print(StrategyGames)
        elif choiceGenre == 10:
            mainloop()
        elif choiceGenre == 11:
            print("go to https://www.youtube.com/watch?v=QB7ACr7pUuE if u r cool like Mr Scott :)\n")
        else:
            print('teehee Try again')

        reset = int(input("type 1 to return to start, type 2 to look at another genre.\n"))
        if reset == 1:
            mainloop()
        elif reset == 2:
            genres()
        else:
            print('teehee Try again\n')
            
    except:
        print('teehee That\'s not a number! :( What would Mr Groome say?\n')

def compareAverages():
    print(genreAverages_df)

def displayAverages():
    fig = plt.figure() # Create matplotlib figure

    ax = fig.add_subplot(111) # Create matplotlib axes
    ax2 = ax.twinx() # Create another axes that shares the same x-axis as ax.
    bars = ('Action', 'Action Adventure', 'Fantasy', 'Party', 'Platformer', 'Racing', 'RPG', 'Sim', 'Strategy')
    x_pos = np.arange(len(bars))

    width = 0.4

    genreAverages_df.meta_score.plot(kind='bar', color='red', ax=ax, width=width, position=1)
    genreAverages_df.user_score.plot(kind='bar', color='blue', ax=ax2, width=width, position=0)

    ax.set_ylabel('meta score')
    ax2.set_ylabel('user score')
    plt.xticks(x_pos, bars)               
    plt.show()

def keyWordFinder():
    keyword = input("Input keyword: ")
    keyword = keyword.title()
    Searched = nintendoGames_df[nintendoGames_df["title"].str.contains(keyword)]
    print(Searched)
    try:
        reset = int(input("type 1 to return to start, type 2 to enter a different keyword."))
        if reset == 1:
            mainloop()
        elif reset == 2:
            keyWordFinder()
        else:
            print('teehee Try again\n')
    except:
        print('teehee That\'s not a number! :( What would Mr Groome say?\n')
#def saveFiles():
    

def mainloop():
    global quit

    print("""This is a collection of data based on reviews for Nintendo Games. Have fun :)
          
    Please select an option:
    1 - See cleaned Dataframe
    2 - See Dataframe seperated into different genres
    3 - Compare average scores given by critics and users
    4 - Display average scores given by critics and users in graph form
    5 - Search for game/s by keyword
    6 - Write files to your computer
    7 - Quit Program
        """)
    #try:
    choice = int(input('Select Number: '))

    if choice == 1:
        ogData()

    elif choice == 2:
        genres()

    elif choice == 3:
        compareAverages()

    elif choice == 4:
        displayAverages()

    elif choice == 5:
        keyWordFinder()

    elif choice == 6:
        quit = True
    
    else:
        print('TEE HEE. Try again\n')

    #except:
       #print('TEE HEE. That\'s not a number :( What would Mr Groome say.\n')


while quit != True:
    mainloop()
