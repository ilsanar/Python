# with open("weather_data.csv") as csv_file:
#     data = csv_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1].isnumeric():
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas as pd


# data = pd.read_csv("weather_data.csv")
# print(data)
# print("\n" * 5)
# print(type(data["temp"]))
# print(type(data))
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)

# avg = data["temp"].describe()
# print(avg)

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# ftemp = monday.temp[0] * 9 / 5 + 32
# print(ftemp)

#
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pd.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

dataset = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(dataset.columns)

new_data = dataset.groupby(by=["Primary Fur Color"]).size().reset_index(name="Count")
print(new_data)
new_data.to_csv("Squirrel_Summary.csv")
