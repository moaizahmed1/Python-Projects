path = input("Enter folder path: ")
option = input("Enter option (a / b / c): ")

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

month_names = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

# FOr Yearly Report
if option == "a":

    year = input("Enter year: ")

    highest_temp = -999
    lowest_temp = 999
    highest_humidity = -999

    highest_day = ""
    lowest_day = ""
    humidity_day = ""

    for month in months:

        file_name = path + "/Murree_weather_" + year + "_" + month + ".txt"

        try:
            file = open(file_name, "r")

            for line in file.readlines()[1:]:

                data = line.strip().split(",")

                if len(data) > 8:

                    date = data[0]
                    day = date.split("-")[2]

                    if data[1] != "":
                        max_temp = int(data[1])

                        if max_temp > highest_temp:
                            highest_temp = max_temp
                            highest_day = month_names[month] + " " + day

                    if data[3] != "":
                        min_temp = int(data[3])

                        if min_temp < lowest_temp:
                            lowest_temp = min_temp
                            lowest_day = month_names[month] + " " + day

                    if data[8] != "":
                        humidity = int(data[8])

                        if humidity > highest_humidity:
                            highest_humidity = humidity
                            humidity_day = month_names[month] + " " + day

            file.close()

        except FileNotFoundError:
            print("File not found:", file_name)

    print("Highest:", highest_temp, "C on", highest_day)
    print("Lowest:", lowest_temp, "C on", lowest_day)
    print("Humidity:", highest_humidity, "% on", humidity_day)

# Monthly Average Report
elif option == "b":

    date_input = input("Enter year/month (Example: 2005/6): ")

    parts = date_input.split("/")

    year = parts[0]
    month = int(parts[1])

    file_name = path + "/Murree_weather_" + year + "_" + months[month - 1] + ".txt"

    try:
        file = open(file_name, "r")

        total_max = 0
        total_min = 0
        total_humidity = 0

        count_max = 0
        count_min = 0
        count_humidity = 0

        for line in file.readlines()[1:]:

            data = line.strip().split(",")

            if len(data) > 8:

                if data[1] != "":
                    total_max += int(data[1])
                    count_max += 1

                if data[3] != "":
                    total_min += int(data[3])
                    count_min += 1

                if data[8] != "":
                    total_humidity += int(data[8])
                    count_humidity += 1

        print("Highest Average:", total_max // count_max, "C")
        print("Lowest Average:", total_min // count_min, "C")
        print("Average Mean Humidity:", total_humidity // count_humidity, "%")

        file.close()

    except FileNotFoundError:
        print("File not found")

# Temperature Chart
elif option == "c":

    date_input = input("Enter year/month (Example: 2011/03): ")

    parts = date_input.split("/")

    year = parts[0]
    month = int(parts[1])

    print(month_names[months[month - 1]], year)

    file_name = path + "/Murree_weather_" + year + "_" + months[month - 1] + ".txt"

    try:
        file = open(file_name, "r")

        for line in file.readlines()[1:]:

            data = line.strip().split(",")

            if len(data) > 3:

                day = data[0].split("-")[2]

                if data[1] != "":
                    max_temp = int(data[1])
                    print(day, "+" * max_temp, str(max_temp) + "C")

                if data[3] != "":
                    min_temp = int(data[3])
                    print(day, "+" * min_temp, str(min_temp) + "C")

        file.close()

    except FileNotFoundError:
        print("File not found")

else:
    print("Invalid option")