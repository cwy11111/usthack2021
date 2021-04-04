import random
import time 
import requests
import smtplib
import json

shop_location = "22.493706, 114.135351"
def location_cal():
    api_key = 'AIzaSyBTLsrhOvni6GkEG5NE5BrDSeNOHZLO7qc'
    source = input()
    dest = input()
    url ='https://maps.googleapis.com/maps/api/distancematrix/json?'
    r = requests.get(url + 'origins=' + source + '&destinations=' + dest + '&key=' + api_key)
    x = r.json()
    print(x)

def deliver_data_gen():
    global time 
    t = time.localtime()
    time = time.strftime("%H%M",t)
    deliver_location = ""
    print(time)
deliver_data_gen()


def online_order():
    global time 
    t = time.localtime()
    time = time.strftime("%H%M",t)
    online_id = "A"+ str(random.randint(1,14))
    online_order_time = time
    driver_distance = random.uniform(0, 2)
    l1 = {"online_id" : online_id, "online_order_time" :  online_order_time, "driver_distance" : driver_distance}
    print(l1)

