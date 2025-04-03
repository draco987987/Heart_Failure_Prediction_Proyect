import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
file_path = "C:\\Users\\organ\\Desktop\\Code institute\\python\\test2-code-institute\\Hearth_Proyect\\Heart_Failure_Prediction_Proyect\\Dataset\\Raw\\Heart_failure_prediction.csv"
df = pd.read_csv(file_path)
print(df.head(5))
print(df.info())


df.drop_duplicates(inplace = True) #eliminate duplicates
df.dropna(inplace = True) #eliminate NaN values
columns_to_drop = ["Chest_Pain_Type", "Resting_ECG", "Exercise_Induced_Angina", "Slope", "Thalassemia"] #Make a list of columns to drop
df.drop(columns = columns_to_drop, inplace = True) #eliminate columns that are not useful for the analysis
print(df.columns) #show the columns of the dataframe


df["Gender"] = df["Gender"].map({"Male": 1, "Female": 0}) #convert categorical to numerical
df["Smoking"] = df["Smoking_History"].map(lambda x: 1 if x in ["Former", "Current"] else 0) #convert categorical to numerical
df["Alcohol_consumption"] = df["Alcohol_Consumption"].map({"None": 0, "Moderate": 1, "Heavy": 2}) #convert categorical to numerical
df["Physical_Activity_Level"] = df["Physical_Activity_Level"].map({"Low": 1, "Moderate": 2, "High": 3}) #convert categorical to numerical
print(df.dtypes) #check the data types of the columns


df.to_csv("Dataset/Cleaned/clean_Heart_data.csv", index = False) #save the cleaned data to a new csv file
df = pd.read_csv("Dataset/Cleaned/clean_Heart_data.csv") #read the cleaned data
print(df.head(5)) #show the first 5 rows of the cleaned data
print(df.info()) #show the info of the cleaned data

# Boxplot de colesterol por género
plt.figure(figsize=(8, 5))
sns.boxplot(x="Gender", y="Cholesterol", data=df, palette=["blue", "pink"])
plt.xticks(ticks=[0, 1], labels=["Masculino", "Femenino"])
plt.xlabel("Género")
plt.ylabel("Colesterol")
plt.title("Distribución del Colesterol por Género")
plt.tight_layout()
plt.show()