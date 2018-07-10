import pandas
import matplotlib.pyplot as plt


data = pandas.read_csv("src/Crime_Data_2010_2017.csv")
print(data.columns)
print(data.info())
print(data.shape)  # (1584316, 26)
print(data.describe())


# Plot the histogram
data['Victim Age'].plot(kind='hist')

x_lab = 'Range of age'
y_lab = 'Number of crime'
title = 'This is title'
plt.xlabel(x_lab)
plt.ylabel(y_lab)
plt.title("Distribution of Crime")
#plt.savefig('Distribution_of_Crime.png')
plt.show()






