# https://www.zoopla.co.uk/for-sale/property/docklands/
# ?beds_max=2&beds_min=1&view_type=list
# &q=Docklands%2C%20London&results_sort=newest_listings&search_source=home

import numpy as np
import pandas as pd 
import requests
from bs4 import BeautifulSoup as soup

# from pprint import pprint

domain =  "https://www.zoopla.co.uk"
endpoint =  "/for-sale/property/docklands"
params = {
    "beds_min" : 1, 
    "beds_max" : 2,
    "view_type": "list",
    "search_source": "home",
    "q" : "Docklands, London", 
    "results_sort" : "newest_listings", 
}
#url = domain + endpoint
file_name = "new_out.html"
with open(file_name, encoding="utf-8") as f:
    lines = f.read()
    print(lines)

#r = requests.get(url, params=params)
page = lines

bsob = soup(page, "html.parser")
h2s_listing_titles = bsob.find_all('h2')
ps_listing_description = bsob.find_all('p', attrs={"data-testid": "listing-description"})

# next_link to replace url in r (request) functions

#ADDRESSES 

address_full = bsob.find_all ('p', attrs ={"class":"css-5agpw4"})
addresses = []
counter_0 = 0
for i in address_full:
    i = i.text.strip()
    addresses.append(i)
    counter_0 = counter_0 + 1

# print("Below are the addresses, stripped.")
# print(addresses)
# print(counter_0)
# print("----------------")

#DISTANCE TO PUBLIC TRANSPORT
distance_to_pub_transport_full = bsob.find_all('div', attrs={"data-testid":"listing-transport"})

distance_to_pub_transport = []
counter = 0 
index = 0
for i in distance_to_pub_transport_full:
    distance_divs = []
    div_children = i.find_all('div', attrs={"class":"ejjz7ko0"})

    for div in div_children: 
        div_clean = div.text.strip()
        distance_divs.append(div_clean)
    
    distance_to_pub_transport.append(distance_divs)
    counter = counter + 1

# print("Below is the distance to public transport, stripped.")
# print(distance_to_pub_transport)
# print(counter)
# print("----------------")


#LISTING PRICES 
listing_prices_full = bsob.find_all('p', attrs ={"class": "css-1w7anck ejgnygt31"})
listing_prices = []
counter_2 = 0
for i in listing_prices_full:
    i = i.text.strip()
    listing_prices.append(i)
    counter_2 = counter_2 + 1

# print("Below are the stripped listing prices")
# print(listing_prices)
# print(counter_2)
# print("----------------")
 
#BED NUMBERS
bed_numbers = []
counter_3 = 0 
for i in h2s_listing_titles : 
    i = i.text.strip()
    bed_numbers.append(i)
    counter_3 = counter_3 + 1

counter_3 = counter_3 -1
bed_numbers = bed_numbers[:-1]
# print("Below are the bed numbers stripped")
# print(bed_numbers)
# print(counter_3)
# print("----------------")

#DATE LISTED
date_listed_full = bsob.find_all('span', attrs ={"class": "css-dwkus2 ejgnygt34"})
date_listed = []
counter_4 = 0
for i in date_listed_full:
    i = i.text.strip()
    date_listed.append(i)
    counter_4 = counter_4 + 1

# print("Below are the stripped date listed")
# print(date_listed)
# print(counter_4)
# print("----------------")


#CREATING DATAFRAME 
#create dictionary of lists
data = {'prices': listing_prices, 'addresses': addresses, 'public_transport': distance_to_pub_transport, 'date_listed': date_listed, 'number_of_bedrooms': bed_numbers }


df = pd.DataFrame(data=data)
print(df)
df.info()

df['prices'] = df['prices'].replace('[£,]', '', regex=True).astype(int)
df['number_of_bedrooms'] = df['number_of_bedrooms'].replace('[a-z]', '', regex=True).astype(int)
print(df)
print("XX")
avg_price = df["prices"].mean()
print(f"Average price is £{avg_price}")

avg_price = df["prices"].mean()
print("----")
avg_price_room = df.groupby('number_of_bedrooms')['prices'].mean()
avg_price_room = avg_price_room.round(1)
avg_price_room = avg_price_room.reset_index(drop=False)
avg_price_room['prices'] = avg_price_room['prices'].astype(int)
print(avg_price_room)

#make this s
# script read from out.html file rather than url
#create own db using postgres and store data there
#how to connect to postgres with python

