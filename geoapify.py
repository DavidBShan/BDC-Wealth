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
    "Power Line": "power.line",
    "Schools": "education",
    "Supermarkets": "commercial.supermarket",
    "Public Roads": "highway.public",
    "Hospitals": "healthcare.hospital"
}

coordinates1 = [
    [26.8949453, 55.0425501, "Belarus"],
    [30.2165276, 55.2064526, "Belarus"],
    [24.5936289, 51.9580389, "Belarus"],
    [30.6777232, 52.3278178, "Belarus"],
    [25.2975127, 53.0974312, "Belarus"],
    [-79.5809716, 43.7494669, "Canada"],
    [-81.3419952, 48.4687805, "Canada"],
    [-63.1328309, 46.2597643, "Canada"],
    [-73.6117814, 45.5397756, "Canada"],
    [-73.3187691, 45.5169113, "Canada"],
    [6.0859439, 46.2234937, "Switzerland"],
    [7.0932317, 46.1302232, "Switzerland"],
    [6.4991556, 46.8159969, "Switzerland"],
    [9.023574, 45.8272073, "Switzerland"],
    [8.035433, 46.8227673, "Switzerland"],
    [-70.666635, -33.433883, "Chile"],
    [-70.660121, -33.385981, "Chile"],
    [-71.431159, -33.044714, "Chile"],
    [-70.745273, -33.478628, "Chile"],
    [-70.609684, -33.590542, "Chile"],
    [114.2918855, 30.539157, "China"],
    [114.2944127, 30.541612, "China"],
    [114.2894522, 30.544546, "China"],
    [114.3005879, 30.529397, "China"],
    [114.2916292, 30.5445604, "China"],
    [-74.1363645, 4.6556926, "Colombia"],
    [-74.1536593, 4.6796393, "Colombia"],
    [-74.1590667, 4.6020484, "Colombia"],
    [-75.2406621, 6.8152785, "Colombia"],
    [-75.6170726, 6.163137, "Colombia"],
    [-68.8684258,12.0949651, "Curacao"],
    [-68.8759417,12.1469529, "Curacao"],
    [-68.9101896,12.1478183, "Curacao"],
    [-68.9180074,12.0991855, "Curacao"],
    [-68.8875512,12.1508563, "Curacao"],
    [14.1013083, 50.1015876, "Czechia"],
    [16.9726285, 49.2179752, "Czechia"],
    [16.3286777, 50.5939582, "Czechia"],
    [13.7532945, 50.6285271, "Czechia"],
    [15.6114176, 49.4076217, "Czechia"],
    [12.1453601, 54.0787257, "Germany"],
    [10.1809011, 53.6560712, "Germany"],
    [7.0996928,52.3002563, "Germany"],
    [9.2294309, 53.9841832, "Germany"],
    [8.838623, 53.0698454, "Germany"],
    [12.1798286, 55.7586516, "Denmark"],
    [12.0808955, 55.6387554, "Denmark"],
    [12.0603124, 55.8565065, "Denmark"],
    [10.1972806, 56.1544313, "Denmark"],
    [12.1788042, 55.4454771, "Denmark"]
]

coordinates2 = [
    [26.9370061, 58.7668527, "Estonia"],
    [24.9222049, 59.3565989, "Estonia"],
    [24.7743417, 59.4368551, "Estonia"],
    [26.9756269, 57.8316441, "Estonia"],
    [28.0478122, 59.4530906, "Estonia"],
    [-3.9898381, 37.2340288, "Spain"],
    [-4.8235766, 42.0305798, "Spain"],
    [-3.6166531, 42.3660715, "Spain"],
    [2.7142886, 39.7660973, "Spain"],
    [-5.8149515, 37.3325404, "Spain"],
    [25.5345005, 60.2848311, "Finland"],
    [26.8093229, 62.6795153, "Finland"],
    [23.9661479, 67.5417382, "Finland"],
    [26.7192216, 60.8849384, "Finland"],
    [25.6166084, 64.9495781, "Finland"],
    [-6.7181349, 62.1051357, "Faroe Islands"],
    [-6.8805316, 61.5257493, "Faroe Islands"],
    [-6.8445761, 61.9799181, "Faroe Islands"],
    [-6.8078848, 62.2415181, "Faroe Islands"],
    [-7.1495551, 62.0533473, "Faroe Islands"]
]

