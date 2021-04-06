import random
import time 
import requests
import smtplib
import json
import googlemaps

shop_location = "22.503118, 114.127934"
customer_location = ["22.495155, 114.124740", "22.492486, 114.134038", "22.501896, 114.149769", "22.501217, 114.145037", "22.501123, 114.140664", "22.495441, 114.133534"]
deliver_location = ["22.495753, 114.129859", "22.502755, 114.136238", "22.499384, 114.144838", "22.493396, 114.143485", "22.497333, 114.132870"]
deliver_method = ["driving", "walking"]
radnom_c_location = random.randint(0, len(customer_location) - 1)
random_d_location = random.randint(0, len(deliver_location) - 1)
random_method = random.randint(0, len(deliver_method) - 1)

def location_cal(): #calculate the distance and time for deliver to shop
    gmaps = googlemaps.Client(key = 'AIzaSyBTLsrhOvni6GkEG5NE5BrDSeNOHZLO7qc')
    my_dist = gmaps.distance_matrix(origins = deliver_location[random_d_location], destinations = shop_location, mode = deliver_method[random_method])['rows'][0]['elements'][0]
    time_deliver_to_shop = my_dist['duration']['value']
    distance_deliver_to_shop = my_dist['distance']['value']
    print("Time:", time_deliver_to_shop/60)
    print("Distance", distance_deliver_to_shop/1000)
    
location_cal()

def deliver_data_gen(): #Generate deliver data for testing 
    global time 
    t = time.localtime()
    time = time.strftime("%H%M",t)
    #deliver_location = ""
    print(time)


def online_order(): #Generate online order for testing
    global time 
    t = time.localtime()
    time = time.strftime("%H%M",t)
    online_id = "A"+ str(random.randint(1,14))
    online_order_time = time
    driver_distance = random.uniform(0, 2)
    l1 = {"online_id" : online_id, "online_order_time" :  online_order_time, "driver_distance" : driver_distance}
    print(l1)

