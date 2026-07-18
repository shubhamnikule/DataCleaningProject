
# Data Cleaning and Visualization Project
# Using Pandas and Matplotlib


# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt


# Step 1: Load CSV Dataset

# Read CSV file
df = pd.read_csv("sales_data.csv")

print("Original Dataset:")
print(df)


# Step 2: Handle Missing Values

print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing Price with average price
df["Price"] = df["Price"].fillna(df["Price"].mean())

# Fill missing Quantity with average quantity
df["Quantity"] = df["Quantity"].fillna(df["Quantity"].mean())

# Step 3: Remove Duplicate Rows

print("\nDuplicate Rows:", df.duplicated().sum())

df = df.drop_duplicates()

# ------------------------------------------
# Step 4: Detect and Remove Outliers
# Using IQR Method
# ------------------------------------------

Q1 = df["Sales"].quantile(0.25)
Q3 = df["Sales"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

# Remove outliers
df = df[(df["Sales"] >= lower) & (df["Sales"] <= upper)]

# ------------------------------------------
# Step 5: Summary Statistics
# ------------------------------------------

print("\nSummary Statistics:")
print(df.describe())

# ------------------------------------------
# Step 6: Data Visualization
# ------------------------------------------

# Chart 1 - Bar Chart
category_sales = df.groupby("Category")["Sales"].sum()
plt.figure(figsize=(8,5))
category_sales.plot(kind="bar")

plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.xticks(rotation=0)   
plt.tight_layout()       

plt.grid(True)
plt.show()

# ------------------------------------------

# Chart 2 - Pie Chart
plt.figure(figsize=(6,6))
category_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Sales Distribution")
plt.ylabel("")
plt.show()

# ------------------------------------------

# Chart 3 - Histogram
plt.figure(figsize=(6,4))
plt.hist(df["Sales"], bins=5)
plt.title("Sales Distribution Histogram")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()

# ------------------------------------------

# Chart 4 - Scatter Plot
plt.figure(figsize=(6,4))
plt.scatter(df["Price"], df["Sales"])
plt.title("Price vs Sales")
plt.xlabel("Price")
plt.ylabel("Sales")
plt.show()

# ------------------------------------------

# Chart 5 - Line Chart
plt.figure(figsize=(8,4))
plt.plot(df["Product"], df["Sales"], marker="o")
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# ------------------------------------------
# Final Cleaned Dataset
# ------------------------------------------

print("\nCleaned Dataset:")
print(df)

# Save cleaned data to a new CSV file
df.to_csv("cleaned_sales_data.csv", index=False)

print("\nCleaned data saved successfully!")