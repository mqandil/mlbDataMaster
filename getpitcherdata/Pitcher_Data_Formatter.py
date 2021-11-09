from getpitcherdata.Get_Probable_Pitchers import get_probable_pitchers as pp
from getpitcherdata.Pitcher_vs_Team_Data_Beautifier import ReadPitcherVsTeamYear as pt
from datetime import datetime

##################################################################

def pitcher_vs_team_data_formatter():

    probable_pitcher_data = pp()

    get_current_date = datetime.now()
    current_date = '05-11-2021' #get_current_date.strftime('%m-%d-%Y')

    i = 1
    j = len(probable_pitcher_data)

    for pitcher_team in probable_pitcher_data:
        
        print('Getting '+pitcher_team[1]+' '+pitcher_team[0]+"'s Record vs "+pitcher_team[2])
        title = pitcher_team[1]+' '+pitcher_team[0]+"'s Record vs "+pitcher_team[2]

        try:
            with open('pitcher_data_'+current_date+'.csv', 'a') as test_csv:
                test_csv.write('\n')
                test_csv.write(pitcher_team[0]+" vs "+pitcher_team[2]+" 2021 Record \n")
                test_csv.close()
            pitcher_team_data = pt(pitcher_team[0], pitcher_team[1], pitcher_team[2])    
            pitcher_team_data.outcomes().to_csv('pitcher_data_'+current_date+'.csv', mode = 'a')
            print('{:.0%}'.format((i/j))+' Done!')
            i += 1

        except:
            print('No Name Match!')
            print('{:.0%}'.format((i/j))+' Done!')
            i += 1

if __name__ == '__main__':
    pitcher_vs_team_data_formatter()