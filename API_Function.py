# Script with a function to get a temperature dataframe from API and covnert city/country name combinations into longitude and latitude

import requests
import pandas as pd

# get temp data from api
def get_temp_data(latitude, longitude, start_date, end_date):
    # construct parameters and get from API
    parameters = "latitude=" + latitude + "&longitude=" + longitude + "&start_date=" + start_date + "&end_date=" + end_date + "&hourly=temperature_2m"
    response = requests.get("https://archive-api.open-meteo.com/v1/archive?", params= parameters)

    # check api response code 
    assert response.status_code == 200, \
            f'Response Status Code was {response.status_code}'

    #return as data frame
    df = pd.DataFrame.from_dict(response.json()["hourly"])
    return df

# function to get longitude and latitude for city 
def get_long_lat(city, country):
    key = "46fdced00f5e406a883a3ebb0d532f7b" # key from opencagedata 
    response = requests.get("https://api.opencagedata.com/geocode/v1/json?q=" + city + "," + country + "&key=" + key)

    # check api response code 
    assert response.status_code == 200, \
            f'Response Status Code was {response.status_code}'
    
    # if response.json()["total_results"] > 1:
    #     print(response.json()["total_results"])

    return response.json()["results"][0]["geometry"]

# Code for testing 
if __name__ == '__main__':
    # test inputs 
    start_date = "2023-04-11"
    end_date = "2023-04-25"
    latitude = "47.91"
    longitude = "106.88"
    # test both functions
    print(get_temp_data(latitude, longitude, start_date, end_date))
    print(get_long_lat("Ulaanbaatar", "Mongolia"))