import json
import random
import csv
import requests
from requests.structures import CaseInsensitiveDict
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Geoapify API key
api_key = os.getenv("GEOAPIFY_API_KEY")

# Categories to query
categories = {
    "Hotels": "accommodation.hotel",
    "Schools": "education.school",
    "Supermarkets": "commercial.supermarket",
    "Restaurants": "catering.restaurant",
    "Hospitals": "healthcare.hospital"
}

coordinates = [
    [-113.5837461, 53.5580047, "Canada"],
    [-123.1580021, 49.3355223, "Canada"],
    [-79.1230428, 44.1109564, "Canada"],
    [-73.637853, 45.4278599, "Canada"],
    [-72.827434, 46.5036479, "Canada"]
]

# Prepare CSV file
csv_file = "output.csv"
csv_columns = ["Country", "Average Hotels", "Average Schools", "Average Supermarkets", "Average Restaurants", "Average Hospitals"]
with open(csv_file, mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=csv_columns)
    writer.writeheader()  # Write the header row

    # Iterate through sampled points
    for coordinate in coordinates:
        lon, lat = coordinate[0], coordinate[1]

        results = {"Country": coordinate[2]}

        # Query Geoapify for each category
        total_features = 0
        total_categories = 0
        for label, category in categories.items():
            url = f"https://api.geoapify.com/v2/places?categories={category}&filter=circle:{lon},{lat},2000&limit=500&apiKey={api_key}"
            headers = CaseInsensitiveDict()
            headers["Accept"] = "application/json"
            
            resp = requests.get(url, headers=headers)
            if resp.status_code == 200:
                features = resp.json().get("features", [])
                feature_count = len(features)
                # Store intermediate category counts (only for calculation)
                results[label] = feature_count
                total_features += feature_count
                total_categories += 1
            else:
                print(f"Error querying {label} for point ({lon}, {lat}): {resp.status_code}")
                results[label] = 0
        
        # Calculate averages
        results["Average Hotels"] = results.get("Hotels", 0)
        results["Average Schools"] = results.get("Schools", 0)
        results["Average Supermarkets"] = results.get("Supermarkets", 0)
        results["Average Restaurants"] = results.get("Restaurants", 0)
        results["Average Hospitals"] = results.get("Hospitals", 0)

        # Remove category-specific counts before writing to the CSV
        results = {key: results[key] for key in csv_columns}

        # Write the data to the CSV
        writer.writerow(results)
        print(f"Written data for point: {coordinate}")

print(f"Results saved to {csv_file}")
