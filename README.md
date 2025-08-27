# 🚢 Exploratory Data Analysis (EDA) - Titanic Dataset

This project performs Exploratory Data Analysis (EDA) on the famous Titanic dataset to uncover insights about passenger demographics, survival rates, and key factors that influenced survival during the disaster.

📂 Dataset

The dataset used is the Titanic dataset from Kaggle
 (train.csv). It contains passenger details such as:

PassengerId

Name, Sex, Age

Pclass (Ticket class)

SibSp (No. of siblings/spouses aboard)

Parch (No. of parents/children aboard)

Ticket, Fare, Cabin

Embarked (Port of Embarkation)

Survival (Target variable: 0 = No, 1 = Yes)

🎯 Objectives

The main goals of this project are:

Perform data cleaning (handling missing values, data types, duplicates).

Conduct descriptive statistics to summarize key features.

Use visualizations to understand trends and distributions.

Identify patterns & correlations that influenced survival.

📊 Key Steps in EDA

Data Cleaning

Handle missing values (Age, Cabin, Embarked).

Convert categorical variables into meaningful values.

Univariate Analysis

Distribution of Age, Fare, and other numerical columns.

Count plots for categorical variables (Sex, Pclass, Embarked).

Bivariate & Multivariate Analysis

Survival rates by gender, age groups, passenger class.

Correlation heatmap for numerical features.

Interaction between family size (SibSp + Parch) and survival.

Visualization Tools Used

Matplotlib

Seaborn

Pandas built-in visualization

📌 Insights

Females had a much higher survival rate than males.

Higher-class passengers (Pclass 1) had better chances of survival.

Children (Age < 10) had a higher chance of survival.

Passengers traveling with family showed slightly better survival odds compared to those traveling alone.

🛠️ Tech Stack

Python

Jupyter Notebook

Libraries: pandas, numpy, matplotlib, seaborn