coordinates3 = [
    [-1.309324,46.14898, "France"],
    [4.702199,46.709927, "France"],
    [2.502553,49.318275, "France"],
    [3.229199,43.215871, "France"],
    [-1.843925,47.476822, "France"],
    [-2.6250246, 49.4341265, "Guernsey"],
    [-2.6021505, 49.4303591, "Guernsey"],
    [-2.5641316, 49.4883816, "Guernsey"],
    [-2.5492645, 49.4719204, "Guernsey"],
    [-2.5523375, 49.4640823, "Guernsey"],
    [-21.8618214, 64.1314708, "Iceland"],
    [-22.6601418, 64.8598524, "Iceland"],
    [-22.56773, 63.9995323, "Iceland"],
    [-21.9502182, 64.1508237, "Iceland"],
    [-21.9470522, 64.1466049, "Iceland"],
    [16.0262672, 46.1221098, "Croatia"],
    [15.7631616, 46.1292782, "Croatia"],
    [15.9332932, 45.4760625, "Croatia"],
    [16.4070434, 45.4875861, "Croatia"],
    [15.0921297, 45.4570742, "Croatia"]
]

coordinates4 = [
    [16.259355, 39.833536, "Italy"],
    [8.359175, 44.822806, "Italy"],
    [9.026985, 44.446313, "Italy"],
    [8.157207, 44.055319, "Italy"],
    [11.483278, 45.223985, "Italy"],
    [-76.9819708, 18.0192817, "Jamaica"],
    [-76.9460142, 18.012766, "Jamaica"],
    [-77.5334452, 17.8959701, "Jamaica"],
    [-77.6488922, 17.8907304, "Jamaica"],
    [-76.9826351, 18.0357077, "Jamaica"],
    [140.786692, 40.793296, "Japan"],
    [130.260056, 33.317046, "Japan"],
    [136.129328, 36.246084, "Japan"],
    [139.33551, 35.72791, "Japan"],
    [138.395808, 36.32683, "Japan"],
    [47.7181701,29.3205062, "Kuwait"],
    [47.7158442,29.3098451, "Kuwait"],
    [48.0692596,29.166644, "Kuwait"],
    [47.9123306,29.294308, "Kuwait"],
    [48.0751532,29.2447001, "Kuwait"]
]

coordinates5 = [
    [69.3604134, 53.2740534, "Kazakhstan"],
    [72.966374, 50.0570787, "Kazakhstan"],
    [74.9790102, 46.8557368, "Kazakhstan"],
    [71.3662384, 42.9172137, "Kazakhstan"],
    [76.9777801, 52.2659775, "Kazakhstan"],
    [9.5403085, 47.1972292, "Liechtenstein"],
    [9.5202683, 47.1458178, "Liechtenstein"],
    [9.6076317, 47.10107, "Liechtenstein"],
    [9.5159659, 47.170563, "Liechtenstein"],
    [9.5439791, 47.1983133, "Liechtenstein"],
    [24.7580756, 54.1207948, "Lithuania"],
    [22.5735631, 56.0583465, "Lithuania"],
    [22.356535, 56.2807666, "Lithuania"],
    [21.1633585, 55.6721611, "Lithuania"],
    [26.1634245, 55.2776081, "Lithuania"],
    [6.1192111, 49.5974771, "Luxembourg"],
    [6.0112512, 49.9943019, "Luxembourg"],
    [5.9028407, 49.9213959, "Luxembourg"],
    [6.1728625, 49.6904836, "Luxembourg"],
    [5.8935414, 49.559825, "Luxembourg"],
    [27.4232915, 56.6040616, "Latvia"],
    [26.6162455, 55.8677622, "Latvia"],
    [24.2076938, 56.4157295, "Latvia"],
    [25.6265499, 57.3243916, "Latvia"],
    [24.1008042, 56.9783733, "Latvia"],
    [-97.93409, 19.057036, "Mexico"],
    [-110.953835, 31.275437, "Mexico"],
    [-96.888864, 16.816741, "Mexico"],
    [-92.609308, 16.736841, "Mexico"],
    [-98.967558, 19.4354, "Mexico"],
    [166.4575051,-22.2648909, "New Caledonia"],
    [166.4795018,-22.2834421, "New Caledonia"],
    [166.4342924,-22.1336086, "New Caledonia"],
    [166.4425164,-22.2726996, "New Caledonia"],
    [166.5682155,-22.2514339, "New Caledonia"],
]

