from Get_Batter_Data import importBatterData
from pybaseball import playerid_lookup
from Data_Column_Dictionary import get_column_id
import numpy as np
import pandas as pd

class BatterVsPitcher():
    def __init__(self, batter_lastname, batter_firstname, pitcher_lastname, pitcher_firstname):
        print('Initializing...')
        
        #Initializes Four Required Arguments
        self.batter_lastname = batter_lastname
        self.batter_firstname = batter_firstname
        self.pitcher_lastname = pitcher_lastname
        self.pitcher_firstname = pitcher_firstname

        # Looks up Pitcher ID for Cross Reference with Batter Data
        download_pitcher_id = playerid_lookup(self.pitcher_lastname, self.pitcher_firstname)
        self.pitcher_id = int(download_pitcher_id['key_mlbam'])

        #Creates DataFrame and Defines Columns
        batter_and_pitcher_pitch_data = pd.DataFrame(columns=[
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
            'delta_home_win_exp', 'delta_run_exp']) #MISSING ROW HERE / HIT DISTANCE MAY BE PROBLEM
        self.batter_and_pitcher_pitch_data = batter_and_pitcher_pitch_data

    def get_year(self):

        #Imports all Data from Batter in Year
        print('Gathering Batter Data...')
        batter = importBatterData(self.batter_lastname, self.batter_firstname)
        batter_pitch_data = np.array(batter.get_year())

        #Empty list to place pitches that meet criteria, index counter for iteration        
        list_of_matches = []
        i = 0

        #Gets Cross Referenced Data and Appends Index to list_of_matches
        print('Cross Referencing Batter and Pitcher Data...')
        for row in batter_pitch_data:
            pitcher_id = row[get_column_id('pitcher')]
            real_pitcher_id = (self.pitcher_id)
            if int(pitcher_id) == int(real_pitcher_id):
                list_of_matches.append(i)
                i += 1
            else:
                i += 1
        
        #Iterates through list of indices that met criteria to add array rows to DataFrame
        j = 0
        print('Adding Data to DataFrame...')
        for index in list_of_matches:
            self.batter_and_pitcher_pitch_data.loc[len(self.batter_and_pitcher_pitch_data.index)] = batter_pitch_data[index]
            j += 1
        
        return self.batter_and_pitcher_pitch_data

    def get_all(self):

        #Imports all Data from Batter in Year
        print('Gathering Batter Data...')
        batter = importBatterData(self.batter_lastname, self.batter_firstname)
        batter_pitch_data = np.array(batter.get_all())


        #Empty list to place pitches that meet criteria, index counter for iteration        
        list_of_matches = []
        i = 0

        #Gets Cross Referenced Data and Appends Index to list_of_matches
        print('Cross Referencing Batter and Pitcher Data...')
        for row in batter_pitch_data:
            pitcher_id = row[get_column_id('pitcher')]
            real_pitcher_id = (self.pitcher_id)
            if int(pitcher_id) == int(real_pitcher_id):
                list_of_matches.append(i)
                i += 1
            else:
                i += 1

        #Index Counter for Iteration
        j = 0

        #Iterates through list of indices that met criteria to add array rows to DataFrame
        print('Adding Data to DataFrame...')
        for index in list_of_matches:
            self.batter_and_pitcher_pitch_data.loc[len(self.batter_and_pitcher_pitch_data.index)] = batter_pitch_data[index]
            j += 1
        
        return self.batter_and_pitcher_pitch_data