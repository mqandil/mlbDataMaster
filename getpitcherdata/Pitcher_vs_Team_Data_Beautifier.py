from seaborn.palettes import color_palette
from getpitcherdata.Pitcher_vs_Team import PitcherVsTeam as pt

import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd

class ReadPitcherVsTeamYear():

    def __init__(self, pitcher_lastname, pitcher_firstname, team_against):
        
        self.pitcher_lastname = pitcher_lastname
        self.pitcher_firstname = pitcher_firstname
        self.team_against = team_against

        get_pitcher_team_data = pt(self.pitcher_lastname, self.pitcher_firstname, self.team_against)
        pitcher_team_data = get_pitcher_team_data.get_year()
        self.pitcher_team_data = pitcher_team_data

    def outcomes(self):
        pitches_with_outcomes = self.pitcher_team_data[self.pitcher_team_data.events.notnull()]
        
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
            print(self.pitcher_lastname+" "+self.pitcher_firstname+" Has Never Faced "+self.team_against+"!")
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
        print(self.pitcher_lastname+" vs "+self.team_against+" 2021 Record:")
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
                '{:.2%}'.format((strikeouts+field_outs)/total_opportunities), 
                round((pitches_with_outcomes['estimated_ba_using_speedangle'].sum())/(singles+doubles+triples+home_runs+field_outs), 2),
                round((pitches_with_outcomes['estimated_woba_using_speedangle'].sum())/(singles+doubles+triples+home_runs+field_outs), 2)
                ]},
            index = ['Instances', 'Percentage', 'Avr. Est. BABIP Against', 'Avr. Est. WOBA Against'],
        )

        # outcomes_table.style.set_table_attributes("style='display:inline'").set_caption(self.pitcher_lastname+" vs "+self.team_against+" 2021 Record")

        return outcomes_table

    def graphs(self):
        pitches_all = self.pitcher_team_data[self.pitcher_team_data.events.notnull()]
        release_position_pitch_type = pitches_all.loc[:,['plate_x', 'plate_z', 'pitch_name']]
        
        unique_pitches = release_position_pitch_type['pitch_name'].unique()
        i = 1
        pitch_index_dictionary = {}
        for pitch in unique_pitches:
            pitch_index_dictionary[pitch]=i
            i += 1
        
        release_position_pitch_type['pitch_name_index'] = release_position_pitch_type['pitch_name'].map(pitch_index_dictionary)
            
        #Pitch Position Scatterplot
        pitch_pos_plot = sns.scatterplot(
            x = release_position_pitch_type['plate_x'], 
            y = release_position_pitch_type['plate_z'],
            hue = release_position_pitch_type['pitch_name_index'],
            palette = sns.color_palette('hls', len(unique_pitches)),
            legend = 'brief',
            
            )
        pitch_pos_plot.set_title(self.pitcher_firstname + ' ' + self.pitcher_lastname + ' vs. ' + self.team_against)
        pitch_pos_plot.legend(bbox_to_anchor = (1, 1), labels = unique_pitches)
        pitch_pos_plot.set_xlabel('')
        pitch_pos_plot.set_ylabel('')
        pitch_pos_plot.set(xticklabels=[], xlabel=None, xticks=[], yticklabels=[], ylabel=None, yticks=[])
        sns.set_theme(rc = {"axes.spines.right": False, "axes.spines.top": False, "axes.spines.left": False, "axes.spines.bottom": False})
        pitch_pos_plot.plot([-0.7083333, 0.7083333], [1.5, 1.5], color = 'black')
        pitch_pos_plot.plot([-0.7083333, 0.7083333], [3.75, 3.75], color = 'black')
        pitch_pos_plot.plot([-0.7083333, -0.7083333], [1.5, 3.75], color = 'black')
        pitch_pos_plot.plot([0.7083333, 0.7083333], [1.5, 3.75], color = 'black')




if __name__ == '__main__':
    test = ReadPitcherVsTeamYear('Eovaldi', 'Nathan', 'TB')
    print(test.graphs())