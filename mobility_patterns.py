import pandas as pd
import matplotlib
import requests
import json
import csv

class pandas_alok():
    
    def __init__(self, path):
        self.path = path
        self.df = pd.read_csv(path)

        self.col_list = []
        for col in self.df.columns:
            self.col_list.append(col)
    

    def empty_class(self):
        pass

url = f"http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=48549&Year={year_range}&Month={month_range}&Day=14&timeframe=1&submit=Download+Data" 
response = requests.get(url)

csv_read = csv.reader(response.text)

# make f-string iterate over all dates in range
# save all responses to one csv file

