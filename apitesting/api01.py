#!/usr/bin/env python3

import datetime

"""Returning the location of the ISS in latitude/longitude"""
import requests

URL= "http://api.open-notify.org/iss-now.json"
def main():
    resp= requests.get(URL).json()
    
    timestamp = datetime.datetime.fromtimestamp(resp["timestamp"])
    lon = resp["iss_position"]["longitude"]
    lat = resp["iss_position"]["latitude"]

    print(f"""CURRENT LOCATION OF THE ISS:
    Timestamp: {timestamp}
    Lon: {lon}
    Lat: {lat}""")

if __name__ == "__main__":
    main()

