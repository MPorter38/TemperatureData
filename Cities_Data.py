# Script to construct dataframes for chosen city where dataframe contains an row for each city and then that city's avg temp

from API_Function import get_long_lat, get_temp_data
import pandas as pd
import numpy as np

def get_avg_temp(city, country):
    # pre defined start and end date
    end = "2023-04-01"
    start = "2018-04-01"

    # get coordinates
    lat = str(get_long_lat(city, country)['lat'])
    lng = str(get_long_lat(city, country)['lng'])
    
    # get all temperatures
    temps_df = get_temp_data(lat, lng, start, end)

    # return mean temperature
    return(temps_df["temperature_2m"].mean())


if __name__ == "__main__":
    # load list of capital cities
    # https://www.worlddata.info/capital-cities.ph
    Cities = pd.read_csv("CapitalCities.csv")

    avg_temps = []

    # loop over all cities
    for i in Cities.index:
        avg_temps.append(get_avg_temp(Cities["Country"][i], Cities["Capital City"][i]))

    df = pd.DataFrame( {"Cities": Cities["Country"], "Temp": avg_temps} )

    # test on first 5
    # for i in range(5):
    #     avg_temps.append(get_avg_temp(Cities["Country"][i], Cities["Capital City"][i]))

    # df = pd.DataFrame( {"Cities": Cities["Country"][0:5], "Temp": avg_temps} )

    # save to csv
    df.to_csv("AvgTemps.csv")
