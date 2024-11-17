import requests
import pandas as pd

# Fetch data from the SpaceX API
url = "https://api.spacexdata.com/v4/launches"
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    data = response.json()  # Parse the JSON data into a Python list
else:
    print(f"Error fetching data: {response.status_code}")
    data = []

# Convert the data to a pandas DataFrame
df = pd.DataFrame(data)

# Print the first five rows of the DataFrame
print(df.head())

# print(df[['name', 'success']].head())


