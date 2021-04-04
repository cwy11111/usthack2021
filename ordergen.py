import random
import time 
import requests
import smtplib
import json
import googlemaps

shop_location = "22.503118, 114.127934"
customer_location = ["22.495155, 114.124740", "22.492486, 114.134038", "22.501896, 114.149769", "22.501217, 114.145037", "22.501123, 114.140664", "22.495441, 114.133534"]
deliver_location = ["22.495753, 114.129859", "22.502755, 114.136238", "22.499384, 114.144838", "22.493396, 114.143485", "22.497333, 114.132870"]
deliver_method = ["Bicycling", "Driving", "Walking"]
radnom_c_location = random.randint(0, len(customer_location) - 1)
random_d_location = random.randint(0, len(deliver_location) - 1)
random_method = random.randint(0, len(deliver_method) - 1)

def location_cal():
    gmaps = googlemaps.Client(key = 'AIzaSyBTLsrhOvni6GkEG5NE5BrDSeNOHZLO7qc')
    my_dist = gmaps.distance_matrix(deliver_location[random_d_location], shop_location)['rows'][0]['elements'][0]
    print(my_dist["distance"]["text"])
location_cal()

def deliver_data_gen():
    global time 
    t = time.localtime()
    time = time.strftime("%H%M",t)
    #deliver_location = ""
    print(time)



def online_order():
    global time 
    t = time.localtime()
    time = time.strftime("%H%M",t)
    online_id = "A"+ str(random.randint(1,14))
    online_order_time = time
    driver_distance = random.uniform(0, 2)
    l1 = {"online_id" : online_id, "online_order_time" :  online_order_time, "driver_distance" : driver_distance}
    print(l1)

