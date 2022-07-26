travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
#ex use of function : add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

def add_new_country(country, times, lst_cities):
    new_entry = {
        "country": country,
        "visits": times,
        "cities": lst_cities
    
    }
    travel_log.append(new_entry)
    print(travel_log)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])