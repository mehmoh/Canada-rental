# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 16:30:46 2022

@author: mehdi
"""
def get_lat_lon(location, google_api_key):
  """
  Get latitude and longitude for a city.

  Parameters
  ----------
  @location [string]: Locatin entered by user from widget
  @google_api_key [string]: Api Key

  Returns
  -------
  [string]: Latitude and longitude

  """
  import requests

  # api-endpoint 
  URL = "https://maps.googleapis.com/maps/api/geocode/json"

  # defining a params dict for the parameters to be sent to the API 
  PARAMS = {'address':location, 'key':google_api_key} 

  # sending get request and saving the response as response object 
  r = requests.get(url = URL, params = PARAMS) 
  
  # get data from response
  data = r.json()
  
  # location
  location_dict = data['results'][0]['geometry']['location']
  lattitude = location_dict['lat']
  longitude = location_dict['lng']
  return lattitude, longitude
