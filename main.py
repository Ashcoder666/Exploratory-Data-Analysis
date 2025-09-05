import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(url)

print(df.info())
print(df.describe())

#Handling missing values

df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

#Remove duplicates

df = df.drop_duplicates()

#Filter firstclass passengers

first_class = df[df["Pclass"] == 1]

#drop incomplete column for data clarity

df = df.drop("Cabin",axis=1)

print(df.info())


#Bar chart : Survival Rate by Class

survival_by_class = df.groupby("Pclass")["Survived"].mean()
survival_by_class.plot(kind="bar",color="skyblue")
plt.title("Survival Rate by Class")
plt.ylabel("Survival Rate")
plt.show()


#Histogram to show : Age Distribution

sns.histplot(df["Age"], kde=True , bins=20 , color="purple")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

#Scatter Plot : Age vs Fare

plt.scatter(df["Age"],df["Fare"] , alpha=0.5 , color = "green")
plt.title("Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()

