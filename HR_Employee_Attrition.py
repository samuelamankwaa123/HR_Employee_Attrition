import pandas as pd

# Define the path to the dataset
file_path = "C:/users/kasutaja/downloads/WA_Fn-UseC_-HR-Employee-Attrition.csv"

# Load the dataset into a DataFrame
data = pd.read_csv(file_path)

# Display the first few rows to confirm it loaded correctly
print(data.head())

# Summary statistics for numerical columns
numerical_summary = data.describe()

# Checking missing values for all columns
missing_values = data.isnull().sum()

# Displaying the results
print("Numerical Summary of the Dataset:")
print(numerical_summary)

print("\nMissing Values Check:")
print(missing_values)

#Attrition rate analysis
# Calculate overall attrition rate
attrition_rate = data['Attrition'].value_counts(normalize=True) * 100
print("Overall Attrition Rate:")
print(attrition_rate)

# Breakdown attrition by department
attrition_by_department = data.groupby('Department')['Attrition'].value_counts(normalize=True).unstack() * 100
print("\nAttrition Rate by Department:")
print(attrition_by_department)

import matplotlib.pyplot as plt

# Calculate attrition rate by department
attrition_by_department = data.groupby('Department')['Attrition'].value_counts(normalize=True).unstack() * 100

# Plotting attrition rate by department
attrition_by_department.plot(kind='bar', figsize=(10, 6), stacked=True, color=['skyblue', 'orange'])
plt.title('Attrition Rate by Department', fontsize=16)
plt.ylabel('Percentage', fontsize=12)
plt.xlabel('Department', fontsize=12)
plt.xticks(rotation=0, fontsize=10)
plt.legend(title="Attrition", labels=['No', 'Yes'], fontsize=10)
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt

# Calculate attrition rate by job role
attrition_by_job_role = data.groupby('JobRole')['Attrition'].value_counts(normalize=True).unstack() * 100

# Plotting attrition rate by job role
attrition_by_job_role.plot(kind='bar', figsize=(12, 6), stacked=True, color=['skyblue', 'orange'])
plt.title('Attrition Rate by Job Role', fontsize=16)
plt.ylabel('Percentage', fontsize=12)
plt.xlabel('Job Role', fontsize=12)
plt.xticks(rotation=45, fontsize=10, ha='right')
plt.legend(title="Attrition", labels=['No', 'Yes'], fontsize=10)
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

# Create a boxplot to analyze age impact on attrition
plt.figure(figsize=(10, 6))
sns.boxplot(x='Attrition', y='Age', data=data, palette='pastel')
plt.title('Impact of Age on Attrition', fontsize=16)
plt.xlabel('Attrition', fontsize=12)
plt.ylabel('Age', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

# Create a boxplot to visualize salary distribution by attrition status
plt.figure(figsize=(10, 6))
sns.boxplot(x='Attrition', y='MonthlyIncome', data=data, palette='pastel')
plt.title('Correlation between Attrition and Monthly Income', fontsize=16)
plt.xlabel('Attrition', fontsize=12)
plt.ylabel('Monthly Income', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()
plt.show()

# Calculate and display median income for each attrition group
median_income = data.groupby('Attrition')['MonthlyIncome'].median()
print("Median Monthly Income by Attrition Status:")
print(median_income)


