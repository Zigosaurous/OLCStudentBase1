
############################################################
############################################################
# TASK 4 - DEVELOPMENT OF PROGRAM
############################################################

# A weather service is developing a program to predict whether
# it will rain.
#
# The prediction uses a 1-nearest-neighbour method based on
# two measurements:
# - temperature
# - wind speed
#
# Each historical weather record is stored in the format:
# [temperature, wind_speed, outcome]
#
# Use the following historical data in your program:

weather_data = [
    [30.0, 8.0, "No Rain"],
    [29.0, 12.0, "No Rain"],
    [27.0, 18.0, "Rain"],
    [25.0, 22.0, "Rain"],
    [32.0, 6.0, "No Rain"],
    [26.0, 16.0, "Rain"],
    [31.0, 10.0, "No Rain"],
    [28.0, 20.0, "Rain"]
]

# For a new set of weather measurements, the distance from
# each historical record is calculated using the Euclidean
# distance formula:
#
# distance =
# sqrt( (temperature1 - temperature2)^2
#                    +
#     (wind_speed1 - wind_speed2)^2 )
#
# The historical record with the smallest distance is the
# nearest neighbour.
#
# The prediction is the outcome stored in that historical
# record.
#
# You can assume that no two historical records will have the
# same distance from a new set of measurements.
#
# All code should have appropriate comments and all identifiers
# should be appropriately named. [4]


#------------------------------------------------------------
# Task 4.1 [4]
#------------------------------------------------------------

# Write a function calculate_distance() that calculates the
# Euclidean distance between two weather records.
#
# Function:
# calculate_distance(
#     temperature1,
#     wind_speed1,
#     temperature2,
#     wind_speed2
# )
#
# The function must:
# - use the distance formula given above;
# - return the calculated distance.

def calculate_distance(temperature1, wind_speed1, temperature2, wind_speed2): # defining the function with 4 parameter

    distance = ((temperature1 - temperature2)**2 +(wind_speed1 - wind_speed2)**2)**0.5 #using given formula to calculate distance
    return distance

#[3.4,5.6,4.8]

def find_nearest(distance_list): # defining find_nearest with one parameter
    smal_dist = distance_list[0] #defining variable num
    pos_smalles = 0
    for item in range(len(distance_list)): #looping through the values in the list
        if distance_list[item] < smal_dist: #finds the smallest value
            smal_dist = distance_list[item]
            pos_smalles = item
    return pos_smalles 
        
# print(find_nearest([3.4,5.6,4.8]))  test     

def predict_rain(current_teamperature, current_wind_speed, weather_data):
    dist_list = []
    temperature2 = weather_data[0]
    wind_speed2 = weather_data[1]
    for i in range(len(weather_data)):
        distance = calculate_distance(current_teamperature, current_wind_speed, temperature2, wind_speed2)
        dist_list.append(distance)

    pos = find_nearest(dist_list)
    








#------------------------------------------------------------
# Task 4.2 [4]
#------------------------------------------------------------

# Write a function find_nearest() that finds the position of
# the smallest distance in a list.
#
# Function:
# find_nearest(distance_list)
#
# Parameter:
#
# distance_list
# - Type: list of float values
# - Contains the distances from the new measurements to each
#   historical weather record.
#
# Return value:
# - Type: int
# - The index of the smallest value in distance_list.
#
# The function must:
# - search through distance_list to find the smallest distance;
# - return the index of the smallest distance.
#
# Do not use the min() function or the index() method in this
# function.









#------------------------------------------------------------
# Task 4.3 [5]
#------------------------------------------------------------

# Write a function predict_rain() that predicts the weather
# outcome for a new set of measurements.
#
# Function:
# predict_rain(
#     current_temperature,
#     current_wind_speed,
#     weather_data
# )
#
# Parameters:
#
# current_temperature
# - Type: float
# - The new temperature measurement.
#
# current_wind_speed
# - Type: float
# - The new wind speed measurement.
#
# weather_data
# - Type: list
# - The historical weather records supplied in the question.
#
# Return value:
# - Type: str
# - Either "Rain" or "No Rain", taken from the nearest
#   historical record.
#
# The function must:
# - create a list containing the distance from the new
#       measurements to every historical record;
# - call calculate_distance() for every historical record
#       when creating the list of distances;
# - call find_nearest() to obtain the index of the nearest
#       historical record;
# - return the outcome stored in the nearest historical record.







#------------------------------------------------------------
# Task 4.4 [8]
#------------------------------------------------------------

# Copy and paste your program from Task 4.3.
#
# The weather service requires an interface that can make and
# save several predictions.
#
# Extend your program so that it:
# - asks the user to input the current temperature as a float;
# - asks the user to input the current wind speed as a float;
# - calls predict_rain() to obtain the prediction;
# - outputs the prediction using a suitable message;
#
# - stores the temperature, wind speed, prediction as one
#   string in a list called prediction_records; use "commas"
#   as separators
#
# - asks whether another prediction is required and repeats
#   while the user enters Y;
#
# - after data entry has finished, writes every item in
#   prediction_records to the file:  weather_predictions.txt
#   with one prediction on each line;

#
# You can assume that:
# - all temperature and wind speed inputs are valid numeric
#   values;
# - the response to continue will be Y or N.

