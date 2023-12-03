import requests
import csv

#download Yelp data
api_key = 'HBxoh_mhwT-KuOG-a7PI3txiDauDZJFSSXq5ejxNH436eSZFgxMMyoU8jJMHqGygYFzU5RGjse7NaDP62mrz58jvGfS_FHAxJdOQo5T5Z-erW5-dntZm5EG5Jo1KZXYx'
endpoint = 'https://api.yelp.com/v3/businesses/search'

params = {
    'location': 'Boston',
    'categories': 'restaurants',
    'limit': 50  # Number of results to retrieve per request (maximum is 50 per Yelp API limitations)
}

# Make the API requests and handle pagination
all_restaurants = []

offset = 0

while True:
    # Update the offset parameter
    params['offset'] = offset
    
    headers = {'Authorization': f'Bearer {api_key}'}
    response = requests.get(endpoint, params=params, headers=headers)

    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        for business in data['businesses']:
            name = business['name']
            categories = ', '.join([category['title'] for category in business['categories']])
            zip_code = business['location']['zip_code']
            all_restaurants.append({'Name': name, 'Cuisine Types': categories, 'Zip Code': zip_code})
        
        if len(data['businesses']) < params['limit']:
            break
        else:
            offset += params['limit']
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        break

csv_file_path = 'restaurants_in_boston.csv'

with open(csv_file_path, 'w', newline='') as csv_file:
    fieldnames = ['Name', 'Cuisine Types', 'Zip Code']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    writer.writeheader()

    for restaurant in all_restaurants:
        writer.writerow(restaurant)

print(f"Data has been written to {csv_file_path}")


#Download Census data
api_key = "80d5cb06b7e5347e9dd28960c0ab4f41c107d1e1"

base_url = "https://api.census.gov/data/2019/acs/acs5/profile"

zip_codes = ["02108", "02109", "02110", "02111", "02113", "02114", "02115", "02116", "02118", "02119", "02120", "02121", "02122", "02124", "02125", "02126", "02127", "02128", "02129", "02130", "02131", "02132", "02134", "02135", "02136", "02163", "02199", "02203", "02210", "02215", "02467"]

income_variables = [
    "DP03_0092E",  # Income less than $10,000
    "DP03_0093E",  # Income $10,000 to $14,999
    "DP03_0094E",  # Income $15,000 to $24,999
    "DP03_0095E",  # Income $25,000 to $34,999
    "DP03_0096E",  # Income $35,000 to $49,999
    "DP03_0097E",  # Income $50,000 to $74,999
    "DP03_0098E",  # Income $75,000 to $99,999
    "DP03_0099E",  # Income $100,000 to $149,999
    "DP03_0100E",  # Income $150,000 to $199,999
    "DP03_0101E",  # Income $200,000 or more
]

variable_mapping = {
    "DP03_0092E": "Income less than $10,000",
    "DP03_0093E": "Income $10,000 to $14,999",
    "DP03_0094E": "Income $15,000 to $24,999",
    "DP03_0095E": "Income $25,000 to $34,999",
    "DP03_0096E": "Income $35,000 to $49,999",
    "DP03_0097E": "Income $50,000 to $74,999",
    "DP03_0098E": "Income $75,000 to $99,999",
    "DP03_0099E": "Income $100,000 to $149,999",
    "DP03_0100E": "Income $150,000 to $199,999",
    "DP03_0101E": "Income $200,000 or more",
}

url = f"{base_url}?get={','.join(income_variables)}&for=zip%20code%20tabulation%20area:{','.join(zip_codes)}&in=state:25&key={api_key}"

response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    header_row = [variable_mapping.get(variable, variable) for variable in data[0]]

    rows = data[1:]

    for row in rows:
        for i in range(0, len(row)):  # Start from index 1 to skip the first column (Zip Code)
            if int(row[i]) <= 0:
                row[i] = 0

    with open('census_income_data_acs_boston.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)

        csv_writer.writerow(header_row)

        csv_writer.writerows(rows)

    print("Data has been successfully downloaded and saved to 'census_income_data_acs_boston.csv'.")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
    print(f"Error message: {response.text}")


