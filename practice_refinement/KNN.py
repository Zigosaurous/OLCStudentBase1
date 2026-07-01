import math

#### do not change this code
devices = {
    "523WR": ["Telmo",  "Speed23",  "PMD",     0.70, 1.10],
    "924MN": ["Lambo",  "Comfit1",  "PMD",     0.60, 1.15],
    "32XC" : ["Lambo",  "Zipline",  "Scooter", 0.35, 0.60],
    "A101X": ["Volt",   "Feather",  "Scooter", 0.32, 0.52],
    "D404Q": ["RoadMax","Urban",    "PMD",     0.66, 1.18],
}

print("Mobility Device Classifier (kNN, k = 1)")
print("Total devices loaded:", len(devices))
#### do not change this code

# Task 2.1 - Complete the function below
def distance2(p1x, p1y, p2x, p2y):
    # Task 2.1 – To be completed by student
    distance = math.sqrt( (p1x - p2x)**2 + (p1y - p2y)**2 )
    return distance


# Task 2.2 - Complete the function below
def predict_type_2d(devices_dict, newdevice_width, newdevice_length):
    # Task 2.2 – To be completed by student
    for i in devices_dict:
        width = i[3]
        length = i[4]
        type = i[2]

        distance = distance2(newdevice_width, newdevice_length, width, length)



# --- main flow (to be refined by you) ---
# Students will add input validation and output formatting later