coordinates6 = [
    [4.8276518, 51.6451369, "Netherlands"],
    [4.4782983, 52.1480417, "Netherlands"],
    [4.9379126, 52.3636091, "Netherlands"],
    [4.8981283, 52.3394452, "Netherlands"],
    [5.8243085, 50.8575022, "Netherlands"],
    [8.1428143, 63.4439636, "Norway"],
    [10.4688911, 59.8761119, "Norway"],
    [9.5947519, 63.0925238, "Norway"],
    [9.069194, 63.6375595, "Norway"],
    [10.8352545, 59.750455, "Norway"],
    [174.8471171, -37.2535322, "New Zealand"],
    [176.7512609, -39.6529176, "New Zealand"],
    [174.7888639, -41.291736, "New Zealand"],
    [172.4083865, -43.6098834, "New Zealand"],
    [174.6547823, -36.9430823, "New Zealand"],
    [-8.7134368, 40.1527951, "Portugal"],
    [-8.4344878, 42.0703715, "Portugal"],
    [-8.9945596, 38.9562073, "Portugal"],
    [-8.6920487, 41.1817077, "Portugal"],
    [-9.1497994, 38.7097503, "Portugal"],
    [51.5052706,25.2808867, "Qatar"],
    [51.2939779,25.1693943, "Qatar"],
    [51.4182517,25.391092, "Qatar"],
    [51.4607365,25.2799549, "Qatar"],
    [51.529438,25.7284784, "Qatar"],
    [39.2682699, 21.4047134, "Saudi Arabia"],
    [41.0795327, 19.1286206, "Saudi Arabia"],
    [42.5615302, 16.9836155, "Saudi Arabia"],
    [43.9673534, 26.3253693, "Saudi Arabia"],
    [40.0104205, 21.5024985, "Saudi Arabia"],
    [103.6958369,1.3312731, "Singapore"],
    [103.6983709,1.326217, "Singapore"],
    [103.7497279,1.3129389, "Singapore"],
    [103.7709366,1.3343529, "Singapore"],
    [103.8780555,1.3319047, "Singapore"]
]

coordinates = [
    [14.4048067, 46.0012006, "Slovenia"],
    [15.2543291, 46.0681409, "Slovenia"],
    [13.6541502, 45.5136074, "Slovenia"],
    [15.395366, 46.0295093, "Slovenia"],
    [15.451291, 45.9443641, "Slovenia"],
    [18.6438321, 48.413131, "Slovakia"],
    [21.9575231, 48.9039439, "Slovakia"],
    [21.2366537, 49.0169019, "Slovakia"],
    [19.5904447, 49.0993114, "Slovakia"],
    [20.3235747, 48.4232622, "Slovakia"],
    [-55.332564, -33.60939, "Uruguay"],
    [-53.790474, -33.26496, "Uruguay"],
    [-56.291549, -34.80825, "Uruguay"],
    [-54.862362, -34.897149, "Uruguay"],
    [-56.268702, -34.887219, "Uruguay"],
    [20.4494533,42.7524654, "Kosovo"],
    [21.1770618,42.6555296, "Kosovo"],
    [21.1974337,42.3052405, "Kosovo"],
    [20.4120922,42.3692085, "Kosovo"],
    [20.966878,42.8203466, "Kosovo"],
    [25.6091266, -25.8933521, "South Africa"],
    [30.4116142, -29.6470015, "South Africa"],
    [30.4442485, -28.7515838, "South Africa"],
    [27.9302861, -26.1048432, "South Africa"],
    [29.7034734, -28.3302319, "South Africa"]
]

# Prepare CSV file
csv_file = "output.csv"
csv_columns = ["Country", "Average Power Line", "Average Schools", "Average Supermarkets", "Average Public Roads", "Average Hospitals"]
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
        results["Average Power Line"] = results.get("Power Line", 0)
        results["Average Schools"] = results.get("Schools", 0)
        results["Average Supermarkets"] = results.get("Supermarkets", 0)
        results["Average Public Roads"] = results.get("Public Roads", 0)
        results["Average Hospitals"] = results.get("Hospitals", 0)

        # Remove category-specific counts before writing to the CSV
        results = {key: results[key] for key in csv_columns}

        # Write the data to the CSV
        writer.writerow(results)
        print(f"Written data for point: {coordinate}")

print(f"Results saved to {csv_file}")
