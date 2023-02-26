from serpapi import GoogleSearch
from urllib.parse import urlsplit, parse_qsl
import pandas as pd
import json
import os  
import socket 
import geocoder
import requests
import time
import requests
import googlemaps



#from serpapi import GoogleSearch
def IPConverter():
    my_ip = get()
    g = geocoder.ip(my_ip)
    g = geocoder.ip('me')
    #print(g.latlng)
    return(g.latlng)
def get():
    endpoint = 'https://ipinfo.io/json'
    response = requests.get(endpoint, verify = True)

    if response.status_code != 200:
        return 'Status:', response.status_code, 'Problem with the request. Exiting.'
        exit()

    data = response.json()
    return data['ip']
ipAddress = "@" + str(IPConverter()[0]) + "," + str(IPConverter()[1]) + ",15z"
#print(ipAddress)
params = {
  "engine": "google_maps",
  "q": "ramen",
  "ll": ipAddress,
  "type": "search",
  "api_key": "5aa1909e29c5608f5423006db43d6f8332b1ab45dacd27380ae14ebae3ab26a5"
}

search = GoogleSearch(params)
results = search.get_dict()
local_results = results["local_results"]
restaurant_list = []
for x in range(len(local_results)):
    local_list = []
    local_list.append(local_results[0]["title"])
    local_list.append(local_results[0]["price"])
    local_list.append(local_results[0]["rating"])
    local_list.append(local_results[0]["address"])
    restaurant_list.append(local_list)