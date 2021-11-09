from pybaseball import statcast_pitcher
from pybaseball import playerid_lookup
from datetime import datetime

class importPitcherData():
    def __init__(self, pitcher_lastname, pitcher_firstname):
        self.pitcher_lastname = pitcher_lastname
        self.pitcher_firstname = pitcher_firstname
        
        #Gets Player ID
        download_id = playerid_lookup(self.pitcher_lastname, self.pitcher_firstname)
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
        return statcast_pitcher(last_month_date, self.current_date, self.player_id)
    
    def get_last_two_months(self):
        two_months_past_date = (
            self.current_date[0:5]+'0'+
            str(int(self.current_date[5:7])-2)+self.current_date[7:10]
        )
        return statcast_pitcher(two_months_past_date, self.current_date, self.player_id)

    def get_year(self):
        year_start = self.current_date[0:5]+str('01')+self.current_date[7:10]
        return statcast_pitcher(year_start, self.current_date, self.player_id)

    def get_all(self):
        return statcast_pitcher('1900-01-01', self.current_date, self.player_id)

if __name__ == '__main__':
    test = importPitcherData('Scherzer', 'Max')
    print(test.get_year())