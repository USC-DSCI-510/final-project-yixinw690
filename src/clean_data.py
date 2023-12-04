import pandas as pd

# Clean Yelp Data, remove restaurants without cuisine types
csv_file_path = 'restaurants_in_boston.csv'
df = pd.read_csv(csv_file_path)

# List of expanded nationality-based keywords
nationality_keywords = [
    'american', 'thai', 'japanese', 'italian', 'mexican', 'indian', 'french', 'chinese', 'greek', 'spanish',
    'mediterranean', 'cuban', 'latin american', 'peruvian', 'cambodian', 'brazilian', 'polish', 'southern',
    'modern european', 'asian', 'korean', 'armenian', 'irish', 'caribbean', 'venezuelan', 'afghan', 'halal',
    'cantonese', 'african', 'somali', 'ethiopian', 'vietnamese', 'taiwanese', 'middle eastern', 'salvadoran',
    'scottish', 'malaysian', 'brazilian', 'himalayan', 'indian', 'szechuan', 'tacos', 'ramen', 'pan asian',
    'moroccan', 'eritrean', 'sushi', 'creperies', 'trinidadian', 'turkish', 'hawaiian', 'thai', 'indonesian',
    'singapore', 'poke', 'dim sum', 'izakaya', 'irish', 'kebab', 'shanghainese', 'middle eastern'
]

filtered_df = df[df['Cuisine Types'].str.lower().str.contains('|'.join(nationality_keywords))]

# Relabel restaurants' cuisine types
def assign_cuisine_category(row):
    cuisine_types = row['Cuisine Types'].lower()
    
    if 'fusion' in cuisine_types:
        return 'Fusion'
    elif 'irish' in cuisine_types:
        return 'Irish'
    elif 'french' in cuisine_types and 'italian' not in cuisine_types:
        return 'French'
    elif 'italian' in cuisine_types and 'french' not in cuisine_types and 'spanish' not in cuisine_types and 'latin american' not in cuisine_types:
        return 'Italian'
    elif 'greek' in cuisine_types:
        return 'Greek'
    elif 'spanish' in cuisine_types:
        return 'Spanish'
    elif 'mediterranean' in cuisine_types and 'greek' not in cuisine_types and 'french' not in cuisine_types and 'italian' not in cuisine_types:
        return 'Mediterranean'
    elif any(keyword in cuisine_types for keyword in ['african', 'ethiopian']):
        return 'African'
    elif any(keyword in cuisine_types for keyword in ['mexican', 'taco']):
        return 'Mexican'
    elif any(keyword in cuisine_types for keyword in ['latin american', 'cuban', 'brazilian','peruvian', 'caribbean']):
        return 'Other Latin American'
    elif 'thai' in cuisine_types:
        return 'Thai'
    elif 'vietnamese' in cuisine_types:
        return 'Vietnamese'
    elif any(keyword in cuisine_types for keyword in ['sushi', 'ramen', 'izakaya']):
        return 'Japanese' 
    elif 'japanese' in cuisine_types and cuisine_types.count(',') == 0:
        return 'Japanese' 
    elif 'japanese' in cuisine_types and any(keyword in cuisine_types for keyword in ['noodles', 'dessert','cocktail bars','specialty food', 'hot pot','poke']):
        return 'Japanese'
    elif 'korean' in cuisine_types:
        return 'Korean'
    elif any(keyword in cuisine_types for keyword in ['dim sum', 'cantonese', 'szechuan', 'shanghainese', 'hongkong', 'taiwanese']):
        return 'Chinese'
    elif 'chinese' in cuisine_types and 'seafood' in cuisine_types:
        return 'Chinese'
    elif 'chinese' in cuisine_types and 'noodles' in cuisine_types:
        return 'Chinese'
    elif 'chinese' in cuisine_types:
        return 'Chinese'
    elif any(keyword in cuisine_types for keyword in ['american', 'hawaiian', 'southern']):
        return 'American'
    elif any(keyword in cuisine_types for keyword in ['afghan', 'arabic', 'middle eastern', 'falafel', 'kebab']):
        return 'Middle Eastern'
    elif any(keyword in cuisine_types for keyword in ['indian', 'himalayan', 'cambodian','pan asian']):
        return 'Other Asian'
    else:
        return 'Other European'

df['Cuisine Category'] = df.apply(assign_cuisine_category, axis=1)

# List of valid zip codes
valid_zip_codes = [
    2203, 2116, 2124, 2132, 2199, 2110, 2113, 2122, 2125, 2128,
    2108, 2120, 2135, 2467, 2115, 2109, 2118, 2121, 2126, 2127,
    2129, 2163, 2114, 2119, 2130, 2131, 2134, 2136, 2210, 2215, 2111
]

# Filter DataFrame based on valid zip codes
df_filtered = df[df['Zip Code'].astype(int).isin(valid_zip_codes)]

# Drop the "Cuisine Types" column
df_filtered.drop(columns=['Cuisine Types'], inplace=True)

# Save the cleaned and relabeled data to a new CSV file
updated_csv_file_path = 'filtered_restaurants_without_cuisine_types.csv'
df_filtered.to_csv(updated_csv_file_path, index=False)

print(f"Updated data (without Cuisine Types) has been written to {updated_csv_file_path}")

#Reorganize income level data into 6 groups
file_path = 'census_income_data_acs_boston.csv'
df = pd.read_csv(file_path)

# Combine and sum the values for the specified income ranges
df['Income $10,000 to $24,999'] = df['Income $10,000 to $14,999'] + df['Income $15,000 to $24,999']
df['Income $25,000 to $49,999'] = df['Income $25,000 to $34,999'] + df['Income $35,000 to $49,999']
df['Income $50,000 to $99,999'] = df['Income $50,000 to $74,999'] + df['Income $75,000 to $99,999']
df['Income $100,000 to $199,999'] = df['Income $100,000 to $149,999'] + df['Income $150,000 to $199,999']

df = df.drop(['Income $10,000 to $14,999', 'Income $15,000 to $24,999',
              'Income $25,000 to $34,999', 'Income $35,000 to $49,999',
              'Income $50,000 to $74,999', 'Income $75,000 to $99,999',
              'Income $100,000 to $149,999', 'Income $150,000 to $199,999', 'state'], axis=1)

# Reorder the columns
new_order = ['zip code tabulation area', 'Income less than $10,000',
             'Income $10,000 to $24,999', 'Income $25,000 to $49,999',
             'Income $50,000 to $99,999', 'Income $100,000 to $199,999',
             'Income $200,000 or more']
df = df[new_order]

# Rename the combined columns
df = df.rename(columns={'zip code tabulation area': 'Zip Code',
                        'Income $10,000 to $24,999': 'Income $10,000 to $24,999',
                        'Income $25,000 to $49,999': 'Income $25,000 to $49,999',
                        'Income $50,000 to $99,999': 'Income $50,000 to $99,999',
                        'Income $100,000 to $199,999': 'Income $100,000 to $199,999'})

df.to_csv('census_income_data_acs_boston_cleaned_combined_reordered.csv', index=False)
