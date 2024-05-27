#Methods one to take the temperature number
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

#methods two
import pandas
data = pandas.read_csv("weather_data.csv")
#pandas by default take the row number one and read like column for the other rows
print(data["temp"])

#read like dictionnary
data_dict = data.to_dict()
#print(data_dict)
#read the series temp like list
temp_list = data["temp"].to_list

print(data["temp"].max())

#Get Data in Columns
print(data["condition"])
print(data.condition)

#Get data in Row
print(data[data.day == "Monday"])
print(data[data["temp"] == data["temp"].max()])

#Create a dataframe from scratch
data_dict = {
    "students" : ["Amy", "Naim", "mohamed"],
    "scores" : [50, 70, 100]
}

dataa= pandas.DataFrame(data_dict)
print(dataa)
data.to_csv("new_data.csv")


