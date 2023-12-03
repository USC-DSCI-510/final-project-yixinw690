import requests
import csv

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
