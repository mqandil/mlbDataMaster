from getpitcherdata.Get_Pitcher_Data import importPitcherData
from pybaseball import playerid_lookup
from pybaseball import team_batting
from getpitcherdata.Data_Column_Dictionary import get_column_id
import numpy as np
import pandas as pd


class PitcherVsTeam():
    def __init__(self, pitcher_lastname, pitcher_firstname, team_against):
        print('Initializing...')
        
        #Initializes Three Required Arguments
        self.pitcher_lastname = pitcher_lastname
        self.pitcher_firstname = pitcher_firstname
        self.team_against = team_against

        # Looks up Pitcher ID for Cross Reference with Batter Data
        download_pitcher_id = playerid_lookup(self.pitcher_lastname, self.pitcher_firstname)
        self.pitcher_id = int(download_pitcher_id['key_mlbam'])

        #Creates DataFrame and Defines Columns
        pitcher_team_pitch_data = pd.DataFrame(columns=[
            "pitch_type", "game_date", 'release_speed', 'release_pos_x', 
            'release_pos_z', 'player_name', 'batter', 'pitcher', 'events', 
            'description', 'spin_dir', 'spin_rate_deprecated', 'break_angle_deprecated', 
            'break_length_deprecated', 'zone', 'outcome', 'game_type', 'stand', 
            'p_throws', 'home_team', 'away_team', 'pitch_result', 'hit_location', 
            'bb_type', 'balls', 'strikes', 'game_year', 'pfx_x', 'pfx_z', 
            'plate_x', 'plate_z', 'on_3b', 'on_2b', 'on_1b', 'outs_when_up', 
            'inning', 'inning_topbot', 'hc_x', 'hc_y', 'tfs_deprecated', 
            'tfs_zulu_deprecated', 'fielder_2', 'umpire', 'sv_id', 'vx0', 
            'vy0', 'vz0', 'ax', 'ay', 'az', 'sz_top', 'sz_bot', 
            'hit_distance_sc', 'launch_speed', 'launch_angle', 'effective_speed', 
            'release_spin_rate', 'release_extension', 'game_pk', 'pitcher.1', 
            'fielder_2.1', 'fielder_3', 'fielder_4', 'fielder_5', 'fielder_6', 
            'fielder_7', 'fielder_8', 'fielder_9', 'release_pos_y', 
            'estimated_ba_using_speedangle', 'estimated_woba_using_speedangle', 
            'woba_value', 'woba_denom', 'babip_value', 'iso_value', 
            'launch_speed_angle', 'at_bat_number', 'pitch_number', 'pitch_name', 
            'home_score', 'away_score', 'bat_score', 'fld_score', 'post_away_score', 
            'post_home_score', 'post_bat_score', 'post_fld_score', 
            'if_fielding_alignment', 'of_fielding_alignment', 'spin_axis', 
            'delta_home_win_exp', 'delta_run_exp'])
        self.pitcher_team_pitch_data = pitcher_team_pitch_data

        team_abbreviations = {
            'Arizona Diamondbacks': 'ARI', 'Atlanta Braves': 'ATL', 'Baltimore Orioles': 'BAL', 
            'Boston Red Sox': 'BOS', 'Chicago Cubs': 'CHC', 'Chicago White Sox': 'CWS', 'Cincinati Reds': 'CIN',
            'Cincinnati Reds': 'CIN', 'Cleveland Indians': 'CLE', 'Colorado Rockies': 'COL', 
            'Detroit Tigers': 'DET', 'Houston Astros': 'HOU', 'Kansas City Royals': 'KC',
            'Los Angeles Angels': 'LAA', 'Los Angeles Dodgers': 'LAD', 'Miami Marlins': 'MIA', 
            'Milwaukee Brewers': 'MIL', 'Minnesota Twins': 'MIN', 'New York Mets': 'NYM', 'New York Yankees': 'NYY', 
            'Oakland Athletics': 'OAK', 'Philadelphia Phillies': 'PHI', 'Pittsburgh Pirates': 'PIT',
            'San Diego Padres': 'SD', 'Seattle Mariners': 'SEA', 'San Francisco Giants': 'SF',
            'St. Louis Cardinals': 'STL', 'Tampa Bay Rays': 'TB', 'Texas Rangers': 'TEX', 'Toronto Blue Jays': 'TOR',
            'Washington Nationals': 'WSH'
        }

    def get_year(self):

        #Imports all Data from Batter in Year
        print('Gathering Batter Data...')
        pitcher = importPitcherData(self.pitcher_lastname, self.pitcher_firstname)
        pitcher_pitch_data = np.array(pitcher.get_year())

        #Empty list to place pitches that meet criteria, index counter for iteration        
        list_of_matches = []
        i = 0

        #Gets Cross Referenced Data and Appends Index to list_of_matches
        print('Cross Referencing Team and Pitcher Data...')
        for row in pitcher_pitch_data:
            home_team = row[get_column_id('home_team')]
            away_team = row[get_column_id('away_team')]
            if self.team_against == home_team or self.team_against == away_team:
                list_of_matches.append(i)
                i += 1
            else:
                i += 1

        #Index Counter for Iteration
        j = 0

        #Iterates through list of indices that met criteria to add array rows to DataFrame
        print('Adding Data to DataFrame...')
        for index in list_of_matches:
            self.pitcher_team_pitch_data.loc[len(self.pitcher_team_pitch_data.index)] = pitcher_pitch_data[index]
            j += 1
        
        return self.pitcher_team_pitch_data

    def get_all(self):

        #Imports all Data from Batter in Year
        print('Gathering Batter Data...')
        pitcher = importPitcherData(self.pitcher_lastname, self.pitcher_firstname)
        pitcher_pitch_data = np.array(pitcher.get_all())

        #Empty list to place pitches that meet criteria, index counter for iteration        
        list_of_matches = []
        i = 0

        #Gets Cross Referenced Data and Appends Index to list_of_matches
        print('Cross Referencing Team and Pitcher Data...')
        for row in pitcher_pitch_data:
            home_team = row[get_column_id('home_team')]
            away_team = row[get_column_id('away_team')]
            if self.team_against == home_team or self.team_against == away_team:
                list_of_matches.append(i)
                i += 1
            else:
                i += 1

        #Index Counter for Iteration
        j = 0

        #Iterates through list of indices that met criteria to add array rows to DataFrame
        print('Adding Data to DataFrame...')
        for index in list_of_matches:
            self.pitcher_team_pitch_data.loc[len(self.pitcher_team_pitch_data.index)] = pitcher_pitch_data[index]
            j += 1
        
        return self.pitcher_team_pitch_data
        
if __name__ == '__main__':
    test = importPitcherData('Scherzer', 'Max')
    test.get_year().to_csv('test.csv', index=False)
