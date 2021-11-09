from datetime import datetime
import requests
from bs4 import BeautifulSoup

def get_probable_pitchers():
    
    #Creates Daily Link for Probable Pitchers
    get_current_date = datetime.now()
    current_date = '2021-05-11' #get_current_date.strftime('%Y-%m-%d')
    probable_pitchers_link = 'https://www.mlb.com/probable-pitchers/'+current_date

    #Stores HTML from Link
    get_probable_pitchers_html = requests.get(probable_pitchers_link)
    probable_pitchers_html = get_probable_pitchers_html.text

    #Finds Appropriate HTML for Pitcher Names
    probable_pitchers_bs4 = BeautifulSoup(probable_pitchers_html, features="lxml")
    probable_pitchers = probable_pitchers_bs4.find_all(class_=['probable-pitchers__pitcher-name-link', 'probable-pitchers__pitcher-name'])

    #Empty List for Pitcher Names
    probable_pitchers_list = []

    #Iterates through Strings and Extracts Pitcher Names
    for item in probable_pitchers:
        item = item.contents[0]
        probable_pitchers_list.append(item)

    for item in probable_pitchers_list:
        if item == '\n':
            probable_pitchers_list.remove(item)

        elif '\n' in item:
            index = probable_pitchers_list.index(item)
            probable_pitchers_list[index] = "TBD"

    #For Altering Names to Abbreviations (Needed for Retreiving Statcast Data)
    team_abbreviations = {
        'D-backs': 'ARI', 'Braves': 'ATL', 'Orioles': 'BAL', 
        'Red Sox': 'BOS', 'Cubs': 'CHC', 'White Sox': 'CWS', 'Reds': 'CIN',
        'Reds': 'CIN', 'Indians': 'CLE', 'Rockies': 'COL', 
        'Tigers': 'DET', 'Astros': 'HOU', 'Royals': 'KC',
        'Angels': 'LAA', 'Dodgers': 'LAD', 'Marlins': 'MIA', 
        'Brewers': 'MIL', 'Twins': 'MIN', 'Mets': 'NYM', 'Yankees': 'NYY', 
        'Athletics': 'OAK', 'Phillies': 'PHI', 'Pirates': 'PIT',
        'Padres': 'SD', 'Mariners': 'SEA', 'Giants': 'SF',
        'Cardinals': 'STL', 'Rays': 'TB', 'Rangers': 'TEX', 'Blue Jays': 'TOR',
        'Nationals': 'WSH'
    }

    #Gets Home and Away Teams
    team_names = probable_pitchers_bs4.find_all(class_=[
        'probable-pitchers__team-name probable-pitchers__team-name--away', 
        'probable-pitchers__team-name probable-pitchers__team-name--home'
        ])

    #For Team Names
    team_names_list = []

    #Iterates through Strings and gets Team Names
    for item in team_names:
        strip_span = str(item).strip('<span class="probable-pitchers__team-name probable-pitchers__team-name--away">')
        strip_end = strip_span.strip('</')
        stripped_name = strip_end.strip()
        team_names_list.append(stripped_name)

    #Reorders for "Team Against" Instead of "Team On"
    team_names_reorder_dict = {
        0:1, 1:0, 2:3, 3:2, 4:5, 5:4, 6:7, 7:6, 
        8:9, 9:8, 10:11, 11:10, 12:13, 13:12, 
        14:15, 15:14, 16:17, 17:16, 18:19, 19:18, 
        20:21, 21:20, 22:23, 23:22, 24:25, 25:24, 
        26:27, 27:26, 28:29, 29:28
        }

    #Lists for final 2D List
    team_against_list = []
    first_name_list = []
    last_name_list = []
    
    tbd_differentiator = 1
    counter = 0

    #Parses out First and Last Names, Reorders Team Names, Appends Data to Final 2D List
    for pitcher in probable_pitchers_list:

        if "TBD" not in pitcher:
            index = pitcher.index(' ')
            first_name = pitcher[0:index]
            last_name = pitcher[index+1:]
            first_name_list.append(first_name)
            last_name_list.append(last_name)
        else:
            first_name = 'TBD'+str(tbd_differentiator)
            last_name = 'TBD'+str(tbd_differentiator)
            first_name_list.append(first_name)
            last_name_list.append(last_name)
            tbd_differentiator += 1
        
        try:
            pitcher_index = counter
            team_against = team_names_list[team_names_reorder_dict[pitcher_index]]
            team_against_abbr = team_abbreviations[team_against]
            team_against_list.append(team_against_abbr)
        except:
            pass
        counter += 1
        
    iteration_list = list(range(0, 30))
    pitcher_team_list = []

    for index in iteration_list:
        try:
            pitcher_team_inner_list = [last_name_list[index], first_name_list[index], team_against_list[index]]
            pitcher_team_list.append(pitcher_team_inner_list)
        except:
            pass

    return pitcher_team_list