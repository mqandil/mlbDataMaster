from getpitcherdata.Pitcher_Data_Formatter import pitcher_vs_team_data_formatter as ptdf
from datetime import datetime

current_date = datetime.now().strftime('%m-%d-%Y')
 
file_name = "pitcher_data_"+"05-11-2021"+".csv"

with open(file_name, "r") as pitcher_team_csv:
    print(pitcher_team_csv)
    pitcher_team_csv.close()
