import requests
from datetime import datetime
import time

My_lat=25.594095
My_lng=85.137566
def check_long_lat():
    

    respose=requests.get(url="http://api.open-notify.org/iss-now.json")
    respose.raise_for_status()

    data=respose.json()
    longitude=float(data["iss_position"]["longitude"])
    latitude=float(data["iss_position"]["latitude"])

    if My_lat-5<=latitude<=My_lat+5 and My_lng-5<=longitude<=My_lng+5:
        return True


def is_night():
    
    date_format=0
    time_now=datetime.now().hour
    parameters={
            "lat":My_lat,
            "lng":My_lng,
            "formatted":date_format
    }

    respose=requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
    respose.raise_for_status()
    data=respose.json()
    sunrise=int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset=int(data["results"]["sunset"].split("T")[1].split(":")[0])
    if time_now>=sunset or time_now<=sunrise:
        return True
while True:
    time.sleep(60)
    if check_long_lat() and is_night():
        print("True")