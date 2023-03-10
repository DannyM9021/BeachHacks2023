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

def searching(param):
    ipAddress = "@" + str(IPConverter()[0]) + "," + str(IPConverter()[1]) + ",15z"
    #print(ipAddress)
    params = {
    "engine": "google_maps",
    "q": param[0],
    "ll": ipAddress,
    "type": "search",
    "api_key": "5aa1909e29c5608f5423006db43d6f8332b1ab45dacd27380ae14ebae3ab26a5"
    } 
    priceRange = 0
    if str(param[1]) == "inexpensive":
        priceRange += 1
    elif str(param[1]) == "moderate":
        priceRange += 2
    else:
        priceRange += 3
    search = GoogleSearch(params)
    results = search.get_dict()
    local_results = results["local_results"]
    #print(local_results)
    restaurant_list = []
    #print(local_results)
    for x in range(len(local_results)):
        local_list = []
        if "price" in local_results[x]:
            if len(local_results[x]["price"]) == priceRange:
                local_list.append(local_results[x]["price"])
                if "title" in local_results[x]:
                    local_list.append(local_results[x]["title"])
                if "rating" in local_results[x]:
                    local_list.append(local_results[x]["rating"])
                if "address" in local_results[x]:
                    local_list.append(local_results[x]["address"])
                restaurant_list.append(local_list)
    return restaurant_list
