# This code is written in python
# The pandas library is used for data processing and to read data files
import pandas as pd 
#The matplotlib library is used to plot histograms and scatter plots
import matplotlib.pyplot as plt

# The GWCutilities has functions to help format data printed to the console
import GWCutilities as util

# Read a comma separated values (CSV) files into a variable
# as a pandas DataFrame
lwd=pd.read_csv("Empowering-Data-Final-Project-EmmaH/livwell175.csv")

# Print out the number of rows and columns
#print(lwd.shape)

#  basic colors:
# 'blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'white'

print("In the Philippines and Indonesia, two Southeast Asian countries, women have had varying levels of education throughout the years.\n")
print("Similar to the US, Indonesia and the Philippines both require 12 years of education for children, though the change in the Philippines from 10 to 12 years was only made in 2016.\n")
input("Press enter to continue.\n")
print("Although there has been improvement in the past few years, many women in both countries do not recieve the full 12 years of education.\n")
print("For one, Indonesia is a majority Muslim nation and the Philippines is a majority Catholic nation. These religions often advocate for gender equality, but there is frequently inequality in practice.\n")
input("Press enter to continue.\n")
print("In both Indonesia and the Philippines, women are still expected to follow the traditional role of being a mother and homemaker. These expectations can stifle the dreams of young girls with big aspirations, affecting their ability to learn and work.\n")
input("Press enter to visualize data.\n")

countryOneBooleanList = lwd["country_name"] == "Indonesia"
countryOneData = lwd.loc[countryOneBooleanList]
countryTwoBooleanList = lwd["country_name"] == "Philippines"
countryTwoData = lwd.loc[countryTwoBooleanList]

print("Click the X to view the next plot.\n")

#time and lit rate
plt.scatter(x="year",y="ED_litt_p",data=countryOneData, color = "red")
plt.scatter(x="year",y="ED_litt_p",data=countryTwoData, color = "blue")
plt.title("Literacy Rate Over Time")
plt.xlabel("Years")
plt.ylabel("Women who are literate (%)")
plt.legend(["Indonesia", "Philippines"])
plt.show()

print("Click the X to view the next plot.\n")

#time and avg schooling
plt.scatter(x="year",y="ED_educ_years_mean",data=countryOneData, color = "red")
plt.scatter(x="year",y="ED_educ_years_mean",data=countryTwoData, color = "blue")
plt.title("Average Years of Schooling Over Time")
plt.xlabel("Years")
plt.ylabel("Female average/median years of schooling")
plt.legend(["Indonesia", "Philippines"])
plt.show()

print("Click the X to view the next plot.\n")

#avg schooling and lit rate
plt.scatter(x="ED_educ_years_mean",y="ED_litt_p",data=countryOneData, color = "red")
plt.scatter(x="ED_educ_years_mean",y="ED_litt_p",data=countryTwoData, color = "blue")
plt.title("Literacy Rate Compared to Average Years of Schooling")
plt.xlabel("Female average/median years of schooling")
plt.ylabel("Women who are literate (%)")
plt.legend(["Indonesia", "Philippines"])
plt.show()

print("Click the X to view the research question.\n")

#avg schooling and percent working
plt.scatter(x="ED_educ_years_mean",y="WK_working_p",data=countryOneData, color = "red")
plt.scatter(x="ED_educ_years_mean",y="WK_working_p",data=countryTwoData, color = "blue")
plt.title("Average Years of Schooling Compared to Percentage of Women Currently Working")
plt.xlabel("Female average/median years of schooling")
plt.ylabel("Women currently working (%)")
plt.legend(["Indonesia", "Philippines"])
plt.show()

print("The patterns in the data pose an interesting question: How do increased years of education for women affect literacy rates and how much women work in Southeast Asia? Why does it not have a clear/direct positive correlation?\n")
print("We ask that you allocate some money and resources to explore these questions. This could help thousands of young girls in Southeast Asia to achieve their dreams and enjoy a successful career.")