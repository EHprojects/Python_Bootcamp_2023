# with open("weather_data.csv") as file:
#     data = file.readlines()
#
# print(data)

# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
# print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()

# total = sum(temp_list)
# avg = total / len(temp_list)

# avg_temp = data["temp"].mean()
# print(avg_temp)
#
# max_temp = data["temp"].max()
# print(max_temp)
#
# print(data.condition)

# print(data[data["day"] == "Monday"])
# print(data[data["temp"] == data["temp"].max()])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print((monday.temp * 9 / 5) + 32)

# Create a dataframe
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data_df = pandas.DataFrame(data_dict)
data_df.to_csv("new_data.csv")
