import requests
import pandas as pd

# Fetch the SpaceX data from the API
url = 'https://api.spacexdata.com/v4/launches'
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Load the JSON data into a pandas DataFrame
    data = response.json()  # Convert the response to JSON
    df = pd.DataFrame(data)  # Convert the JSON data to a DataFrame

    # Print the first 5 rows of the DataFrame
    print("First 5 rows of the DataFrame:")
    print(df.head())

    # Explore the DataFrame: Print columns and data types
    print("\nColumns in the DataFrame:")
    print(df.columns)
    
    print("\nData types of the DataFrame columns:")
    print(df.dtypes)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
