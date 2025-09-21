# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Load and Explore the Dataset
try:
    # Load dataset CSV file
    df = pd.read_csv('Used_Car_Price_Prediction.csv') 
    
    # Display first 5 rows
    print("First 5 rows of the dataset:")
    print(df.head())
    
    # Show data types and check for missing values
    print("\nData types and missing values:")
    print(df.info())
    print(df.isnull().sum())
    
    # Clean dataset by dropping rows with missing values
    df_clean = df.dropna()  
    
    print(f"\nAfter cleaning, dataset has {len(df_clean)} rows.")
except FileNotFoundError:
    print("Error: Dataset file not found.")
except Exception as e:
    print(f"An error occurred: {e}")

# Task 2: Basic Data Analysis
print("\nBasic statistical description:")
print(df_clean.describe())


grouped = df_clean.groupby('car_name')['yr_mfr'].mean() 
print("\nMean values by category:")
print(grouped)

# Task 3: Data Visualization

plt.figure(figsize=(10, 6))
plt.plot(df_clean['yr_mfr'], df_clean['sale_price'])
plt.title('Line Chart: Trend Over Time')
plt.xlabel('Time')
plt.ylabel('Value')
plt.show()

# Bar chart example
plt.figure(figsize=(10, 6))
grouped.plot(kind='bar')
plt.title('Bar Chart: Average Value by Category')
plt.xlabel('Category')
plt.ylabel('Average Value')
plt.show()

# Histogram example
plt.figure(figsize=(10, 6))
df_clean['numerical_column'].hist(bins=20)
plt.title('Histogram: Distribution of Numerical Column')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# Scatter plot example
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_clean, x='numerical_column1', y='numerical_column2')
plt.title('Scatter Plot: Relation between Numerical Column 1 and 2')
plt.xlabel('Numerical Column 1')
plt.ylabel('Numerical Column 2')
plt.show()
