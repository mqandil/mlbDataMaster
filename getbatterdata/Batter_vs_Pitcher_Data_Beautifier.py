from Batter_vs_Pitcher import BatterVsPitcher as bp

import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


class ReadBatterVsPitcherAll():

    def __init__(self):
        
        self.batter_lastname = input("Batter's Last Name:")
        self.batter_firstname = input("Batter's First Name:")
        self.pitcher_lastname = input("Pitcher's Last Name:")
        self.pitcher_firstname = input("Pitcher's First Name:")

        get_batter_pitcher_data = bp(self.batter_lastname, self.batter_firstname, self.pitcher_lastname, self.pitcher_firstname)
        batter_pitcher_data = get_batter_pitcher_data.get_all()
        self.batter_pitcher_data = batter_pitcher_data

    def outcomes(self):
        pitches_with_outcomes = self.batter_pitcher_data[self.batter_pitcher_data.events.notnull()]
        
        #Basic Counting Stats
        singles = len(pitches_with_outcomes[pitches_with_outcomes.events == 'single'])
        doubles = len(pitches_with_outcomes[pitches_with_outcomes.events == 'double'])
        triples = len(pitches_with_outcomes[pitches_with_outcomes.events == 'triple'])
        home_runs = len(pitches_with_outcomes[pitches_with_outcomes.events == 'home_run'])
        walks = len(pitches_with_outcomes[pitches_with_outcomes.events == 'walk'])
        strikeouts = len(pitches_with_outcomes[pitches_with_outcomes.events == 'strikeout'])
        field_outs = len(pitches_with_outcomes[pitches_with_outcomes.events == 'field_out'])
        total_opportunities = singles + doubles + triples + home_runs + walks + strikeouts + field_outs

        if total_opportunities == 0:
            print('These Players Have Never Faced Each Other!')
            return

        #Singles BA/WOBA
        if singles != 0:
            singlesdf = pitches_with_outcomes[pitches_with_outcomes.events == 'single']
            singles_est_ba = (singlesdf['estimated_ba_using_speedangle'].sum())/singles
            singles_est_woba = (singlesdf['estimated_woba_using_speedangle'].sum())/singles
        else:
            singles_est_ba = 0
            singles_est_woba = 0

        #Doubles BA/WOBA
        if doubles != 0:
            doublesdf = pitches_with_outcomes[pitches_with_outcomes.events == 'double']
            doubles_est_ba = (doublesdf['estimated_ba_using_speedangle'].sum())/doubles
            doubles_est_woba = (doublesdf['estimated_woba_using_speedangle'].sum())/doubles
        else:
            doubles_est_ba = 0
            doubles_est_woba = 0

        #Triples BA/WOBA
        if triples != 0:
            triplesdf = pitches_with_outcomes[pitches_with_outcomes.events == 'triple']
            triples_est_ba = (triplesdf['estimated_ba_using_speedangle'].sum())/triples
            triples_est_woba = (triplesdf['estimated_woba_using_speedangle'].sum())/triples
        else:
            triples_est_ba = 0
            triples_est_woba = 0

        #Home Runs BA/WOBA
        if home_runs != 0:
            home_runsdf = pitches_with_outcomes[pitches_with_outcomes.events == 'home_run']
            home_runs_est_ba = (home_runsdf['estimated_ba_using_speedangle'].sum())/home_runs
            home_runs_est_woba = (home_runsdf['estimated_woba_using_speedangle'].sum())/home_runs
        else:
            home_runs_est_ba = 0
            home_runs_est_woba = 0

        #Field Outs BA/WOBA
        if field_outs != 0:
            field_outsdf = pitches_with_outcomes[pitches_with_outcomes.events == 'field_out']
            field_outs_est_ba = (field_outsdf['estimated_ba_using_speedangle'].sum())/field_outs
            field_outs_est_woba = (field_outsdf['estimated_woba_using_speedangle'].sum())/field_outs
        else:
            field_outs_est_ba = 0
            field_outs_est_woba = 0

        #Metrics by Outcome Table
        print(self.batter_lastname+" vs "+self.pitcher_lastname+" All-Time Record:")
        outcomes_table = pd.DataFrame({
            'Single': [int(singles), '{:.2%}'.format(singles/total_opportunities), round(singles_est_ba, 2), round(singles_est_woba, 2)],
            'Double': [int(doubles), '{:.2%}'.format(doubles/total_opportunities), round(doubles_est_ba, 2), round(doubles_est_woba, 2)],
            'Triple': [int(triples), '{:.2%}'.format(triples/total_opportunities), round(triples_est_ba, 2), round(triples_est_woba, 2)],
            'Home Run': [int(home_runs), '{:.2%}'.format(home_runs/total_opportunities), round(home_runs_est_ba, 2), round(home_runs_est_woba, 2)],
            'Walk': [int(walks), '{:.2%}'.format(walks/total_opportunities), 'N/A', 'N/A'],
            'Strikeout': [int(strikeouts), '{:.2%}'.format(strikeouts/total_opportunities), 'N/A', 'N/A'],
            'Field Out': [int(field_outs), '{:.2%}'.format(field_outs/total_opportunities), round(field_outs_est_ba, 2), round(field_outs_est_woba, 2)],
            'Total': [
                int(total_opportunities),
                '{:.2%}'.format((singles+doubles+triples+home_runs+walks)/total_opportunities), 
                round((pitches_with_outcomes['estimated_ba_using_speedangle'].sum())/(singles+doubles+triples+home_runs+field_outs), 2),
                round((pitches_with_outcomes['estimated_woba_using_speedangle'].sum())/(singles+doubles+triples+home_runs+field_outs), 2)
                ]},
            index = ['Instances', 'Percentage', 'Avr. Est. BABIP', 'Avr. Est. WOBA'],
        )

        return outcomes_table

    def pitch_types(self):
        
        pitches = self.batter_pitcher_data[self.batter_pitcher_data.pitch_type.notnull()]

        auto_ball = len(pitches[pitches.pitch_type == "AB"])
        auto_strike = len(pitches[pitches.pitch_type == "AS"])
        change_up = len(pitches[pitches.pitch_type == "CH"])
        curveball = len(pitches[pitches.pitch_type == "CU"])
        eephus = len(pitches[pitches.pitch_type == "EP"])
        cutter = len(pitches[pitches.pitch_type == "FC"])
        four_fastball = len(pitches[pitches.pitch_type == "FF"])
        forkball = len(pitches[pitches.pitch_type == "FO"])
        splitter = len(pitches[pitches.pitch_type == "FS"])
        two_fastball = len(pitches[pitches.pitch_type == "FT"])
        gyroball = len(pitches[pitches.pitch_type == "GY"])
        intentional_ball = len(pitches[pitches.pitch_type == "IN"])
        knuckle_curve = len(pitches[pitches.pitch_type == "KC"])
        knuckleball = len(pitches[pitches.pitch_type == "KN"])
        no_pitch = len(pitches[pitches.pitch_type == "NP"])
        pitchout = len(pitches[pitches.pitch_type == "PO"])
        screwball = len(pitches[pitches.pitch_type == "SC"])
        sinker = len(pitches[pitches.pitch_type == "SI"])
        slider = len(pitches[pitches.pitch_type == "SL"])
        unknown = len(pitches[pitches.pitch_type == "UN"])

        hit_into_play = len(pitches[pitches.description == "hit_into_play"])
        called_strike = len(pitches[pitches.description == "called_strike"])
        ball = len(pitches[pitches.description == "ball"])
        foul = len(pitches[pitches.description == "foul"])
        swinging_strike = len(pitches[pitches.description == "swinging_strike"])
        swinging_strike_blocked = len(pitches[pitches.description == "swinging_strike_blocked"])

        pitch_list = [auto_ball, auto_strike, change_up, curveball, eephus, 
            cutter, four_fastball, forkball, splitter, two_fastball, 
            gyroball, intentional_ball, knuckle_curve, knuckleball, 
            no_pitch, pitchout, screwball, sinker, slider, unknown]

        pitch_dict = {
            auto_ball: 'AB', auto_strike: 'AS', change_up: 'CH', curveball: 'CU', eephus: 'EP', 
            cutter: 'FC', four_fastball: 'FF', forkball: 'FO', splitter: 'FS', two_fastball: 'FT', 
            gyroball: 'GY', intentional_ball: 'IN', knuckle_curve: 'KC', knuckleball: 'KN', 
            no_pitch: 'NP', pitchout: 'PO', screwball: 'SC', sinker: 'SI', slider: 'SL', unknown: 'UN'
            }

        for pitch_type in pitch_list:
            if pitch_type == 0:
                pitch_dict.pop(pitch_type)
                pitch_list.pop(pitch_type)

        pitch_outcome_list = [ball, called_strike, swinging_strike, swinging_strike_blocked, foul, hit_into_play]
        
        pitch_outcome_dict = {
            hit_into_play: 'hit_into_play', called_strike: 'called_strike', ball: 'ball', foul: 'foul', 
            swinging_strike: 'swinging_strike', swinging_strike_blocked: 'swinging_strike_blocked'
        }

        for pitch in pitch_outcome_list:
            if pitch == 0:
                pitch_outcome_list.pop(pitch)
                pitch_outcome_dict.pop(pitch)
        
        for pitch_type in pitch_list:
            pitches_in_pitch_type = pitches[pitches.pitch_type == pitch_dict[pitch]]
            for pitch in pitches_in_pitch_type:
                str(pitch)



        pitch_outcome_dataframe = pd.DataFrame({
            

            },
            columns = pitch_outcome_list
        )