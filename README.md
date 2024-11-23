
#HR_Employee Attrition Analysis Project

## Overview

This project analyzes employee attrition data to uncover insights about employee turnover patterns. Using the dataset stored at `C:/users/kasutaja/downloads/WA_Fn-UseC_-HR-Employee-Attrition.csv`, various analyses and visualizations have been conducted to explore attrition rates, department-wise breakdowns, and correlations with factors like age and monthly income.

## Features

### Data Analysis
1. **Dataset Summary**:
   - Displays basic statistics for numerical columns.
   - Checks for missing values in the dataset.

2. **Attrition Rate Analysis**:
   - Overall attrition rate (percentage of employees who left).
   - Attrition breakdown by department and job role.

### Data Visualization
1. **Attrition Rate by Department**:
   - Stacked bar chart showing attrition percentages (Yes/No) for each department.

2. **Attrition Rate by Job Role**:
   - Stacked bar chart highlighting attrition percentages for various job roles.

3. **Impact of Age on Attrition**:
   - Boxplot showing age distributions for employees who stayed vs. those who left.

4. **Correlation between Attrition and Monthly Income**:
   - Boxplot depicting the relationship between monthly income and attrition status.
   - Median monthly income calculated for each attrition group.

### Technologies Used
- **Python**:
  - Libraries: `pandas`, `matplotlib`, `seaborn`
- **Data Source**:
  - IBM HR Analytics Employee Attrition dataset.

## How to Run

1. **Setup**:
   - Ensure Python is installed on your system.
   - Install required libraries using:
     ```bash
     pip install pandas matplotlib seaborn
     ```

2. **Run the Script**:
   - Save the script to a `.py` file and run it in your Python environment.
   - Ensure the dataset is located at `C:/users/kasutaja/downloads/WA_Fn-UseC_-HR-Employee-Attrition.csv`.

3. **Output**:
   - Summary statistics and missing values check are printed in the console.
   - Attrition rates are displayed, and visualizations are rendered for better understanding.

## Key Results

1. **Overall Attrition Rate**:
   - Displays the percentage of employees who left and stayed.

2. **Attrition by Department**:
   - Highlights departments with the highest attrition rates.

3. **Attrition by Job Role**:
   - Reveals job roles most affected by attrition.

4. **Age and Monthly Income Correlations**:
   - Shows how age and salary levels relate to attrition status.

## Future Work

- Add predictive modeling to forecast attrition likelihood.
- Perform deeper statistical analysis on other factors (e.g., job satisfaction, work-life balance).
- Automate report generation with BI tools like Tableau or Power BI.

