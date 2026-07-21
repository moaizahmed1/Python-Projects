import os
import csv
import argparse

class WeatherMan:
    def __init__(self, date, max_temperature, min_temperature, humidity):
        self.date = date
        self.max_temperature = int(max_temperature) if max_temperature else 0
        self.min_temperature = int(min_temperature) if min_temperature else 0
        self.humidity = int(humidity) if humidity else 0


class WeatherReader:
    
    def get_weather_files_to_read(self, folder, year, month=None):
        month_name_map = {
            "1": "Jan", "2": "Feb", "3": "Mar",
            "4": "Apr", "5": "May", "6": "Jun",
            "7": "Jul", "8": "Aug", "9": "Sep",
            "10": "Oct", "11": "Nov", "12": "Dec"
        }
        files_to_read = []
        
        if month:
           m_name = month_name_map.get(str(month), str(month))
           target_filename = f"Murree_weather_{year}_{m_name}.txt"
           
           if os.path.exists(os.path.join(folder, target_filename)):
                # Sirf file ka naam append karein, path get_weather_data mein banega
                files_to_read.append(target_filename)
        else:
            months = month_name_map.values()
            for _month in months:
                _target_filename = f"Murree_weather_{year}_{_month}.txt"            
                if os.path.exists(os.path.join(folder, _target_filename)):
                    files_to_read.append(_target_filename)
        
        return files_to_read
    
    def _parse_weather_file(self, path):
        file_data = {}
        with open(path, "r") as f:
            reader = csv.DictReader(f)
            
            for row in reader:
                Main_Key=row["PKT"]
                
                file_data[Main_Key] = WeatherMan(
                    date=row["PKT"],
                    max_temperature=row["Max TemperatureC"],
                    min_temperature=row["Min TemperatureC"],
                    humidity=row[" Mean Humidity"]
                    )
                    
        return file_data
    
    def get_weather_data(self, folder, year, month=None):
        read_weather_files = self.get_weather_files_to_read(folder, year, month)
        weather_dictionary = {}  
        
        for filename in read_weather_files:
            path = os.path.join(folder, filename)
            file_data = self._parse_weather_file(path)
            weather_dictionary.update(file_data)
            
        return weather_dictionary


class Weathercalculator:
    @staticmethod
    def get_extreme_values(weather_dictionary):
        results = list(weather_dictionary.values())
        if not results:
            return None, None, None
            
        high = low = results[0]
        max_hum_entry = results[0]
        
        for item in results:
            if item.max_temperature > high.max_temperature: 
                high = item
            if item.min_temperature < low.min_temperature: 
                low = item
            if item.humidity > max_hum_entry.humidity:
                max_hum_entry = item
                
        return high, low, max_hum_entry

    @staticmethod
    def get_average_valuess(weather_dictionary):
        results = list(weather_dictionary.values())
        if not results:
            return 0, 0, 0
            
        average_max_temperature = sum(x.max_temperature for x in results) / len(results)
        average_min_temperature = sum(x.min_temperature for x in results) / len(results)
        average_min_humidity = sum(x.humidity for x in results) / len(results)
        
        return int(average_max_temperature), int(average_min_temperature), int(average_min_humidity)


class WeatherReportGenerator:
    @staticmethod
    def print_extreme_temperature(high, low, max_humidity):
        if high and low:
            print(f"Highest: {high.max_temperature}C on {high.date}")
            print(f"Lowest: {low.min_temperature}C on {low.date}")
        if max_humidity:
            print(f"Humidity: {max_humidity.humidity}% on {max_humidity.date}")
            print("\n")

    @staticmethod
    def print_average_temperature(average_max_temperature, average_min_temperature, average_min_humidity):
        print(f"Highest Average: {average_max_temperature}C")
        print(f"Lowest Average: {average_min_temperature}C")
        print(f"Average Mean Humidity: {average_min_humidity}%")
        print("\n")

    @staticmethod
    def print_chart(weather_dictionary):
        RED = "\033[91m"
        BLUE = "\033[94m"
        reset = "\033[0m"
        
        for date, read_data in weather_dictionary.items():
            day = date.split("-")[2] if "-" in date else date
            
            max_bars = '+' * read_data.max_temperature
            print(f"{reset}{day}: {RED}{max_bars} {read_data.max_temperature}C{reset}")
            
            min_bars = '-' * read_data.min_temperature
            print(f"{reset}{day}: {BLUE}{min_bars} {read_data.min_temperature}C{reset}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("folder")
    parser.add_argument("-e", "--extreme")
    parser.add_argument("-a", "--average")
    parser.add_argument("-c", "--chart")
    args = parser.parse_args()
    
    reader = WeatherReader()
    calculator = Weathercalculator()

    if args.extreme:
        weather_data = reader.get_weather_data(args.folder, args.extreme)
        if weather_data: 
            high, low, max_hum = calculator.get_extreme_values(weather_data)
            WeatherReportGenerator.print_extreme_temperature(high, low, max_hum)

    if args.average:
        y, m = args.average.split('/')
        weather_data = reader.get_weather_data(args.folder, y, m)
        if weather_data: 
            average_max_temperature, average_min_temperature, average_min_humidity = calculator.get_average_valuess(weather_data)
            WeatherReportGenerator.print_average_temperature(average_max_temperature, average_min_temperature, average_min_humidity)

    if args.chart:
        y, m = args.chart.split('/')
        weather_data = reader.get_weather_data(args.folder, y, m)
        if weather_data: 
            WeatherReportGenerator.print_chart(weather_data)



main()