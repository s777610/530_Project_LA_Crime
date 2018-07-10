import pandas
import matplotlib.pyplot as plt


data = pandas.read_csv("Crime_Data_2010_2017.csv")
number_of_crime_0704 = {}

for x in range(2010, 2017):
    data_that_date = data[data["Date Occurred"].str.contains(f'07/04/{x}')]
    Location = list(data_that_date["Location "])
    number_of_crime_0704[x] = len(Location)
print(number_of_crime_0704)


plt.plot(number_of_crime_0704.keys(), number_of_crime_0704.values())
x_lab = 'Independence Day of Year'
y_lab = 'Number of Crimes'
title = 'The relationship between years and criminal activities'
plt.xlabel(x_lab)
plt.ylabel(y_lab)
plt.title(title)
plt.savefig('Independence_Day.png')
plt.show()