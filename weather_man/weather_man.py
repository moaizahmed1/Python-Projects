import os
import csv
import argparse

class WeatherEntry:
    def __init__(self, date, max_temp, min_temp, hum):
        self.date = date
        self.max_temp = int(max_temp) if max_temp else 0
        self.min_temp = int(min_temp) if min_temp else 0
        self.hum = int(hum) if hum else 0

class WeatherReader:
    def get_data(self, folder, year, month=None):
        data = []
        
        month_map = {
            "1": "Jan", "01": "Jan", "2": "Feb", "02": "Feb", "3": "Mar", "03": "Mar", 
            "4": "Apr", "04": "Apr", "5": "May", "05": "May", "6": "Jun", "06": "Jun",
            "7": "Jul", "07": "Jul", "8": "Aug", "08": "Aug", "9": "Sep", "09": "Sep",
            "10": "Oct", "11": "Nov", "12": "Dec"
            
        }
        
        for filename in os.listdir(folder):
            if year in filename:
                if month:
                    month_name = month_map.get(month, month) 
                    if month_name not in filename:
                        continue
                
                path = os.path.join(folder, filename)
                with open(path, "r") as f:
                    reader = csv.reader(f)
                    next(reader)
                    for row in reader:
                        if len(row) > 8 and row[1].strip():
                            data.append(WeatherEntry(row[0], row[1], row[3], row[8]))
        return data

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("folder")
    parser.add_argument("-e", "--extreme")
    parser.add_argument("-a", "--average")
    parser.add_argument("-c", "--chart")
    args = parser.parse_args()
    
    reader = WeatherReader()

    if args.extreme:
        results = reader.get_data(args.folder, args.extreme)
        
        if results:
            hi = results[0]
            lo = results[0]
            
            for item in results:
                if item.max_temp > hi.max_temp:
                    hi = item
                if item.min_temp < lo.min_temp:
                    lo = item
                    
            print("Highest:", hi.max_temp, "C on", hi.date)
            print("Lowest:", lo.min_temp, "C on", lo.date)

    # Average Option
    if args.average:
        y, m = args.average.split('/')
        results = reader.get_data(args.folder, y, m)
        
        # Only run math if results actually has data
        if len(results) > 0:
            avg_max = sum(x.max_temp for x in results) / len(results)
            print("Highest Average:", int(avg_max), "C")
        else:
            print("No data found for the average calculation.")

    # Chart Option
    if args.chart:
        y, m = args.chart.split('/')
        results = reader.get_data(args.folder, y, m)
        
        # Only draw if we found data
        if len(results) > 0:
            for r in results:
                day = r.date.split("-")[2]
                print(day, "+" * r.max_temp, r.max_temp, "C")
        else:
            print("No data found for the chart.")

main()