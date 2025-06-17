# Calculate the distance between the pick-up location and the drop location

import geopy.distance

def get_distance(location_1, location_2):

    distance = geopy.distance.distance(location_1, location_2).km

    return distance


def get_price_per_km(hour):

    if (hour > 8) & (hour < 11):
        price_per_km = 20
    elif (hour > 18) & (hour < 21):
        price_per_km = 15
    else:
        price_per_km = 10

    return price_per_km

def get_final_price(pick_up_location, drop_location, booking_hour):

    total_distance = get_distance(pick_up_location, drop_location)
    actual_price_per_km = get_price_per_km(booking_hour)

    final_price = round(total_distance * actual_price_per_km, 2)

    return final_price

# Inputs

pick_up_location = (18.5, 73.8)
drop_location = (21.1, 79.0)
booking_time = 10

get_final_price(pick_up_location, drop_location, booking_time)

get_distance(pick_up_location,drop_location)
