import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load 2 csv files for analysis
cuisine_data_path = 'filtered_restaurants_without_cuisine_types.csv'
cuisine_data = pd.read_csv(cuisine_data_path)

df_income = pd.read_csv('census_income_data_acs_boston_cleaned_combined_reordered.csv')

# Analysis #1: Count restaurants in each zip code per cuisine category
restaurant_count = cuisine_data.groupby(['Zip Code', 'Cuisine Category']).size().reset_index(name='Count')
output_file_path = 'restaurant_count.csv'
restaurant_count.to_csv(output_file_path, index=False)

# Visualization #1: Box plot showing the distribution of cuisine diversity
cuisine_diversity = cuisine_data.groupby('Zip Code')['Cuisine Category'].nunique().reset_index()
cuisine_diversity.rename(columns={'Cuisine Category': 'Cuisine Diversity'}, inplace=True)

plt.figure(figsize=(12, 6))
sns.boxplot(x=cuisine_diversity['Cuisine Diversity'])
plt.title('Distribution of Cuisine Diversity Across Zip Codes')
plt.xlabel('Number of Unique Cuisine Types')
plt.ylabel('Frequency')
plt.show()

# Visualization #2: Scatterplot showing correlation between income and cuisine types
# Load restaurant_count file
df_restaurant = pd.read_csv('restaurant_count.csv')
df_cuisine_count = df_restaurant.groupby('Zip Code').agg({'Cuisine Category': 'nunique'}).reset_index()
df_cuisine_count.rename(columns={'Cuisine Category': 'Number of Cuisine Types'}, inplace=True)

income_columns = df_income.columns[1:]
weights = {col: i+1 for i, col in enumerate(income_columns)}

df_income['Income Score'] = sum(df_income[col] * weight for col, weight in weights.items())
df_income['Total Households'] = df_income[income_columns].sum(axis=1)
df_income['Income Level'] = df_income['Income Score'] / df_income['Total Households']

df_income_final = df_income[['Zip Code', 'Income Level']].copy()

# Merging the datasets
df_final_merged = pd.merge(df_cuisine_count, df_income_final, on='Zip Code', how='inner')

correlation = df_final_merged.corr()


# Draw scatterplot with a fitted line
plt.figure(figsize=(10, 6))
sns.regplot(data=df_final_merged, x='Income Level', y='Number of Cuisine Types', scatter_kws={'s':50})
plt.title('Correlation with Fitted Line: Income Level vs. Number of Cuisine Types in Boston Zip Codes')
plt.xlabel('Income Level')
plt.ylabel('Number of Cuisine Types')
plt.grid(True)
plt.show()

# Visualization #3: Bar charts to further analyze areas with low and high cuisine diversity

# Check if outliers (areas of low or high cuisine diversity) exist
Q1 = cuisine_diversity['Cuisine Diversity'].quantile(0.25)
Q3 = cuisine_diversity['Cuisine Diversity'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR

# Function to determine the predominant income bracket for each zip code
def predominant_income_bracket(row):
    income_brackets = row.index[1:]  # Excluding 'Zip Code'
    max_value = row[1:].max()
    predominant_bracket = income_brackets[row[1:] == max_value].tolist()
    return ', '.join(predominant_bracket)

# Apply the function to determine the predominant income bracket for each zip code
df_income['Predominant Income Bracket'] = df_income.apply(predominant_income_bracket, axis=1)

merged_data_with_brackets = pd.merge(cuisine_diversity, df_income[['Zip Code', 'Predominant Income Bracket']], on='Zip Code')

below_Q1_with_brackets = merged_data_with_brackets[merged_data_with_brackets['Cuisine Diversity'] < Q1]
above_Q3_with_brackets = merged_data_with_brackets[merged_data_with_brackets['Cuisine Diversity'] > Q3]

# Bar Chart No.1: most prevalent cuisine types among zip codes below Q1
zip_codes_below_Q1 = below_Q1_with_brackets['Zip Code']
cuisine_data_below_Q1 = cuisine_data[cuisine_data['Zip Code'].isin(zip_codes_below_Q1)]
cuisine_count_below_Q1 = cuisine_data_below_Q1['Cuisine Category'].value_counts().reset_index()
cuisine_count_below_Q1.columns = ['Cuisine Type', 'Frequency']

plt.figure(figsize=(12, 6))
sns.barplot(x='Frequency', y='Cuisine Type', data=cuisine_count_below_Q1.head(10))  # Top 10 cuisine types
plt.title('Most Prevalent Cuisine Types in Zip Codes Below Q1 for Cuisine Diversity')
plt.xlabel('Frequency')
plt.ylabel('Cuisine Type')
plt.show()

# Bar Chart NO.2: most prevalent cuisine types among zip codes above Q3
zip_codes_above_Q3 = above_Q3_with_brackets['Zip Code']
cuisine_data_above_Q3 = cuisine_data[cuisine_data['Zip Code'].isin(zip_codes_above_Q3)]
cuisine_count_above_Q3 = cuisine_data_above_Q3['Cuisine Category'].value_counts().reset_index()
cuisine_count_above_Q3.columns = ['Cuisine Type', 'Frequency']

plt.figure(figsize=(12, 6))
sns.barplot(x='Frequency', y='Cuisine Type', data=cuisine_count_above_Q3.head(10))  # Top 10 cuisine types
plt.title('Most Prevalent Cuisine Types in Zip Codes Above Q3 for Cuisine Diversity')
plt.xlabel('Frequency')
plt.ylabel('Cuisine Type')
plt.show()

