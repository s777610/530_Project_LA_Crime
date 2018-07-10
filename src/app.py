
import pandas
import matplotlib.pyplot as plt
import numpy as np


data = pandas.read_csv("Crime_Data_2010_2017.csv")
print(data.columns)
print(data.info())
print(data.shape)  # (1584316, 26)
print(data.describe())

# Print the value counts for 'Victim Sex'
# print(data['Victim Sex'].value_counts(dropna=False))

#data_occurred = data["Date Occurred"]
#index_data2017 = data_occurred == '2017'
#data_2017 = data[index_data2017]

#data_2017 = data[data["Date Occurred"][-4:] == "2017"]

data_2017_1225 = data[data["Date Occurred"].str.contains('12/25/2017')]

data_2017_1225["Time Occurred"] = data_2017_1225["Time Occurred"].astype(int)
print(type(data_2017_1225["Time Occurred"]))

data_2017_1225.plot(kind="scatter", x='Time Occurred', y='Victim Age', rot=70)
plt.show()

#print(type(data["Date Occurred"][0]))
#print(data["Date Occurred"][0][-4:])

x_lab = 'Range of age'
y_lab = 'Number of crime'
title = 'This is title'
#plt.xlabel(x_lab)
#plt.ylabel(y_lab)
#plt.title("Distribution of Crime")
# plt.savefig('Distribution_of_Crime.png')
# plt.show()

'''
Date_occured = list(data["Date Occurred"])
Time_Occurred = list(data["Time Occurred"])
Victim_age = list(data["Victim Age"])
Victim_Sex = list(data["Victim Sex"])
Address = list(data["Address"])
Area_name = list(data["Area Name"])

victim_sex = data["Victim Sex"]
vic_is_M = victim_sex == "M"
vic_is_F = victim_sex == "F"
df_victim_M = data[vic_is_M]
df_victim_F = data[vic_is_F]

df_Vic = data[np.logical_and(data["column"] < 500, data["column"] > 100)]
data["column"] = data["column"].apply(str.upper)

victim_age = data["Victim Age"]
vic_age_no_NaN = victim_age is not "NaN"
df_vic_age = data[vic_age_no_NaN]
print(type(df_vic_age))
print(df_vic_age.head())



# Location = list(data["Location "])

# plt.plot(x, y)
# plt.scatter(Victim_age[0:5000], Time_Occurred[0:5000])
#plt.hist(df_victim_M["Victim Age"])
#plt.show()

'''
'''
x_lab = 'This is X'
y_lab = 'This is Y'
title = 'This is title'
plt.xlabel(x_lab)
plt.ylabel(y_lab)
plt.title(title)
plt.show()
'''