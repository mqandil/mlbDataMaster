from pybaseball import statcast_batter
from pybaseball import playerid_lookup
from datetime import datetime

class importBatterData():
    def __init__(self, batter_lastname, batter_firstname):
        self.batter_lastname = batter_lastname
        self.batter_firstname = batter_firstname
        
        #Gets Player ID
        download_id = playerid_lookup(self.batter_lastname, self.batter_firstname)
        self.player_id = str(int(download_id['key_mlbam']))

        #Gets Current Date
        get_current_date = datetime.now()
        self.current_date = get_current_date.strftime('%Y-%m-%d')
    
    #Looks up Player and returns pitch-by-pitch statcast data (dataframe)
    def get_last_month(self):
        last_month_date = (
            self.current_date[0:5]+'0'+
            str(int(self.current_date[5:7])-1)+self.current_date[7:10]
        )       
        return statcast_batter(last_month_date, self.current_date, self.player_id)
    
    def get_last_two_months(self):
        two_months_past_date = (
            self.current_date[0:5]+'0'+
            str(int(self.current_date[5:7])-2)+self.current_date[7:10]
        )
        return statcast_batter(two_months_past_date, self.current_date, self.player_id)

    def get_all(self):
        return statcast_batter('1900-01-01', self.current_date, self.player_id)

    def get_year(self):
        year_start = self.current_date[0:5]+str('01')+self.current_date[7:10]
        return statcast_batter(year_start, self.current_date, self.player_id)