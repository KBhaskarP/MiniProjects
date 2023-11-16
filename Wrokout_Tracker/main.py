import requests


#API requirements:-
app_id="5d0ced6a"
app_key="a9f0dda3ad310cd45436bb33828282e7"
url_endpoint="https://trackapi.nutritionix.com/v2/natural/exercise"

#USER Information:-
GENDER = "male"
WEIGHT_KG = 84
HEIGHT_CM = 180
AGE = 32



statement="ran 3 miles"



headers={
    "x-app-id": app_id,
    "x-app-key":app_key,
    "Content-Type": "application/json"
    
}


params={
    "query":statement,
    "genders":GENDER,
    "weight_kg":WEIGHT_KG,
    "height_cm":HEIGHT_CM,
    "age":AGE
}

response=requests.post(url_endpoint,json=params,headers=headers)
response.raise_for_status()
result=response.json()
print(result)