import pandas
import matplotlib.pyplot as plt

data = pandas.read_csv("Crime_Data_2010_2017.csv")
data.boxplot(column='Victim Age', by='Victim Sex', rot=90)

plt.savefig('Age_varies_by_sex.png')
plt.show()
