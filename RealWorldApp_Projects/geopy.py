## The process to convert address to its coordinates ie latitude and longitudes is called GEOCODING
##******************************************************************************************************************

import pandas as pd
from geopy.geocoders import Nominatim

# # USING GEOCODERS WITH A STRING OF ADDRESS:
# nom = Nominatim()   #create a Nominatim variable object and store that object in variable nom
#                     # then you point to the geocode method of the Nominatim object
#                     # and pass an address as s string in there
# a = nom.geocode("606 Columbia Avenue, North Bergen, NJ 07047")        # if you pass an unreal address you get None as output
# print type(a)                  # a is a special location object of geopy
# print a
# print a.latitude               # to get latitude
# print a.longitude              # to get longitude

##******************************************************************************************************************

## USING GEOCODERS WITH OUR DATAFRAME:

df1 = pd.read_csv("C:\Users\DIPESH\supermarkets.csv")

df1["Address"] = df1["Address"] + ", " + df1["City"] + ", " + df1["State"] + ", " + df1["Country"]
print df1

nmt = Nominatim()              #create a Nominatim variable object and store that object in variable nmt

df1["Coordinates"] = df1["Address"].apply(nmt.geocode)
##creates a new column "Coordinates". In that, add the coordinates of address in each row
## by using .apply() method of pandas and in brackets the method you want to apply ie nmt.goecode
print df1
print df1.Coordinates[0].latitude

df1["Latitude"] = df1["Coordinates"].apply(lambda x : x.latitude if x!=None else None)
df1["Longitude"] = df1["Coordinates"].apply(lambda x : x.longitude if x!=None else None)
## (lambda is an inline method to give a function
## x is a temporary variable in lambda which stores all the values of column 'Coordinates'
## x.latitude will apply the .latitude method to every value of the column and extract only the latitude
## and store it in the new column "Latitude"
## Have to use a if statement since one value of column "Coordinates" is None.)
print df1



