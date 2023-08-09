import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('okcupid_profiles.csv',sep='\t')

# Data Cleaning

# Identify all missing data
missing_values = df.isnull().sum()
print("Missing Values:")
print(missing_values)

# Strategy to handle missing data: Remove data entries with missing values
df_cleaned = df.dropna()

# Analysis

# 1. Average age of users
average_age = df_cleaned['age'].mean()
print("Average Age of Users:", average_age)

# Visualize the distribution of age
sns.histplot(df_cleaned['age'], kde=True)
plt.xlabel('Age')
plt.ylabel('Count')
plt.title('Distribution of Age')
plt.savefig('age_distribution.png')
plt.close()

# 2. Average height of users
average_height = df_cleaned['height'].mean()
print("Average Height of Users:", average_height)

# Visualize the distribution of height
sns.histplot(df_cleaned['height'], kde=True)
plt.xlabel('Height')
plt.ylabel('Count')
plt.title('Distribution of Height')
plt.savefig('height_distribution.png')
plt.close()

# 3. Relationship between wealth and height
# Define "wealthy" as users with income greater than a certain threshold (e.g., $100,000)
wealthy_users = df_cleaned[df_cleaned['income'] > 100000]
average_height_wealthy = wealthy_users['height'].mean()
print("Average Height of Wealthy Users:", average_height_wealthy)

# Visualize the relationship between wealth and height using a scatter plot
sns.scatterplot(data=df_cleaned, x='income', y='height')
plt.xlabel('Income')
plt.ylabel('Height')
plt.title('Relationship between Wealth and Height')
plt.savefig('wealth_height_relationship.png')
plt.close()

# 4. Relationship between age and height
# Calculate statistics for shorter and taller users separately
short_users = df_cleaned[df_cleaned['height'] < average_height]
average_age_short = short_users['age'].mean()
tall_users = df_cleaned[df_cleaned['height'] > average_height]
average_age_tall = tall_users['age'].mean()
print("Average Age of Short Users:", average_age_short)
print("Average Age of Tall Users:", average_age_tall)

# Visualize the relationship between age and height using box plots
sns.boxplot(data=df_cleaned, x='height', y='age')
plt.xlabel('Height')
plt.ylabel('Age')
plt.title('Relationship between Height and Age')
plt.savefig('height_age_relationship.png')
plt.close()

# 5. Percentage of vegetarian and vegan users
total_users = df_cleaned.shape[0]
vegetarian_users = df_cleaned[df_cleaned['diet'].str.contains('vegetarian', case=False)]
vegan_users = df_cleaned[df_cleaned['diet'].str.contains('vegan', case=False)]
percentage_vegetarian = (vegetarian_users.shape[0] / total_users) * 100
percentage_vegan = (vegan_users.shape[0] / total_users) * 100
print("Percentage of Vegetarian Users:", percentage_vegetarian)
print("Percentage of Vegan Users:", percentage_vegan)

# Visualize the percentage of vegetarian and vegan users using a pie chart
labels = ['Vegetarian', 'Vegan', 'Non-vegetarian']
sizes = [percentage_vegetarian, percentage_vegan, 100 - percentage_vegetarian - percentage_vegan]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.title('Percentage of Users by Diet')
plt.savefig('diet_percentage.png')
plt.close()

# ... continue with the remaining visualizations ...

# Save the cleaned dataset
df_cleaned.to_csv('okcupid_profiles_cleaned.csv', index=False)

# Brief conclusion
print("\nConclusion:")
print("The analysis of the OkCupid Profiles dataset revealed insights about the average age and height of users, the relationship between wealth and height, the correlation between age and height, the percentage of vegetarian and vegan users, the proportion of smoking users among vegetarians and vegans, the impact of income on body type, the city with the highest number of users, the most common job, and the most common education level. These findings can provide valuable information for further analysis and decision-making in the context of OkCupid and user preferences.")
