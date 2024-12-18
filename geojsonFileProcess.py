import json

file_path = "./dataset/countrywide-addresses-country.geojson"

features = []

with open(file_path, "r") as f:
    for line in f:
        try:
            feature = json.loads(line.strip())
            features.append(feature)
        except json.JSONDecodeError as e:
            print(f"Error decoding line: {line.strip()} - {e}")

feature_collection = {
    "type": "FeatureCollection",
    "features": features
}

output_file = "combined_feature_collection.geojson"
with open(output_file, "w") as out_f:
    json.dump(feature_collection, out_f, indent=4)

print(f"FeatureCollection saved to {output_file}")
