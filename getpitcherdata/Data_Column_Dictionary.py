column_id_dict = {
    "pitch_type": 0, "game_date": 1, 'release_speed': 2, 'release_pos_x': 3, 
    'release_pos_z': 4, 'player_name': 5, 'batter': 6, 'pitcher': 7, 'events': 8, 
    'description': 9, 'spin_dir': 10, 'spin_rate_deprecated': 11, 'break_angle_deprecated': 12, 
    'break_length_deprecated': 13, 'zone': 14, 'outcome': 15, 'game_type': 16, 'stand': 17, 
    'p_throws': 18, 'home_team': 19, 'away_team': 20, 'pitch_result': 21, 'hit_location': 22, 
    'bb_type': 23, 'balls': 24, 'strikes': 25, 'game_year': 26, 'pfx_x': 27, 'pfx_z': 28, 
    'plate_x': 29, 'plate_z': 30, 'on_3b': 31, 'on_2b': 32, 'on_1b': 33, 'outs_when_up': 34, 
    'inning': 35, 'inning_topbot': 36, 'hc_x': 37, 'hc_y': 38, 'tfs_deprecated': 39, 
    'tfs_zulu_deprecated': 40, 'fielder_2': 41, 'umpire': 42, 'sv_id': 43, 'vx0': 44, 
    'vy0': 45, 'vz0': 46, 'ax': 47, 'ay': 48, 'az': 49, 'sz_top': 50, 'sz_bot': 51, 
    'hit_distance_sc': 52, 'launch_speed': 53, 'launch_angle': 54, 'effective_speed': 55, 
    'release_spin_rate': 56, 'release_extension': 57, 'game_pk': 58, 'pitcher.1': 59, 
    'fielder_2.1': 60, 'fielder_3': 61, 'fielder_4': 62, 'fielder_5': 63, 'fielder_6': 64, 
    'fielder_7': 65, 'fielder_8': 66, 'fielder_9': 67, 'release_pos_y': 68, 
    'estimated_ba_using_speedangle': 69, 'estimated_woba_using_speedangle': 70, 
    'woba_value': 71, 'woba_denom': 72, 'babip_value': 73, 'iso_value': 74, 
    'launch_speed_angle': 75, 'at_bat_number': 76, 'pitch_number': 77, 'pitch_name': 78, 
    'home_score': 79, 'away_score': 80, 'bat_score': 81, 'fld_score': 82, 'post_away_score': 83, 
    'post_home_score': 84, 'post_bat_score': 85, 'post_fld_score': 86, 
    'if_fielding_alignment': 87, 'of_fielding_alignment': 88, 'spin_axis': 89, 
    'delta_home_win_exp': 90, 'delta_run_exp': 91
    }

def column_id_options():
    for key, value in column_id_dict.items():
        print(key)

def get_column_id(column_key):
    return column_id_dict[column_key]